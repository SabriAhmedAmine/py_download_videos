# UDL (Termux) — YouTube / TikTok / Instagram Downloader (Interactive)

Interactive downloader for Android using **Termux + yt-dlp + ffmpeg**.

✅ Prompts you for:
1) URL (one time)  
2) Video/Audio (**v/a**)  
3) Quality (**Enter = best**, or **1/2/3/...**)  

✅ Auto-detects:
- Platform: YouTube / Instagram / TikTok
- Playlist / Instagram carousel → creates a **folder named after the playlist** and downloads everything inside it

✅ Saves to a folder you can open from your phone’s **Files app** (not only Termux).

> Use only for content you own or have permission to download.

---

## 1) Install Termux (IMPORTANT)

Install **Termux from F-Droid or GitHub releases** (recommended).  
Avoid random APK sites.

---

## 2) One-time setup in Termux

Open Termux and run:

```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install -y python ffmpeg
python -m pip install -U pip yt-dlp
```

### If you get mirror/DNS errors during update
Try:

```bash
termux-change-repo
pkg update && pkg upgrade -y
```

If you still see DNS errors like “No address associated with hostname”, check Android network settings:
- Disable VPN temporarily
- Disable “Private DNS” custom hostname / adblock DNS
- Reconnect Wi‑Fi or toggle airplane mode

---

## 3) Create the script

Create/edit:

```bash
nano ~/udl.py
```

Paste your `udl.py` script code, then save:
- Save: `CTRL + O` then `Enter`
- Exit: `CTRL + X`

---

## 4) Recommended output location (phone-accessible)

To access downloads from your phone’s normal **Files / Gallery / Music** apps, save to shared storage:

**Recommended path:**
- `/storage/emulated/0/Download/UniversalDownloader`

In your script, make sure this line exists:

```python
DEFAULT_DEST = Path("/storage/emulated/0/Download/UniversalDownloader")
```

---

## 5) Run it

```bash
python ~/udl.py
```

The script will ask:
- `URL:`
- `Video or Audio? (v/a):`
- Quality menu (press **Enter** for best)

---

## 6) Where files are saved (and how to find them)

Open your phone’s **Files / My Files / File Manager** app:
- Internal storage → **Download** → **UniversalDownloader**

Files:
- Video: `.mp4`
- Audio: `.mp3`

If the URL is a playlist/carousel, you’ll see:
- Download/UniversalDownloader/**<Playlist Title>**/…

---

## 7) Cookies (optional but recommended)

Cookies help when:
- Instagram needs login / private content
- YouTube shows “sign in / bot check”
- TikTok blocks without a logged-in session

### Setup cookies auto-load
1) Export cookies from a browser where you’re logged in (Netscape format `cookies.txt`)
2) Copy `cookies.txt` to your phone (Downloads is fine)
3) In Termux:

```bash
mkdir -p ~/.config/udl
cp ~/storage/downloads/cookies.txt ~/.config/udl/cookies.txt
```

If this file exists:
- `~/.config/udl/cookies.txt`
…the script will use it automatically.

---

## 8) Updating (when a site changes / downloads fail)

Update yt-dlp (most common fix):

```bash
python -m pip install -U yt-dlp
```

Update Termux packages:

```bash
pkg update && pkg upgrade -y
```

---

## 9) Troubleshooting

### “Storage” / “Permission denied” for Downloads
Run again and allow permission:

```bash
termux-setup-storage
```

Then reopen Termux and retry.

### “No address associated with hostname”
That’s DNS/network. Fix Android network settings (VPN/Private DNS/adblock DNS), then retry:
```bash
pkg update
```

### “ffmpeg not found” / merging fails
Install ffmpeg:
```bash
pkg install -y ffmpeg
```

---

## Notes
- Some platforms change often. Updating **yt-dlp** is the #1 fix.
- You are responsible for how you use this tool and respecting copyright/ToS.
