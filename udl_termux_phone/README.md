# UDL (Termux) — Universal Media Downloader

Interactive downloader for **YouTube / Instagram / TikTok** using **Termux + yt-dlp + ffmpeg**.

This script is designed for Android users who want a simple, interactive downloader that saves files directly to phone-accessible storage.

> ⚠️ Use only for content you own or have permission to download.

---

## Features

- Interactive prompts (no long commands)
- Supports **video or audio**
- Quality selection (best by default)
- Auto-detects platforms
- Playlists / Instagram carousels saved into folders
- Saves to **Internal Storage → Download**

---

## 1) Install Termux

Install Termux from **F-Droid or GitHub releases** (recommended).

---

## 2) One-time setup

```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install -y python ffmpeg
python -m pip install -U pip yt-dlp
```

---

## 3) Create the script

```bash
nano ~/udl.py
```

Paste your script and save.

---

## 4) Output location (phone-accessible)

Recommended path:

```
/storage/emulated/0/Download/UniversalDownloader
```

Make sure your script uses:

```python
DEFAULT_DEST = Path("/storage/emulated/0/Download/UniversalDownloader")
```

---

## 5) Run

```bash
python ~/udl.py
```

---

## 6) Create a shortcut command (alias)

Edit shell config:

```bash
nano ~/.bashrc
```

Add:

```bash
alias your_alis='python /data/data/com.termux/files/home/udl.py'
```

Reload:

```bash
source ~/.bashrc
```

Run anywhere:

```bash
your_alis
```

---

## 7) Cookies (optional)

```bash
mkdir -p ~/.config/udl
cp ~/storage/downloads/cookies.txt ~/.config/udl/cookies.txt
```

---

## Notes

- Update yt-dlp often
- Respect copyright and platform terms
