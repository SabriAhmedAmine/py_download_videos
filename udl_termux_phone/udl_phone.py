"""
UDL (Termux) — Interactive YouTube / TikTok / Instagram downloader (yt-dlp)

Flow:
- Ask URL once
- Ask mode: v/a
- Ask quality: Enter=best, or 1/2/3/4/...
- Detect platform + detect playlist/carousel
- If playlist -> create folder named after playlist title and download items into it
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, Optional

from yt_dlp import YoutubeDL

#DEFAULT_DEST = Path.home() / "storage" / "downloads" / "UniversalDownloader"
DEFAULT_DEST = Path("/storage/emulated/0/Download/UniversalDownloader")
DEFAULT_COOKIES = Path.home() / ".config" / "udl" / "cookies.txt"


def detect_platform(url: str) -> str:
    if re.search(r"(youtube\.com|youtu\.be)", url, re.I):
        return "YouTube"
    if re.search(r"instagram\.com", url, re.I):
        return "Instagram"
    if re.search(r"tiktok\.com", url, re.I):
        return "TikTok"
    return "Unknown"


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def sanitize_folder_name(name: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*\n\r\t]', "_", (name or "").strip())
    safe = re.sub(r"\s+", " ", safe).strip()
    return (safe[:120] or "Playlist")


def progress_hook(d: Dict[str, Any]) -> None:
    st = d.get("status")
    if st == "downloading":
        pct = (d.get("_percent_str") or "").strip()
        spd = (d.get("_speed_str") or "").strip()
        eta = (d.get("_eta_str") or "").strip()
        print(f"\r⬇️  {pct} | {spd} | ETA {eta}", end="", flush=True)
    elif st == "finished":
        print("\n✅ Download finished. Post-processing…", flush=True)


def pick_cookies() -> Optional[str]:
    return str(DEFAULT_COOKIES) if DEFAULT_COOKIES.exists() else None


def extract_info(url: str, cookiefile: Optional[str]) -> Dict[str, Any]:
    opts: Dict[str, Any] = {"quiet": True, "skip_download": True}
    if cookiefile:
        opts["cookiefile"] = cookiefile
    with YoutubeDL(opts) as ydl:
        return ydl.extract_info(url, download=False)


def ask_url() -> str:
    while True:
        u = input("URL: ").strip()
        if u:
            return u
        print("Please paste a URL.")


def ask_mode() -> str:
    while True:
        m = input("Video or Audio? (v/a): ").strip().lower()
        if m in ("v", "video"):
            return "video"
        if m in ("a", "audio"):
            return "audio"
        print("Type 'v' for video or 'a' for audio.")


def ask_quality(mode: str) -> str:
    if mode == "video":
        print("\nQuality (press Enter = best):")
        print("  1) 1080p")
        print("  2) 720p")
        print("  3) 480p")
        print("  4) 360p")
        print("  5) 1440p")
        print("  6) 2160p (4K)")
        while True:
            q = input("Choose: ").strip()
            if q == "":
                return "best"
            mapping = {"1": "1080", "2": "720", "3": "480", "4": "360", "5": "1440", "6": "2160"}
            if q in mapping:
                return mapping[q]
            print("Choose Enter or a number (1-6).")
    else:
        print("\nAudio quality (press Enter = best):")
        print("  1) 256 kbps")
        print("  2) 192 kbps")
        print("  3) 128 kbps")
        while True:
            q = input("Choose: ").strip()
            if q == "":
                return "best"
            mapping = {"1": "256", "2": "192", "3": "128"}
            if q in mapping:
                return mapping[q]
            print("Choose Enter or a number (1-3).")


def build_video_format(cap: str) -> str:
    if cap in ("best", "", "auto"):
        return "bestvideo+bestaudio/best"
    # cap is like "1080"
    return f"bestvideo[height<={cap}]+bestaudio/best"


def audio_preferred_quality(q: str) -> str:
    # FFmpegExtractAudio preferredquality: "0"=best, or bitrate string
    if q in ("best", "", "0"):
        return "0"
    return q


def main() -> int:
    url = ask_url()
    mode = ask_mode()
    quality = ask_quality(mode)

    platform = detect_platform(url)
    print(f"\n📌 Platform detected: {platform}")

    dest_root = DEFAULT_DEST
    ensure_dir(dest_root)

    cookiefile = pick_cookies()
    if cookiefile:
        print(f"🍪 Cookies detected: {cookiefile}")

    # Detect playlist/carousel (Instagram carousels often show as playlist)
    info = extract_info(url, cookiefile=cookiefile)
    is_playlist = isinstance(info, dict) and info.get("_type") == "playlist"

    if is_playlist:
        pl_title = sanitize_folder_name(info.get("title") or "Playlist")
        dest = dest_root / pl_title
        ensure_dir(dest)
        outtmpl = str(dest / "%(playlist_index)03d - %(title).120B [%(id)s].%(ext)s")
        noplaylist = False
        print(f"📚 Playlist/Carousel detected → folder: {pl_title}")
    else:
        dest = dest_root
        outtmpl = str(dest / "%(title).120B [%(id)s].%(ext)s")
        # Prevent accidentally downloading a whole playlist if URL contains list=...
        noplaylist = True
        print("🎯 Single item detected.")

    common: Dict[str, Any] = {
        "outtmpl": outtmpl,
        "noplaylist": noplaylist,
        "retries": 10,
        "fragment_retries": 10,
        "concurrent_fragment_downloads": 4,
        "progress_hooks": [progress_hook],
        "continuedl": True,
        "writethumbnail": True,
    }
    if cookiefile:
        common["cookiefile"] = cookiefile

    if mode == "audio":
        ydl_opts = {
            **common,
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": audio_preferred_quality(quality),
                },
                {"key": "EmbedThumbnail"},
                {"key": "FFmpegMetadata"},
            ],
        }
        print(f"🎵 Mode: AUDIO (MP3) | Quality: {quality}")
    else:
        ydl_opts = {
            **common,
            "format": build_video_format(quality),
            "merge_output_format": "mp4",
            "postprocessors": [
                {"key": "EmbedThumbnail"},
                {"key": "FFmpegMetadata"},
            ],
        }
        print(f"🎬 Mode: VIDEO | Quality cap: {quality} | Output: MP4")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n✅ All done.")
    print(f"📂 Saved in: {dest_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
