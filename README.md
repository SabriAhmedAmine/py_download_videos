# 🎥 Universal Video Downloader Pro

A powerful and user-friendly Python tool for downloading **videos and audio** from **YouTube, Instagram, and TikTok** with customizable quality options. Supports both **individual videos/posts** and **entire playlists**.

This repository includes:
- **Desktop GUI** downloader (Windows/macOS/Linux)
- **Android (Termux) interactive CLI** downloader (recommended for phones)

> ⚠️ Note: Site support can change over time. This project relies on **yt-dlp**, so updating yt-dlp is often the #1 fix when something stops working.

---

## ✨ Features

- **Multi-Platform Support**: Download from YouTube, Instagram, and TikTok (as supported by yt-dlp)
- **Video Downloads**: Download videos in your preferred resolution
- **Audio Extraction**: Extract high-quality audio in MP3 format
- **Playlist Support**: Download entire playlists automatically
- **Quality Selection**: Choose from available resolutions and audio bitrates
- **Smart Organization**: Automatic folder creation for playlists
- **Format Conversion**: Automatic conversion to MP4 (video) and MP3 (audio)
- **Metadata Embedding**: Adds metadata and thumbnails to downloaded files
- **Desktop GUI**: User-friendly graphical interface with real-time progress
- **Android (Termux) CLI**: Interactive prompts for URL / mode / quality (no options to memorize)

---

## 🚀 Quick Start

### Prerequisites (Desktop)

- Python **3.7+**
- **FFmpeg** (required for format conversion/merging)

### Installation (Desktop)

1) **Clone the repository**
```bash
git clone https://github.com/SabriAhmedAmine/py_download_videos.git
cd youtube-downloader
```

2) **Install required dependencies**
```bash
pip install -U yt-dlp
```

3) **Install FFmpeg**

**Windows**
- Download from https://ffmpeg.org/download.html  
- Add FFmpeg to your system PATH

**macOS**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian)**
```bash
sudo apt update
sudo apt install ffmpeg
```

---

## 📖 Usage

## 🎬 Option 1: Universal Video Downloader (Recommended Desktop GUI)

**File:** `UniversalDownloader (Youtube_Insta_Tiktok).py`

Run:
```bash
python "UniversalDownloader (Youtube_Insta_Tiktok).py"
```

### Supported Platforms (via yt-dlp)
- ✅ YouTube (Videos, Shorts, Playlists)
- ✅ Instagram (Posts, Reels, Carousels; some content may require login/cookies)
- ✅ TikTok (Videos; some regions/content may require login/cookies)

### Features (GUI)
- Paste YouTube, Instagram, or TikTok URL
- Automatic platform detection
- Choose video resolutions (1080p, 720p, 480p, etc.)
- Multiple audio quality options for MP3 extraction
- Automatic MP4/MP3 conversion (FFmpeg)
- Playlist support with organized folders
- Custom destination folders
- Real-time download progress tracking
- Modern interface with progress bar and activity log

Example workflow:
1. Run the application (GUI window opens)
2. Enter a URL
3. Click **Analyze** (detect content type)
4. Choose **Video** or **Audio (MP3)**
5. Select quality
6. Choose destination folder (optional)
7. Click **DOWNLOAD NOW**

---

## 🎵 Option 2: YouTube-Only Downloader (Legacy)

**File:** `Amine's Youtube downloader .py`

Run:
```bash
python "Amine's Youtube downloader .py"
```

Supported:
- ✅ YouTube only (Videos & Playlists)

Notes:
- Legacy script maintained for YouTube-specific use cases.
- For multi-platform support, use the Universal Downloader above.

---

## 📱 Option 3: Android (Termux) — Interactive CLI (Recommended for phones)

This is the simplest way to run the downloader on Android without building an APK.

### 3.1 Install Termux (IMPORTANT)
Install Termux from **F-Droid** or **GitHub Releases** (recommended). Avoid random APK sites.

### 3.2 One-time setup in Termux
Open Termux and run:
```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install -y python ffmpeg
python -m pip install -U pip yt-dlp
```

If you get mirror/DNS errors:
```bash
termux-change-repo
pkg update && pkg upgrade -y
```

### 3.3 Run the Android script
**File:** `udl.py`

Run:
```bash
python udl.py
```

The script will ask:
- URL (one time)
- Video or Audio? (v/a)
- Quality (Enter = best, or 1/2/3/...)

### 3.4 Phone-accessible output folder
To access downloads from the phone’s **Files** app (not Termux), set the destination to:
- `/storage/emulated/0/Download/UniversalDownloader`

In `udl.py`, ensure:
```python
DEFAULT_DEST = Path("/storage/emulated/0/Download/UniversalDownloader")
```

### 3.5 Cookies (optional but recommended)
Cookies help with:
- Instagram private content / login-required posts
- YouTube “sign in / bot check”
- Some TikTok restrictions

Steps:
1) Export cookies in **Netscape cookies.txt** format from a logged-in browser
2) Copy `cookies.txt` to your phone (Downloads)
3) In Termux:
```bash
mkdir -p ~/.config/udl
cp ~/storage/downloads/cookies.txt ~/.config/udl/cookies.txt
```
If `~/.config/udl/cookies.txt` exists, the script can be configured to auto-use it.

---

## 📁 File Structure

```
py_download_videos/
├── UniversalDownloader (Youtube_Insta_Tiktok).py    # Main downloader (YouTube, Instagram, TikTok) - Desktop GUI
├── Amine's Youtube downloader .py                   # Legacy YouTube downloader (French)
├── udl.py                                           # Android (Termux) interactive CLI downloader
├── README.md                                        # This file
└── downloads/                                       # Default download folder (desktop)
```

---

## 🎛️ Configuration Options

### Supported Platforms
- **YouTube**: Videos, Shorts, Playlists
- **Instagram**: Posts, Reels, Carousels (some content may require cookies/login)
- **TikTok**: Videos (some content may require cookies/login)

### Video Quality Options
- **Automatic**: Best available quality
- **2160p (4K)**: Ultra High Definition
- **1440p (2K)**: High Definition
- **1080p (Full HD)**: Full Definition
- **720p (HD)**: Standard Definition
- **480p / 360p**: Low bandwidth options
- **Format**: Automatically converted to MP4

### Audio Quality Options
- **Best available**
- **256 kbps**: Very high quality
- **192 kbps**: High quality (recommended)
- **128 kbps**: Standard quality

---

## ⚠️ Important Notes

- **Legal Compliance**: Only download content you have permission to download
- **Copyright & Terms**: Respect the terms of service of each platform
- **FFmpeg Required**: Ensure FFmpeg is installed for merging/conversion
- **Internet Connection**: Stable connection recommended
- **Platform Changes**: If something stops working, **update yt-dlp** first:
  ```bash
  python -m pip install -U yt-dlp
  ```

---

## 🐛 Troubleshooting

### “FFmpeg not found”
- Install FFmpeg and ensure it’s on PATH (desktop)
- On Termux:
  ```bash
  pkg install -y ffmpeg
  ```

### Downloads fail / extraction errors
- Update yt-dlp:
  ```bash
  python -m pip install -U yt-dlp
  ```
- Use cookies if login is required (Instagram private, YouTube bot check, etc.)

### Termux “No address associated with hostname”
- DNS/network issue (VPN/Private DNS/adblock DNS). Disable them temporarily and retry:
  ```bash
  pkg update && pkg upgrade -y
  ```

### Permission errors (Android storage)
- Run and allow permission prompt:
  ```bash
  termux-setup-storage
  ```

---

## 🤝 Contributing

Contributions are welcome:
1. Report bugs (open an issue with logs and your environment)
2. Suggest features
3. Submit pull requests
4. Improve documentation

Development setup:
```bash
git clone https://github.com/SabriAhmedAmine/py_download_videos.git
cd py_download_videos
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -U yt-dlp
```

---

## 📄 License

This project is licensed under the MIT License — see the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- **yt-dlp**: https://github.com/yt-dlp/yt-dlp
- **FFmpeg**: https://ffmpeg.org/
- Platforms: YouTube, Instagram, TikTok

---

⭐ Star this repository if you find it helpful!
