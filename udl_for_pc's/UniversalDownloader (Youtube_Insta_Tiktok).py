import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
from queue import Queue
import subprocess
import json
import re
import os
from pathlib import Path
from datetime import datetime
import sys

class UniversalDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Universal Video Downloader Pro By Amiiiine")
        self.root.geometry("700x700")
        self.root.resizable(True, True)
        self.root.configure(bg="#f5f6fa")
        self.root.minsize(650, 600)
        
        # Center window
        self.center_window()
        
        # Variables
        self.url_var = tk.StringVar()
        self.destination_var = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.format_var = tk.StringVar(value="video")
        self.quality_var = tk.StringVar()
        self.video_type = tk.StringVar(value="Waiting for URL...")
        self.is_downloading = False
        self.download_thread = None
        self.message_queue = Queue()
        self.is_playlist = False
        self.playlist_name = ""
        
        # Detect if running as EXE
        self.is_exe = getattr(sys, 'frozen', False)
        
        # Create interface
        self.create_widgets()
        
        # Start UI update loop
        self.process_queue()
        
        # Startup logs
        self.log_message("✅ Application started successfully", "success")
        self.log_message("ℹ️ Enter a YouTube, Instagram, or TikTok URL to begin", "info")
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 25
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#3498db", height=60)
        header_frame.pack(fill="x", pady=(0, 10))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🎬 Universal Video Downloader Pro",
            font=("Arial", 18, "bold"),
            bg="#3498db",
            fg="white"
        )
        title_label.pack(pady=12)
        
        # Main container
        main_container = tk.Frame(self.root, bg="#f5f6fa")
        main_container.pack(fill="both", expand=True, padx=20)
        
        # URL Section
        url_frame = tk.LabelFrame(
            main_container,
            text="📎 Video URL (YouTube, Instagram, TikTok)",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=15,
            pady=15
        )
        url_frame.pack(fill="x", pady=(0, 10))
        
        url_entry_frame = tk.Frame(url_frame, bg="white")
        url_entry_frame.pack(fill="x")
        
        self.url_entry = tk.Entry(
            url_entry_frame,
            textvariable=self.url_var,
            font=("Arial", 11),
            relief="solid",
            borderwidth=1
        )
        self.url_entry.pack(side="left", fill="x", expand=True, ipady=5)
        
        analyze_btn = tk.Button(
            url_entry_frame,
            text="Analyze",
            command=self.analyze_url,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            cursor="hand2"
        )
        analyze_btn.pack(side="left", padx=(10, 0))
        
        # Detected Type
        self.type_label = tk.Label(
            url_frame,
            textvariable=self.video_type,
            font=("Arial", 9),
            bg="white",
            fg="#7f8c8d"
        )
        self.type_label.pack(anchor="w", pady=(10, 0))
        
        # Format & Quality Container
        options_frame = tk.Frame(main_container, bg="#f5f6fa")
        options_frame.pack(fill="x", pady=(0, 10))
        
        # Format Section
        format_frame = tk.LabelFrame(
            options_frame,
            text="🎵 Format",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=15,
            pady=10
        )
        format_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        radio_frame = tk.Frame(format_frame, bg="white")
        radio_frame.pack(anchor="w")
        
        video_radio = tk.Radiobutton(
            radio_frame,
            text="Video",
            variable=self.format_var,
            value="video",
            font=("Arial", 10),
            bg="white",
            cursor="hand2",
            command=self.update_quality_options
        )
        video_radio.pack(side="left", padx=(0, 20))
        
        audio_radio = tk.Radiobutton(
            radio_frame,
            text="Audio (MP3)",
            variable=self.format_var,
            value="audio",
            font=("Arial", 10),
            bg="white",
            cursor="hand2",
            command=self.update_quality_options
        )
        audio_radio.pack(side="left")
        
        # Quality Section
        quality_frame = tk.LabelFrame(
            options_frame,
            text="🎯 Quality",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=15,
            pady=10
        )
        quality_frame.pack(side="left", fill="both", expand=True, padx=(5, 0))
        
        self.quality_combo = ttk.Combobox(
            quality_frame,
            textvariable=self.quality_var,
            font=("Arial", 10),
            state="readonly"
        )
        self.quality_combo.pack(fill="x")
        self.update_quality_options()
        
        # Destination Section
        dest_frame = tk.LabelFrame(
            main_container,
            text="📁 Destination Folder",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=15,
            pady=10
        )
        dest_frame.pack(fill="x", pady=(0, 10))
        
        dest_entry_frame = tk.Frame(dest_frame, bg="white")
        dest_entry_frame.pack(fill="x")
        
        dest_entry = tk.Entry(
            dest_entry_frame,
            textvariable=self.destination_var,
            font=("Arial", 10),
            relief="solid",
            borderwidth=1,
            state="readonly"
        )
        dest_entry.pack(side="left", fill="x", expand=True, ipady=4)
        
        browse_btn = tk.Button(
            dest_entry_frame,
            text="Browse",
            command=self.select_folder,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            cursor="hand2"
        )
        browse_btn.pack(side="left", padx=(10, 0))
        
        # Progress Section
        progress_frame = tk.LabelFrame(
            main_container,
            text="🔄 Progress",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=15,
            pady=10
        )
        progress_frame.pack(fill="x", pady=(0, 10))
        
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode="determinate",
            length=400
        )
        self.progress_bar.pack(fill="x", pady=(0, 5))
        
        self.progress_label = tk.Label(
            progress_frame,
            text="Ready",
            font=("Arial", 9),
            bg="white",
            fg="#7f8c8d"
        )
        self.progress_label.pack(anchor="w")
        
        # Logs Section
        log_frame = tk.LabelFrame(
            main_container,
            text="📝 Activity Log",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=15,
            pady=10
        )
        log_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            font=("Consolas", 9),
            height=8,
            relief="flat",
            bg="#f8f9fa",
            wrap="word"
        )
        self.log_text.pack(fill="both", expand=True)
        
        # Download Button
        self.download_btn = tk.Button(
            main_container,
            text="⬇️  DOWNLOAD NOW",
            command=self.start_download,
            bg="#3498db",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2"
        )
        self.download_btn.pack(pady=(0, 10))
        
        # Hover effects
        self.setup_hover_effects()
    
    def setup_hover_effects(self):
        def on_enter(e):
            e.widget['background'] = '#2980b9'
        def on_leave(e):
            e.widget['background'] = '#3498db'
        self.download_btn.bind("<Enter>", on_enter)
        self.download_btn.bind("<Leave>", on_leave)
    
    def update_quality_options(self):
        if self.format_var.get() == "video":
            qualities = [
                "Best Quality (Auto)",
                "2160p (4K)",
                "1440p (2K)",
                "1080p (Full HD)",
                "720p (HD)",
                "480p",
                "360p"
            ]
        else:
            qualities = [
                "Best (320 kbps)",
                "High (256 kbps)",
                "Medium (192 kbps)",
                "Standard (128 kbps)"
            ]
        
        self.quality_combo['values'] = qualities
        self.quality_combo.current(0)
    
    def select_folder(self):
        folder = filedialog.askdirectory(initialdir=self.destination_var.get())
        if folder:
            self.destination_var.set(folder)
            self.log_message(f"📁 Destination set to: {folder}", "info")
    
    def analyze_url(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL")
            return
        
        platform = self.detect_platform(url)
        if platform == "Unknown":
            messagebox.showerror("Error", "❌ Unsupported or invalid URL")
            self.log_message("❌ Unsupported URL", "error")
            return
        
        self.log_message(f"🔍 Analyzing {platform} URL...", "info")
        self.video_type.set(f"Analyzing {platform}...")
        
        # Reset playlist vars
        self.is_playlist = False
        self.playlist_name = ""
        
        thread = threading.Thread(target=self._analyze_url_thread, args=(url,))
        thread.daemon = True
        thread.start()
    
    def detect_platform(self, url):
        if any(re.match(p, url) for p in [r'.*youtube\.com/.*', r'.*youtu\.be/.*']):
            return "YouTube"
        if any(re.match(p, url) for p in [r'.*instagram\.com/.*']):
            return "Instagram"
        if any(re.match(p, url) for p in [r'.*tiktok\.com/.*']):
            return "TikTok"
        return "Unknown"

    def _analyze_url_thread(self, url):
        try:
            cmd = self._get_ytdlp_command()
            cmd.extend(['--dump-single-json', '--no-playlist', url])

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30,
                creationflags=self._get_creation_flags()
            )
            
            if result.returncode != 0:
                error_msg = result.stderr[:200] if result.stderr else "Unknown error"
                self.message_queue.put(("log", f"❌ Analysis failed: {error_msg}", "error"))
                self.message_queue.put(("type", "❌ Analysis failed"))
                return
            
            info = json.loads(result.stdout.strip())
            
            if isinstance(info, dict) and info.get('_type') == 'playlist':
                entries = info.get('entries') or []
                video_count = len(entries)
                self.message_queue.put(("log", f"✅ Playlist detected: {video_count} items", "success"))
                self.message_queue.put(("type", f"📊 Playlist ({video_count} items)"))
                self.is_playlist = True
                self.playlist_name = self._clean_filename(info.get('title') or "Playlist")
            else:
                title = info.get('title', 'Unknown Title')[:80]
                self.message_queue.put(("log", f"✅ Video detected: {title}", "success"))
                self.message_queue.put(("type", f"📊 Single Video: {title}"))
                self.is_playlist = False
        
        except Exception as e:
            self.message_queue.put(("log", f"❌ Error: {str(e)[:150]}", "error"))
            self.message_queue.put(("type", "❌ Analysis failed"))
    
    def _clean_filename(self, filename):
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename.strip()[:100]
    
    def _get_ytdlp_command(self):
        if self.is_exe:
            exe_dir = os.path.dirname(sys.executable)
            ytdlp_path = os.path.join(exe_dir, 'yt-dlp.exe')
            return [ytdlp_path] if os.path.exists(ytdlp_path) else ['yt-dlp']
        return [sys.executable, '-m', 'yt_dlp']
    
    def _get_creation_flags(self):
        return subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
    
    def start_download(self):
        if self.is_downloading:
            messagebox.showwarning("Warning", "A download is already in progress")
            return
        
        url = self.url_var.get().strip()
        if not url or self.detect_platform(url) == "Unknown":
            messagebox.showerror("Error", "Please enter a valid URL")
            return
        
        destination = self.destination_var.get()
        if self.is_playlist and self.playlist_name:
            destination = os.path.join(destination, self.playlist_name)
        
        os.makedirs(destination, exist_ok=True)
        
        self.is_downloading = True
        self.download_btn.config(state="disabled", text="Downloading...")
        self.progress_bar['value'] = 0
        self.progress_label.config(text="Starting...")
        
        threading.Thread(target=self._download_thread, args=(url, destination), daemon=True).start()
    
    def _download_thread(self, url, destination):
        try:
            format_type = self.format_var.get()
            quality = self.quality_var.get()
            cmd = self._get_ytdlp_command()
            
            # Common options
            cmd.extend(['--add-metadata', '--embed-thumbnail', '--newline', '--progress'])
            
            if self.is_playlist:
                output_template = os.path.join(destination, '%(playlist_index)02d - %(title)s.%(ext)s')
                cmd.append('--yes-playlist')
            else:
                output_template = os.path.join(destination, '%(title)s.%(ext)s')
                cmd.append('--no-playlist')
            
            cmd.extend(['-o', output_template])

            if format_type == "video":
                if "2160p" in quality: f = 'bestvideo[height<=2160]+bestaudio/best'
                elif "1440p" in quality: f = 'bestvideo[height<=1440]+bestaudio/best'
                elif "1080p" in quality: f = 'bestvideo[height<=1080]+bestaudio/best'
                elif "720p" in quality: f = 'bestvideo[height<=720]+bestaudio/best'
                else: f = 'bestvideo+bestaudio/best'
                cmd.extend(['-f', f, '--merge-output-format', 'mp4'])
            else:
                cmd.extend(['-x', '--audio-format', 'mp3'])
                if "320" in quality: cmd.extend(['--audio-quality', '0'])
                elif "256" in quality: cmd.extend(['--audio-quality', '256k'])
                else: cmd.extend(['--audio-quality', '128k'])
            
            cmd.append(url)
            
            self.message_queue.put(("log", f"🚀 Starting download to: {destination}", "info"))
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                creationflags=self._get_creation_flags(),
                universal_newlines=True
            )
            
            for line in process.stdout:
                line = line.strip()
                if not line: continue
                
                # Parse progress
                if '[download]' in line and '%' in line:
                    try:
                        match = re.search(r'(\d+\.?\d*)%', line)
                        if match:
                            percent = float(match.group(1))
                            self.message_queue.put(("progress", percent, f"Downloading: {percent}%"))
                    except: pass
                elif '[ExtractAudio]' in line:
                    self.message_queue.put(("progress", 95, "Converting to MP3..."))
                elif '[VideoConvertor]' in line:
                    self.message_queue.put(("progress", 98, "Merging video/audio..."))

            process.wait()
            success = process.returncode == 0
            self.message_queue.put(("complete", success))
            
        except Exception as e:
            self.message_queue.put(("log", f"❌ Error: {str(e)}", "error"))
            self.message_queue.put(("complete", False))

    def process_queue(self):
        try:
            while True:
                msg = self.message_queue.get_nowait()
                if msg[0] == "log": self.log_message(msg[1], msg[2])
                elif msg[0] == "type": self.video_type.set(msg[1])
                elif msg[0] == "progress":
                    self.progress_bar['value'] = msg[1]
                    self.progress_label.config(text=msg[2])
                elif msg[0] == "complete":
                    self.is_downloading = False
                    self.download_btn.config(state="normal", text="⬇️  DOWNLOAD NOW")
                    if msg[1]:
                        self.progress_bar['value'] = 100
                        self.progress_label.config(text="✅ Finished!")
                        self.log_message("✅ Download completed successfully!", "success")
                    else:
                        self.log_message("❌ Download failed", "error")
                        self.progress_label.config(text="❌ Failed")
        except: pass
        self.root.after(100, self.process_queue)

    def log_message(self, message, msg_type="info"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        colors = {"info": "#2c3e50", "success": "#27ae60", "warning": "#f39c12", "error": "#e74c3c"}
        for tag, color in colors.items(): self.log_text.tag_config(tag, foreground=color)
        self.log_text.insert("end", f"[{timestamp}] ", "info")
        self.log_text.insert("end", f"{message}\n", msg_type)
        self.log_text.see("end")

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversalDownloaderApp(root)
    root.mainloop()
