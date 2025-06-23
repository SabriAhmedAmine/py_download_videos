# 🎥 YouTube Video & Audio Downloader

A powerful and user-friendly Python tool for downloading YouTube videos and audio with customizable quality options. Supports both individual videos and entire playlists.

## ✨ Features

- **Video Downloads**: Download YouTube videos in your preferred resolution
- **Audio Extraction**: Extract high-quality audio in MP3 format
- **Playlist Support**: Download entire playlists automatically
- **Quality Selection**: Choose from available resolutions and audio bitrates
- **Smart Organization**: Automatic folder creation for playlists
- **Format Conversion**: Automatic conversion to MP4 (video) and MP3 (audio)
- **Interactive CLI**: User-friendly command-line interface

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- FFmpeg (required for format conversion)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
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

### Video Downloader (`all.py`)

Download YouTube videos with selectable quality:

```bash
python all.py
```

**Features:**
- Choose from available resolutions (1080p, 720p, 480p, etc.)
- Automatic MP4 format conversion
- Playlist support with organized folders
- Custom destination folders

**Example workflow:**
1. Enter YouTube URL
2. Choose destination folder (optional)
3. Select video quality from available options
4. Download begins automatically

### Audio Downloader (`sounds.py`)

Extract audio from YouTube videos:

```bash
python sounds.py
```

**Features:**
- Multiple audio quality options (64-320 kbps)
- MP3 format output
- Playlist audio extraction
- Custom destination folders

**Example workflow:**
1. Enter YouTube URL
2. Choose destination folder (optional)
3. Select audio quality (64, 96, 128, 192, 256, 320 kbps)
4. Download begins automatically

## 📁 File Structure

```
youtube-downloader/
├── all.py              # Video downloader script
├── sounds.py           # Audio downloader script
├── downloads/          # Default video download folder
├── audio_downloads/    # Default audio download folder
└── README.md          # This file
```

## 🎛️ Configuration Options

### Video Quality Options
- **Automatic**: Best available quality
- **Custom**: Select from available resolutions
- **Format**: Automatically converted to MP4

### Audio Quality Options
- **64 kbps**: Low quality, small file size
- **96 kbps**: Basic quality
- **128 kbps**: Standard quality
- **192 kbps**: High quality (recommended)
- **256 kbps**: Very high quality
- **320 kbps**: Maximum quality

## 🔧 Advanced Usage

### Custom Download Paths

Both scripts allow you to specify custom download directories:
- Press Enter for default location
- Or specify your preferred path when prompted

### Playlist Downloads

When downloading playlists:
- **Videos**: Creates a folder named after the playlist
- **Audio**: Creates a folder for playlist audio files
- All files are organized automatically

## ⚠️ Important Notes

- **Legal Compliance**: Only download content you have permission to download
- **Copyright**: Respect YouTube's terms of service and copyright laws
- **Rate Limiting**: The tool respects YouTube's rate limits
- **FFmpeg Required**: Ensure FFmpeg is properly installed for format conversion

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
git clone https://github.com/yourusername/youtube-downloader.git
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

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: The powerful YouTube downloading library
- **[FFmpeg](https://ffmpeg.org/)**: Essential for audio/video processing
- **YouTube**: For providing the platform and content

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [GitHub Issues](https://github.com/yourusername/youtube-downloader/issues)
3. Create a new issue with detailed information

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ for the YouTube downloading community
