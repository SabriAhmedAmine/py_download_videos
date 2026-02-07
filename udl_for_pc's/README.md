# 🎥 Universal Video Downloader Pro

A powerful and user-friendly Python tool for downloading videos and audio from YouTube, Instagram, and TikTok with customizable quality options. Supports both individual videos/posts and entire playlists.

## ✨ Features

- **Multi-Platform Support**: Download from YouTube, Instagram, and TikTok
- **Video Downloads**: Download videos in your preferred resolution
- **Audio Extraction**: Extract high-quality audio in MP3 format
- **Playlist Support**: Download entire playlists automatically
- **Quality Selection**: Choose from available resolutions and audio bitrates
- **Smart Organization**: Automatic folder creation for playlists
- **Format Conversion**: Automatic conversion to MP4 (video) and MP3 (audio)
- **Interactive GUI**: User-friendly graphical interface with real-time progress
- **Metadata Embedding**: Adds metadata and thumbnails to downloaded files

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- FFmpeg (required for format conversion)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/SabriAhmedAmine/youtube-downloader.git
   cd youtube-downloader
   ```

2. **Install required dependencies**

   ```bash
   pip install yt-dlp
   ```

3. **Install FFmpeg**

   **Windows:**

   - Download from [FFmpeg official site](https://ffmpeg.org/download.html)
   - Add to your system PATH

   **macOS:**

   ```bash
   brew install ffmpeg
   ```

   **Linux (Ubuntu/Debian):**

   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

## 📖 Usage

### 🎬 Option 1: Universal Video Downloader (Recommended)

**File:** `UniversalDownloader (Youtube_Insta_Tiktok).py`

Download videos from YouTube, Instagram, or TikTok with a modern user-friendly GUI:

```bash
python "UniversalDownloader (Youtube_Insta_Tiktok).py"
```

**Supported Platforms:**

- ✅ YouTube (Videos, Shorts, Playlists)
- ✅ Instagram (Posts, Reels, Stories)
- ✅ TikTok (Videos, Collections)

**Features:**

- Paste YouTube, Instagram, or TikTok URL
- Automatic platform detection
- Choose from available resolutions for videos (1080p, 720p, 480p, etc.)
- Multiple audio quality options (64-320 kbps) for MP3 extraction
- Automatic MP4/MP3 format conversion
- Playlist support with organized folders
- Custom destination folders
- Real-time download progress tracking
- Modern graphical interface with progress bar and activity log

**Example workflow:**

1. Run the application (GUI window opens)
2. Enter YouTube, Instagram, or TikTok URL
3. Click "Analyze" to detect content type
4. Choose format (Video or Audio MP3)
5. Select desired quality from dropdown
6. Choose destination folder (optional)
7. Click "DOWNLOAD NOW" to begin

---

### 🎵 Option 2: YouTube-Only Downloader (Legacy)

**File:** `Amine's Youtube downloader .py`

A dedicated YouTube video and audio downloader with French interface:

```bash
python "Amine's Youtube downloader .py"
```

**Supported Format:**

- ✅ YouTube only (Videos & Playlists)

**Features:**

- Specialized for YouTube downloads
- High-quality video downloads with resolution selection
- MP3 audio extraction
- Playlist support with automatic organization
- Detailed progress tracking and logging
- French language interface

**Note:** This is a legacy script maintained for YouTube-specific use cases. For multi-platform support, use the Universal Video Downloader instead.

## 📁 File Structure

```
py_download_videos/
├── UniversalDownloader (Youtube_Insta_Tiktok).py    # Main downloader (YouTube, Instagram, TikTok)
├── Amine's Youtube downloader .py                   # Legacy YouTube downloader (French)
├── README.md                                         # This file
└── downloads/                                        # Default video download folder
```

## 🎛️ Configuration Options

### Supported Platforms

- **YouTube**: Videos, Shorts, Playlists
- **Instagram**: Posts, Reels, Stories
- **TikTok**: Videos, Collections

### Video Quality Options

- **Automatic**: Best available quality
- **2160p (4K)**: Ultra High Definition
- **1440p (2K)**: High Definition
- **1080p (Full HD)**: Full Definition
- **720p (HD)**: Standard Definition
- **480p / 360p**: Low bandwidth options
- **Format**: Automatically converted to MP4

### Audio Quality Options

- **320 kbps**: Maximum quality (FLAC equivalent)
- **256 kbps**: Very high quality
- **192 kbps**: High quality (recommended)
- **128 kbps**: Standard quality

## 🔧 Advanced Usage

### Platform Detection

The application automatically detects the platform from the URL:

- **YouTube**: youtube.com, youtu.be, youtube.com/shorts
- **Instagram**: instagram.com (posts, reels, stories)
- **TikTok**: tiktok.com (@, video/, discover/)

### Custom Download Paths

The GUI allows you to specify custom download directories:

- Browse button opens folder selection dialog
- Defaults to your Downloads folder
- All files are organized automatically

### Playlist Downloads

When downloading playlists:

- **Videos**: Creates a folder with the playlist name
- **Audio**: Creates a folder for playlist audio files
- All files are indexed automatically (01-, 02-, etc.)

## ⚠️ Important Notes

- **Legal Compliance**: Only download content you have permission to download
- **Copyright & Terms**: Respect the terms of service of each platform (YouTube, Instagram, TikTok)
- **Rate Limiting**: The tool respects platform rate limits and guidelines
- **FFmpeg Required**: Ensure FFmpeg is properly installed for format conversion
- **Internet Connection**: Stable connection required for reliable downloads
- **File Permissions**: Ensure write access to destination folder

## 🐛 Troubleshooting

### Common Issues

**"FFmpeg not found" error:**

- Ensure FFmpeg is installed and added to your system PATH
- Restart your terminal/command prompt after installation

**Download fails:**

- Check your internet connection
- Verify the YouTube URL is correct and accessible
- Some videos may have download restrictions

**Permission errors:**

- Ensure you have write permissions to the destination folder
- Try running as administrator/sudo if necessary

### Error Messages

- **"An error occurred"**: Check the URL and your internet connection
- **"Invalid choice"**: Enter a valid number from the available options
- **"Invalid input"**: Follow the prompt format exactly

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report Bugs**: Open an issue with detailed information
2. **Suggest Features**: Share your ideas for improvements
3. **Submit Pull Requests**: Help improve the code
4. **Update Documentation**: Help keep the README current

### Development Setup

```bash
# Fork the repository
git clone https://github.com/SabriAhmedAmine/youtube-downloader.git
cd youtube-downloader

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install yt-dlp
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: The powerful multi-platform video downloading library
- **[FFmpeg](https://ffmpeg.org/)**: Essential for audio/video processing and format conversion
- **Platforms**: YouTube, Instagram, and TikTok

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Verify FFmpeg is installed and in your system PATH
3. Ensure your internet connection is stable
4. Check that the URL is valid and accessible

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ for content creators and video enthusiasts
