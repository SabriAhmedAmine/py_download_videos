# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox, scrolledtext
# import threading
# from queue import Queue
# import subprocess
# import json
# import re
# import os
# from pathlib import Path
# from datetime import datetime
# import sys


# class YouTubeDownloaderApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("🎬 YouTube Downloader Pro By the One and Only Amiiiine")
#         self.root.geometry("650x650")
#         self.root.resizable(True, True)
#         self.root.configure(bg="#f5f6fa")
#         self.root.minsize(650, 500)
        
#         # Centrer la fenêtre
#         self.center_window()
        
#         # Variables
#         self.url_var = tk.StringVar()
#         self.destination_var = tk.StringVar(value=str(Path.home() / "Downloads"))
#         self.format_var = tk.StringVar(value="video")
#         self.quality_var = tk.StringVar()
#         self.video_type = tk.StringVar(value="Analyse en cours...")
#         self.is_downloading = False
#         self.download_thread = None
#         self.message_queue = Queue()
#         self.is_playlist = False
#         self.playlist_name = ""
        
#         # Détecter si on est en mode EXE
#         self.is_exe = getattr(sys, 'frozen', False)
        
#         # Créer l'interface
#         self.create_widgets()
        
#         # Démarrer la mise à jour de l'interface
#         self.process_queue()
        
#         # Log de démarrage
#         self.log_message("✅ Application démarrée avec succès", "success")
#         self.log_message("ℹ️ Entrez une URL YouTube pour commencer", "info")
    
#     def center_window(self):
#         self.root.update_idletasks()
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.root.winfo_screenheight() // 2) - (height // 2) - 25
#         self.root.geometry(f'{width}x{height}+{x}+{y}')
    
#     def create_widgets(self):
#         # En-tête
#         header_frame = tk.Frame(self.root, bg="#3498db", height=50)
#         header_frame.pack(fill="x", pady=(0, 10))
#         header_frame.pack_propagate(False)
        
#         title_label = tk.Label(
#             header_frame,
#             text="🎬 YouTube Downloader Pro",
#             font=("Arial", 16, "bold"),
#             bg="#3498db",
#             fg="white"
#         )
#         title_label.pack(pady=12)
        
#         # Conteneur principal
#         main_container = tk.Frame(self.root, bg="#f5f6fa")
#         main_container.pack(fill="both", expand=True, padx=15)
        
#         # Section URL
#         url_frame = tk.LabelFrame(
#             main_container,
#             text="📎 URL YouTube",
#             font=("Arial", 9, "bold"),
#             bg="white",
#             fg="#2c3e50",
#             relief="flat",
#             padx=10,
#             pady=10
#         )
#         url_frame.pack(fill="x", pady=(0, 8))
        
#         url_entry_frame = tk.Frame(url_frame, bg="white")
#         url_entry_frame.pack(fill="x")
        
#         self.url_entry = tk.Entry(
#             url_entry_frame,
#             textvariable=self.url_var,
#             font=("Arial", 10),
#             relief="solid",
#             borderwidth=1
#         )
#         self.url_entry.pack(side="left", fill="x", expand=True, ipady=3)
        
#         analyze_btn = tk.Button(
#             url_entry_frame,
#             text="Analyser",
#             command=self.analyze_url,
#             bg="#3498db",
#             fg="white",
#             font=("Arial", 9, "bold"),
#             relief="flat",
#             padx=12,
#             cursor="hand2"
#         )
#         analyze_btn.pack(side="left", padx=(8, 0))
        
#         # Type détecté
#         self.type_label = tk.Label(
#             url_frame,
#             textvariable=self.video_type,
#             font=("Arial", 8),
#             bg="white",
#             fg="#7f8c8d"
#         )
#         self.type_label.pack(anchor="w", pady=(8, 0))
        
#         # Section Format
#         format_frame = tk.LabelFrame(
#             main_container,
#             text="🎵 Format",
#             font=("Arial", 9, "bold"),
#             bg="white",
#             fg="#2c3e50",
#             relief="flat",
#             padx=10,
#             pady=8
#         )
#         format_frame.pack(fill="x", pady=(0, 8))
        
#         radio_frame = tk.Frame(format_frame, bg="white")
#         radio_frame.pack(anchor="w")
        
#         video_radio = tk.Radiobutton(
#             radio_frame,
#             text="Vidéo",
#             variable=self.format_var,
#             value="video",
#             font=("Arial", 9),
#             bg="white",
#             cursor="hand2",
#             command=self.update_quality_options
#         )
#         video_radio.pack(side="left", padx=(0, 15))
        
#         audio_radio = tk.Radiobutton(
#             radio_frame,
#             text="Audio",
#             variable=self.format_var,
#             value="audio",
#             font=("Arial", 9),
#             bg="white",
#             cursor="hand2",
#             command=self.update_quality_options
#         )
#         audio_radio.pack(side="left")
        
#         # Section Qualité
#         quality_frame = tk.LabelFrame(
#             main_container,
#             text="🎯 Qualité",
#             font=("Arial", 9, "bold"),
#             bg="white",
#             fg="#2c3e50",
#             relief="flat",
#             padx=10,
#             pady=8
#         )
#         quality_frame.pack(fill="x", pady=(0, 8))
        
#         self.quality_combo = ttk.Combobox(
#             quality_frame,
#             textvariable=self.quality_var,
#             font=("Arial", 9),
#             state="readonly",
#             width=50
#         )
#         self.quality_combo.pack(fill="x")
#         self.update_quality_options()
        
#         # Section Destination
#         dest_frame = tk.LabelFrame(
#             main_container,
#             text="📁 Destination",
#             font=("Arial", 9, "bold"),
#             bg="white",
#             fg="#2c3e50",
#             relief="flat",
#             padx=10,
#             pady=8
#         )
#         dest_frame.pack(fill="x", pady=(0, 8))
        
#         dest_entry_frame = tk.Frame(dest_frame, bg="white")
#         dest_entry_frame.pack(fill="x")
        
#         dest_entry = tk.Entry(
#             dest_entry_frame,
#             textvariable=self.destination_var,
#             font=("Arial", 9),
#             relief="solid",
#             borderwidth=1,
#             state="readonly"
#         )
#         dest_entry.pack(side="left", fill="x", expand=True, ipady=3)
        
#         browse_btn = tk.Button(
#             dest_entry_frame,
#             text="Parcourir",
#             command=self.select_folder,
#             bg="#95a5a6",
#             fg="white",
#             font=("Arial", 9, "bold"),
#             relief="flat",
#             padx=12,
#             cursor="hand2"
#         )
#         browse_btn.pack(side="left", padx=(8, 0))
        
#         # Section Progression
#         progress_frame = tk.LabelFrame(
#             main_container,
#             text="🔄 Progression",
#             font=("Arial", 9, "bold"),
#             bg="white",
#             fg="#2c3e50",
#             relief="flat",
#             padx=10,
#             pady=8
#         )
#         progress_frame.pack(fill="x", pady=(0, 8))
        
#         self.progress_bar = ttk.Progressbar(
#             progress_frame,
#             mode="determinate",
#             length=400
#         )
#         self.progress_bar.pack(fill="x", pady=(0, 5))
        
#         self.progress_label = tk.Label(
#             progress_frame,
#             text="En attente...",
#             font=("Arial", 8),
#             bg="white",
#             fg="#7f8c8d"
#         )
#         self.progress_label.pack(anchor="w")
        
#         # Section Logs
#         log_frame = tk.LabelFrame(
#             main_container,
#             text="📝 Journal",
#             font=("Arial", 9, "bold"),
#             bg="white",
#             fg="#2c3e50",
#             relief="flat",
#             padx=10,
#             pady=8
#         )
#         log_frame.pack(fill="both", expand=True, pady=(0, 8))
        
#         self.log_text = scrolledtext.ScrolledText(
#             log_frame,
#             font=("Consolas", 8),
#             height=6,
#             relief="flat",
#             bg="#f8f9fa",
#             wrap="word"
#         )
#         self.log_text.pack(fill="both", expand=True)
        
#         # Bouton de téléchargement
#         self.download_btn = tk.Button(
#             main_container,
#             text="⬇️  TÉLÉCHARGER",
#             command=self.start_download,
#             bg="#3498db",
#             fg="white",
#             font=("Arial", 11, "bold"),
#             relief="flat",
#             padx=20,
#             pady=10,
#             cursor="hand2"
#         )
#         self.download_btn.pack(pady=(0, 8))
        
#         # Effets hover sur les boutons
#         self.setup_hover_effects()
    
#     def setup_hover_effects(self):
#         """Configurer les effets de survol"""
#         def on_enter(e):
#             e.widget['background'] = '#2980b9'
        
#         def on_leave(e):
#             e.widget['background'] = '#3498db'
        
#         self.download_btn.bind("<Enter>", on_enter)
#         self.download_btn.bind("<Leave>", on_leave)
    
#     def update_quality_options(self):
#         """Mettre à jour les options de qualité selon le format"""
#         if self.format_var.get() == "video":
#             qualities = [
#                 "Meilleure qualité (automatique)",
#                 "2160p (4K)",
#                 "1440p (2K)",
#                 "1080p (Full HD)",
#                 "720p (HD)",
#                 "480p",
#                 "360p"
#             ]
#         else:
#             qualities = [
#                 "Meilleure qualité (320 kbps)",
#                 "Haute qualité (256 kbps)",
#                 "Qualité moyenne (192 kbps)",
#                 "Qualité standard (128 kbps)"
#             ]
        
#         self.quality_combo['values'] = qualities
#         self.quality_combo.current(0)
    
#     def select_folder(self):
#         """Sélectionner le dossier de destination"""
#         folder = filedialog.askdirectory(initialdir=self.destination_var.get())
#         if folder:
#             self.destination_var.set(folder)
#             self.log_message(f"📁 Dossier sélectionné : {folder}", "info")
    
#     def analyze_url(self):
#         """Analyser l'URL YouTube"""
#         url = self.url_var.get().strip()
        
#         if not url:
#             messagebox.showwarning("Attention", "Veuillez entrer une URL YouTube")
#             return
        
#         if not self.is_valid_youtube_url(url):
#             messagebox.showerror("Erreur", "❌ URL YouTube invalide")
#             self.log_message("❌ URL invalide", "error")
#             return
        
#         self.log_message("🔍 Analyse de l'URL...", "info")
        
#         # Réinitialiser les variables de playlist
#         self.is_playlist = False
#         self.playlist_name = ""
        
#         # Analyser en arrière-plan
#         thread = threading.Thread(target=self._analyze_url_thread, args=(url,))
#         thread.daemon = True
#         thread.start()
    
#     def _analyze_url_thread(self, url):
#         """Thread d'analyse de l'URL"""
#         try:
#             # Préparer la commande yt-dlp
#             cmd = self._get_ytdlp_command()
#             cmd.extend(['--dump-json', '--flat-playlist', url])
            
#             # Exécuter la commande
#             result = subprocess.run(
#                 cmd, 
#                 capture_output=True, 
#                 text=True, 
#                 timeout=30,
#                 creationflags=self._get_creation_flags()
#             )
            
#             if result.returncode != 0:
#                 error_msg = result.stderr[:200] if result.stderr else "Erreur inconnue"
#                 self.message_queue.put(("log", f"❌ Impossible d'analyser l'URL: {error_msg}", "error"))
#                 self.message_queue.put(("type", "❌ Analyse échouée"))
#                 return
            
#             # Parser les résultats
#             lines = result.stdout.strip().split('\n')
#             if not lines or lines[0] == '':
#                 self.message_queue.put(("log", "❌ Aucune donnée reçue", "error"))
#                 self.message_queue.put(("type", "❌ Analyse échouée"))
#                 return
            
#             if len(lines) > 1:
#                 # Playlist détectée
#                 video_count = len(lines)
#                 self.message_queue.put(("log", f"✅ Playlist détectée : {video_count} vidéos", "success"))
#                 self.message_queue.put(("type", f"📊 Playlist ({video_count} vidéos)"))
#                 self.is_playlist = True
                
#                 # Récupérer le nom de la playlist (premier élément)
#                 try:
#                     first_video = json.loads(lines[0])
#                     self.playlist_name = first_video.get('playlist', 'Playlist YouTube')
#                     # Nettoyer le nom pour le système de fichiers
#                     self.playlist_name = self._clean_filename(self.playlist_name)
#                 except:
#                     self.playlist_name = "Playlist_YouTube"
                
#             else:
#                 # Vidéo unique
#                 try:
#                     info = json.loads(lines[0])
#                     title = info.get('title', 'Titre inconnu')[:80]
#                     self.message_queue.put(("log", f"✅ Vidéo détectée : {title}", "success"))
#                     self.message_queue.put(("type", "📊 Vidéo unique"))
#                     self.is_playlist = False
#                 except json.JSONDecodeError:
#                     self.message_queue.put(("log", "✅ Contenu YouTube détecté", "success"))
#                     self.message_queue.put(("type", "📊 Contenu YouTube"))
#                     self.is_playlist = False
        
#         except subprocess.TimeoutExpired:
#             self.message_queue.put(("log", "⏱️ Délai d'analyse dépassé", "error"))
#             self.message_queue.put(("type", "❌ Analyse échouée"))
#         except Exception as e:
#             self.message_queue.put(("log", f"❌ Erreur: {str(e)[:150]}", "error"))
#             self.message_queue.put(("type", "❌ Analyse échouée"))
    
#     def _clean_filename(self, filename):
#         """Nettoyer le nom de fichier pour le système de fichiers"""
#         # Remplace les caractères non valides
#         invalid_chars = '<>:"/\\|?*'
#         for char in invalid_chars:
#             filename = filename.replace(char, '_')
        
#         # Retire les espaces en début/fin et limite la longueur
#         filename = filename.strip()
#         if len(filename) > 100:
#             filename = filename[:100]
        
#         return filename
    
#     def is_valid_youtube_url(self, url):
#         """Vérifier si l'URL est valide"""
#         patterns = [
#             r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+',
#             r'(https?://)?(www\.)?youtube\.com/watch\?v=.+',
#             r'(https?://)?(www\.)?youtube\.com/playlist\?list=.+',
#             r'(https?://)?(www\.)?youtu\.be/.+',
#             r'(https?://)?(www\.)?youtube\.com/shorts/.+'
#         ]
#         return any(re.match(pattern, url) for pattern in patterns)
    
#     def _get_ytdlp_command(self):
#         """Obtenir la commande yt-dlp selon le mode"""
#         if self.is_exe:
#             # Mode EXE: chercher yt-dlp.exe
#             exe_dir = os.path.dirname(sys.executable)
#             ytdlp_path = os.path.join(exe_dir, 'yt-dlp.exe')
            
#             if os.path.exists(ytdlp_path):
#                 return [ytdlp_path]
#             else:
#                 # Essayer dans le PATH
#                 return ['yt-dlp']
#         else:
#             # Mode script: utiliser le module Python
#             return [sys.executable, '-m', 'yt_dlp']
    
#     def _get_creation_flags(self):
#         """Obtenir les flags de création de processus"""
#         if os.name == 'nt':
#             return subprocess.CREATE_NO_WINDOW
#         return 0
    
#     def start_download(self):
#         """Démarrer le téléchargement"""
#         if self.is_downloading:
#             messagebox.showwarning("Attention", "Un téléchargement est déjà en cours")
#             return
        
#         url = self.url_var.get().strip()
#         if not url:
#             messagebox.showwarning("Attention", "Veuillez entrer une URL YouTube")
#             return
        
#         if not self.is_valid_youtube_url(url):
#             messagebox.showerror("Erreur", "URL YouTube invalide")
#             return
        
#         destination = self.destination_var.get()
        
#         # Si c'est une playlist, créer un sous-dossier
#         if self.is_playlist and self.playlist_name:
#             playlist_folder = os.path.join(destination, self.playlist_name)
#             destination = playlist_folder
        
#         if not os.path.exists(destination):
#             try:
#                 os.makedirs(destination, exist_ok=True)
#                 if self.is_playlist:
#                     self.log_message(f"📁 Dossier créé pour la playlist : {destination}", "info")
#             except Exception as e:
#                 messagebox.showerror("Erreur", f"Impossible de créer le dossier: {destination}\n{str(e)}")
#                 return
        
#         # Vérifier les permissions
#         if not os.access(destination, os.W_OK):
#             messagebox.showerror("Erreur", "🚫 Impossible d'écrire dans ce dossier")
#             return
        
#         self.is_downloading = True
#         self.download_btn.config(state="disabled", text="Téléchargement en cours...")
#         self.progress_bar['value'] = 0
#         self.progress_label.config(text="Démarrage du téléchargement...")
        
#         # Démarrer le téléchargement dans un thread
#         self.download_thread = threading.Thread(
#             target=self._download_thread,
#             args=(url, destination)
#         )
#         self.download_thread.daemon = True
#         self.download_thread.start()
    
#     def _download_thread(self, url, destination):
#         """Thread de téléchargement"""
#         try:
#             format_type = self.format_var.get()
#             quality = self.quality_var.get()
            
#             # Construire la commande yt-dlp
#             cmd = self._get_ytdlp_command()
            
#             # Structure du nom de fichier pour les playlists
#             if self.is_playlist:
#                 output_template = os.path.join(destination, '%(playlist_index)02d - %(title)s.%(ext)s')
#             else:
#                 output_template = os.path.join(destination, '%(title)s.%(ext)s')
            
#             if format_type == "video":
#                 # Appliquer la qualité sélectionnée
#                 if "2160p" in quality:
#                     cmd.extend(['-f', 'bestvideo[height<=2160]+bestaudio/best[height<=2160]'])
#                 elif "1440p" in quality:
#                     cmd.extend(['-f', 'bestvideo[height<=1440]+bestaudio/best[height<=1440]'])
#                 elif "1080p" in quality:
#                     cmd.extend(['-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'])
#                 elif "720p" in quality:
#                     cmd.extend(['-f', 'bestvideo[height<=720]+bestaudio/best[height<=720]'])
#                 elif "480p" in quality:
#                     cmd.extend(['-f', 'bestvideo[height<=480]+bestaudio/best[height<=480]'])
#                 elif "360p" in quality:
#                     cmd.extend(['-f', 'bestvideo[height<=360]+bestaudio/best[height<=360]'])
#                 else:
#                     # Meilleure qualité par défaut
#                     cmd.extend(['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'])
                
#                 cmd.extend(['--merge-output-format', 'mp4'])
#             else:
#                 cmd.extend(['-x', '--audio-format', 'mp3'])
                
#                 # Appliquer la qualité audio
#                 if "320" in quality:
#                     cmd.extend(['--audio-quality', '0'])
#                 elif "256" in quality:
#                     cmd.extend(['--audio-quality', '256k'])
#                 elif "192" in quality:
#                     cmd.extend(['--audio-quality', '192k'])
#                 elif "128" in quality:
#                     cmd.extend(['--audio-quality', '128k'])
#                 else:
#                     cmd.extend(['--audio-quality', '0'])
            
#             # Options communes
#             cmd.extend([
#                 '-o', output_template,
#                 '--no-playlist' if not self.is_playlist else '--yes-playlist',
#                 '--newline',
#                 '--no-warnings',
#                 '--progress',
#                 url
#             ])
            
#             if self.is_playlist:
#                 self.message_queue.put(("log", f"📚 Playlist détectée : {self.playlist_name}", "info"))
#                 self.message_queue.put(("log", f"📁 Dossier de la playlist : {destination}", "info"))
#             else:
#                 self.message_queue.put(("log", "🚀 Téléchargement démarré...", "info"))
#                 self.message_queue.put(("log", f"📁 Destination : {destination}", "info"))
            
#             # Exécuter yt-dlp
#             process = subprocess.Popen(
#                 cmd,
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.STDOUT,
#                 text=True,
#                 bufsize=1,
#                 creationflags=self._get_creation_flags(),
#                 universal_newlines=True
#             )
            
#             # Variables pour suivre la progression
#             total_videos = 0
#             current_video = 0
            
#             # Lire la sortie en temps réel
#             for line in process.stdout:
#                 line = line.strip()
#                 if line:
#                     # Détecter le nombre total de vidéos dans une playlist
#                     if '[playlist]' in line and 'Downloading' in line:
#                         match = re.search(r'Downloading (\d+) items', line)
#                         if match:
#                             total_videos = int(match.group(1))
#                             self.message_queue.put(("log", f"📊 Nombre total de vidéos : {total_videos}", "info"))
                    
#                     # Détecter quand une nouvelle vidéo commence
#                     if '[download]' in line and 'Downloading item' in line:
#                         match = re.search(r'Downloading item (\d+) of', line)
#                         if match:
#                             current_video = int(match.group(1))
#                             if total_videos > 0:
#                                 self.message_queue.put(("log", f"🎬 Téléchargement de la vidéo {current_video}/{total_videos}", "info"))
                    
#                     # Parser la progression
#                     if '[download]' in line and '%' in line:
#                         # Extraire le pourcentage
#                         match = re.search(r'(\d+\.?\d*)%', line)
#                         if match:
#                             percent = float(match.group(1))
#                             # Calculer la progression globale pour les playlists
#                             if total_videos > 0 and current_video > 0:
#                                 # Progression de la vidéo actuelle
#                                 video_progress = percent / 100
#                                 # Progression globale
#                                 overall_progress = ((current_video - 1) + video_progress) / total_videos * 100
#                                 progress_text = f"Playlist: {current_video}/{total_videos} ({percent:.1f}%) - {line}"
#                                 self.message_queue.put(("progress", overall_progress, progress_text))
#                             else:
#                                 self.message_queue.put(("progress", percent, line))
                    
#                     # N'afficher que les messages importants
#                     if any(keyword in line.lower() for keyword in ['download', 'merging', 'destination', 'error', 'warning', 'extract']):
#                         if not line.startswith('[youtube]') or 'error' in line.lower():
#                             self.message_queue.put(("log", line, "info"))
            
#             process.wait()
            
#             if process.returncode == 0:
#                 if self.is_playlist:
#                     self.message_queue.put(("log", f"✅ Playlist téléchargée avec succès! ({total_videos} vidéos)", "success"))
#                     self.message_queue.put(("log", f"📁 Tous les fichiers sont dans : {destination}", "success"))
#                 else:
#                     self.message_queue.put(("log", "✅ Téléchargement terminé avec succès!", "success"))
#                     self.message_queue.put(("log", f"📁 Fichier enregistré dans : {destination}", "success"))
#                 self.message_queue.put(("complete", True))
#             else:
#                 self.message_queue.put(("log", "❌ Échec du téléchargement", "error"))
#                 self.message_queue.put(("log", f"Code d'erreur: {process.returncode}", "error"))
#                 self.message_queue.put(("complete", False))
        
#         except FileNotFoundError:
#             error_msg = "yt-dlp n'est pas trouvé. "
#             if self.is_exe:
#                 error_msg += "Placez yt-dlp.exe dans le même dossier que l'application."
#             else:
#                 error_msg += "Installez-le avec: pip install yt-dlp"
            
#             self.message_queue.put(("log", f"❌ {error_msg}", "error"))
#             self.message_queue.put(("complete", False))
#         except Exception as e:
#             self.message_queue.put(("log", f"❌ Erreur lors du téléchargement: {str(e)[:200]}", "error"))
#             self.message_queue.put(("complete", False))
    
#     def process_queue(self):
#         """Traiter la file de messages"""
#         try:
#             while True:
#                 message = self.message_queue.get_nowait()
                
#                 if message[0] == "log":
#                     self.log_message(message[1], message[2])
#                 elif message[0] == "type":
#                     self.video_type.set(message[1])
#                 elif message[0] == "progress":
#                     self.progress_bar['value'] = message[1]
#                     self.progress_label.config(text=message[2])
#                 elif message[0] == "complete":
#                     self.is_downloading = False
#                     self.download_btn.config(state="normal", text="⬇️  TÉLÉCHARGER")
#                     self.progress_bar['value'] = 100 if message[1] else 0
#                     if message[1]:
#                         self.progress_label.config(text="✅ Téléchargement terminé!")
#                         if self.is_playlist:
#                             self.log_message("✅ Téléchargement de la playlist terminé!", "success")
#                         else:
#                             self.log_message("✅ Téléchargement terminé avec succès!", "success")
#                     else:
#                         self.progress_label.config(text="❌ Échec du téléchargement")
#                         self.log_message("❌ Le téléchargement a échoué", "error")
#         except:
#             pass
        
#         self.root.after(100, self.process_queue)
    
#     def log_message(self, message, msg_type="info"):
#         """Ajouter un message au journal"""
#         timestamp = datetime.now().strftime("%H:%M:%S")
        
#         # Couleurs selon le type
#         colors = {
#             "info": "#2c3e50",
#             "success": "#27ae60",
#             "warning": "#f39c12",
#             "error": "#e74c3c"
#         }
        
#         # Configurer les tags
#         for tag, color in colors.items():
#             self.log_text.tag_config(tag, foreground=color)
        
#         # Ajouter le message
#         self.log_text.insert("end", f"[{timestamp}] ", "info")
#         self.log_text.insert("end", f"{message}\n", msg_type)
#         self.log_text.see("end")


# def main():
#     root = tk.Tk()
#     app = YouTubeDownloaderApp(root)
#     root.mainloop()


# if __name__ == "__main__":
#     main()



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


class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 YouTube Downloader Pro By the One and Only Amiiiine")
        self.root.geometry("650x650")
        self.root.resizable(True, True)
        self.root.configure(bg="#f5f6fa")
        self.root.minsize(650, 500)
        
        # Centrer la fenêtre
        self.center_window()
        
        # Variables
        self.url_var = tk.StringVar()
        self.destination_var = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.format_var = tk.StringVar(value="video")
        self.quality_var = tk.StringVar()
        self.video_type = tk.StringVar(value="Analyse en cours...")
        self.is_downloading = False
        self.download_thread = None
        self.message_queue = Queue()
        self.is_playlist = False
        self.playlist_name = ""
        
        # Détecter si on est en mode EXE
        self.is_exe = getattr(sys, 'frozen', False)
        
        # Créer l'interface
        self.create_widgets()
        
        # Démarrer la mise à jour de l'interface
        self.process_queue()
        
        # Log de démarrage
        self.log_message("✅ Application démarrée avec succès", "success")
        self.log_message("ℹ️ Entrez une URL YouTube pour commencer", "info")
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 25
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # En-tête
        header_frame = tk.Frame(self.root, bg="#3498db", height=50)
        header_frame.pack(fill="x", pady=(0, 10))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🎬 YouTube Downloader Pro",
            font=("Arial", 16, "bold"),
            bg="#3498db",
            fg="white"
        )
        title_label.pack(pady=12)
        
        # Conteneur principal
        main_container = tk.Frame(self.root, bg="#f5f6fa")
        main_container.pack(fill="both", expand=True, padx=15)
        
        # Section URL
        url_frame = tk.LabelFrame(
            main_container,
            text="📎 URL YouTube",
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=10,
            pady=10
        )
        url_frame.pack(fill="x", pady=(0, 8))
        
        url_entry_frame = tk.Frame(url_frame, bg="white")
        url_entry_frame.pack(fill="x")
        
        self.url_entry = tk.Entry(
            url_entry_frame,
            textvariable=self.url_var,
            font=("Arial", 10),
            relief="solid",
            borderwidth=1
        )
        self.url_entry.pack(side="left", fill="x", expand=True, ipady=3)
        
        analyze_btn = tk.Button(
            url_entry_frame,
            text="Analyser",
            command=self.analyze_url,
            bg="#3498db",
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            padx=12,
            cursor="hand2"
        )
        analyze_btn.pack(side="left", padx=(8, 0))
        
        # Type détecté
        self.type_label = tk.Label(
            url_frame,
            textvariable=self.video_type,
            font=("Arial", 8),
            bg="white",
            fg="#7f8c8d"
        )
        self.type_label.pack(anchor="w", pady=(8, 0))
        
        # Section Format
        format_frame = tk.LabelFrame(
            main_container,
            text="🎵 Format",
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=10,
            pady=8
        )
        format_frame.pack(fill="x", pady=(0, 8))
        
        radio_frame = tk.Frame(format_frame, bg="white")
        radio_frame.pack(anchor="w")
        
        video_radio = tk.Radiobutton(
            radio_frame,
            text="Vidéo",
            variable=self.format_var,
            value="video",
            font=("Arial", 9),
            bg="white",
            cursor="hand2",
            command=self.update_quality_options
        )
        video_radio.pack(side="left", padx=(0, 15))
        
        audio_radio = tk.Radiobutton(
            radio_frame,
            text="Audio",
            variable=self.format_var,
            value="audio",
            font=("Arial", 9),
            bg="white",
            cursor="hand2",
            command=self.update_quality_options
        )
        audio_radio.pack(side="left")
        
        # Section Qualité
        quality_frame = tk.LabelFrame(
            main_container,
            text="🎯 Qualité",
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=10,
            pady=8
        )
        quality_frame.pack(fill="x", pady=(0, 8))
        
        self.quality_combo = ttk.Combobox(
            quality_frame,
            textvariable=self.quality_var,
            font=("Arial", 9),
            state="readonly",
            width=50
        )
        self.quality_combo.pack(fill="x")
        self.update_quality_options()
        
        # Section Destination
        dest_frame = tk.LabelFrame(
            main_container,
            text="📁 Destination",
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=10,
            pady=8
        )
        dest_frame.pack(fill="x", pady=(0, 8))
        
        dest_entry_frame = tk.Frame(dest_frame, bg="white")
        dest_entry_frame.pack(fill="x")
        
        dest_entry = tk.Entry(
            dest_entry_frame,
            textvariable=self.destination_var,
            font=("Arial", 9),
            relief="solid",
            borderwidth=1,
            state="readonly"
        )
        dest_entry.pack(side="left", fill="x", expand=True, ipady=3)
        
        browse_btn = tk.Button(
            dest_entry_frame,
            text="Parcourir",
            command=self.select_folder,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            padx=12,
            cursor="hand2"
        )
        browse_btn.pack(side="left", padx=(8, 0))
        
        # Section Progression
        progress_frame = tk.LabelFrame(
            main_container,
            text="🔄 Progression",
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=10,
            pady=8
        )
        progress_frame.pack(fill="x", pady=(0, 8))
        
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode="determinate",
            length=400
        )
        self.progress_bar.pack(fill="x", pady=(0, 5))
        
        self.progress_label = tk.Label(
            progress_frame,
            text="En attente...",
            font=("Arial", 8),
            bg="white",
            fg="#7f8c8d"
        )
        self.progress_label.pack(anchor="w")
        
        # Section Logs
        log_frame = tk.LabelFrame(
            main_container,
            text="📝 Journal",
            font=("Arial", 9, "bold"),
            bg="white",
            fg="#2c3e50",
            relief="flat",
            padx=10,
            pady=8
        )
        log_frame.pack(fill="both", expand=True, pady=(0, 8))
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            font=("Consolas", 8),
            height=6,
            relief="flat",
            bg="#f8f9fa",
            wrap="word"
        )
        self.log_text.pack(fill="both", expand=True)
        
        # Bouton de téléchargement
        self.download_btn = tk.Button(
            main_container,
            text="⬇️  TÉLÉCHARGER",
            command=self.start_download,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.download_btn.pack(pady=(0, 8))
        
        # Effets hover sur les boutons
        self.setup_hover_effects()
    
    def setup_hover_effects(self):
        """Configurer les effets de survol"""
        def on_enter(e):
            e.widget['background'] = '#2980b9'
        
        def on_leave(e):
            e.widget['background'] = '#3498db'
        
        self.download_btn.bind("<Enter>", on_enter)
        self.download_btn.bind("<Leave>", on_leave)
    
    def update_quality_options(self):
        """Mettre à jour les options de qualité selon le format"""
        if self.format_var.get() == "video":
            qualities = [
                "Meilleure qualité (automatique)",
                "2160p (4K)",
                "1440p (2K)",
                "1080p (Full HD)",
                "720p (HD)",
                "480p",
                "360p"
            ]
        else:
            qualities = [
                "Meilleure qualité (320 kbps)",
                "Haute qualité (256 kbps)",
                "Qualité moyenne (192 kbps)",
                "Qualité standard (128 kbps)"
            ]
        
        self.quality_combo['values'] = qualities
        self.quality_combo.current(0)
    
    def select_folder(self):
        """Sélectionner le dossier de destination"""
        folder = filedialog.askdirectory(initialdir=self.destination_var.get())
        if folder:
            self.destination_var.set(folder)
            self.log_message(f"📁 Dossier sélectionné : {folder}", "info")
    
    def analyze_url(self):
        """Analyser l'URL YouTube"""
        url = self.url_var.get().strip()
        
        if not url:
            messagebox.showwarning("Attention", "Veuillez entrer une URL YouTube")
            return
        
        if not self.is_valid_youtube_url(url):
            messagebox.showerror("Erreur", "❌ URL YouTube invalide")
            self.log_message("❌ URL invalide", "error")
            return
        
        self.log_message("🔍 Analyse de l'URL...", "info")
        
        # Réinitialiser les variables de playlist
        self.is_playlist = False
        self.playlist_name = ""
        
        # Analyser en arrière-plan
        thread = threading.Thread(target=self._analyze_url_thread, args=(url,))
        thread.daemon = True
        thread.start()
    
    def _analyze_url_thread(self, url):
        """Thread d'analyse de l'URL"""
        try:
            # Préparer la commande yt-dlp
            # Use --dump-single-json to get playlist metadata (title, entries) when URL is a playlist
            cmd = self._get_ytdlp_command()
            cmd.extend(['--dump-single-json', url])

            # Exécuter la commande
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30,
                creationflags=self._get_creation_flags()
            )
            
            if result.returncode != 0:
                error_msg = result.stderr[:200] if result.stderr else "Erreur inconnue"
                self.message_queue.put(("log", f"❌ Impossible d'analyser l'URL: {error_msg}", "error"))
                self.message_queue.put(("type", "❌ Analyse échouée"))
                return
            
            # Parser le JSON (single object for video or playlist)
            text = result.stdout.strip()
            if not text:
                self.message_queue.put(("log", "❌ Aucune donnée reçue", "error"))
                self.message_queue.put(("type", "❌ Analyse échouée"))
                return

            try:
                info = json.loads(text)
            except json.JSONDecodeError:
                # Fallback: couldn't parse JSON
                self.message_queue.put(("log", "❌ Impossible de parser les données JSON", "error"))
                self.message_queue.put(("type", "❌ Analyse échouée"))
                return

            # Si c'est une playlist, yt-dlp renvoie un objet avec "_type": "playlist" et une clé "entries"
            if isinstance(info, dict) and info.get('_type') == 'playlist':
                entries = info.get('entries') or []
                video_count = len(entries)
                self.message_queue.put(("log", f"✅ Playlist détectée : {video_count} vidéos", "success"))
                self.message_queue.put(("type", f"📊 Playlist ({video_count} vidéos)"))
                self.is_playlist = True

                # Récupérer le nom de la playlist depuis les métadonnées
                self.playlist_name = info.get('title') or info.get('playlist') or "Playlist_YouTube"
                self.playlist_name = self._clean_filename(self.playlist_name)
            else:
                # Vidéo unique
                title = info.get('title', 'Titre inconnu')[:80] if isinstance(info, dict) else 'Titre inconnu'
                self.message_queue.put(("log", f"✅ Vidéo détectée : {title}", "success"))
                self.message_queue.put(("type", "📊 Vidéo unique"))
                self.is_playlist = False
        
        except subprocess.TimeoutExpired:
            self.message_queue.put(("log", "⏱️ Délai d'analyse dépassé", "error"))
            self.message_queue.put(("type", "❌ Analyse échouée"))
        except Exception as e:
            self.message_queue.put(("log", f"❌ Erreur: {str(e)[:150]}", "error"))
            self.message_queue.put(("type", "❌ Analyse échouée"))
    
    def _clean_filename(self, filename):
        """Nettoyer le nom de fichier pour le système de fichiers"""
        # Remplace les caractères non valides
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        
        # Retire les espaces en début/fin et limite la longueur
        filename = filename.strip()
        if len(filename) > 100:
            filename = filename[:100]
        
        return filename
    
    def is_valid_youtube_url(self, url):
        """Vérifier si l'URL est valide"""
        patterns = [
            r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+',
            r'(https?://)?(www\.)?youtube\.com/watch\?v=.+',
            r'(https?://)?(www\.)?youtube\.com/playlist\?list=.+',
            r'(https?://)?(www\.)?youtu\.be/.+',
            r'(https?://)?(www\.)?youtube\.com/shorts/.+'
        ]
        return any(re.match(pattern, url) for pattern in patterns)
    
    def _get_ytdlp_command(self):
        """Obtenir la commande yt-dlp selon le mode"""
        if self.is_exe:
            # Mode EXE: chercher yt-dlp.exe
            exe_dir = os.path.dirname(sys.executable)
            ytdlp_path = os.path.join(exe_dir, 'yt-dlp.exe')
            
            if os.path.exists(ytdlp_path):
                return [ytdlp_path]
            else:
                # Essayer dans le PATH
                return ['yt-dlp']
        else:
            # Mode script: utiliser le module Python
            return [sys.executable, '-m', 'yt_dlp']
    
    def _get_creation_flags(self):
        """Obtenir les flags de création de processus"""
        if os.name == 'nt':
            return subprocess.CREATE_NO_WINDOW
        return 0
    
    def start_download(self):
        """Démarrer le téléchargement"""
        if self.is_downloading:
            messagebox.showwarning("Attention", "Un téléchargement est déjà en cours")
            return
        
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Attention", "Veuillez entrer une URL YouTube")
            return
        
        if not self.is_valid_youtube_url(url):
            messagebox.showerror("Erreur", "URL YouTube invalide")
            return
        
        destination = self.destination_var.get()
        
        # Si c'est une playlist, créer un sous-dossier
        if self.is_playlist and self.playlist_name:
            playlist_folder = os.path.join(destination, self.playlist_name)
            destination = playlist_folder
        
        if not os.path.exists(destination):
            try:
                os.makedirs(destination, exist_ok=True)
                if self.is_playlist:
                    self.log_message(f"📁 Dossier créé pour la playlist : {destination}", "info")
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de créer le dossier: {destination}\n{str(e)}")
                return
        
        # Vérifier les permissions
        if not os.access(destination, os.W_OK):
            messagebox.showerror("Erreur", "🚫 Impossible d'écrire dans ce dossier")
            return
        
        self.is_downloading = True
        self.download_btn.config(state="disabled", text="Téléchargement en cours...")
        self.progress_bar['value'] = 0
        self.progress_label.config(text="Démarrage du téléchargement...")
        
        # Démarrer le téléchargement dans un thread
        self.download_thread = threading.Thread(
            target=self._download_thread,
            args=(url, destination)
        )
        self.download_thread.daemon = True
        self.download_thread.start()
    
    def _download_thread(self, url, destination):
        """Thread de téléchargement"""
        try:
            format_type = self.format_var.get()
            quality = self.quality_var.get()
            
            # Construire la commande yt-dlp
            cmd = self._get_ytdlp_command()

            # Options communes pour intégrer thumbnail et métadonnées
            # Requires ffmpeg and yt-dlp; yt-dlp will use mutagen/ffmpeg to embed covers for audio
            common_embed_opts = ['--add-metadata', '--embed-thumbnail']
            cmd.extend(common_embed_opts)
            
            # Structure du nom de fichier pour les playlists
            if self.is_playlist:
                output_template = os.path.join(destination, '%(playlist_index)02d - %(title)s.%(ext)s')
            else:
                output_template = os.path.join(destination, '%(title)s.%(ext)s')
            
            if format_type == "video":
                # Appliquer la qualité sélectionnée
                if "2160p" in quality:
                    cmd.extend(['-f', 'bestvideo[height<=2160]+bestaudio/best[height<=2160]'])
                elif "1440p" in quality:
                    cmd.extend(['-f', 'bestvideo[height<=1440]+bestaudio/best[height<=1440]'])
                elif "1080p" in quality:
                    cmd.extend(['-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'])
                elif "720p" in quality:
                    cmd.extend(['-f', 'bestvideo[height<=720]+bestaudio/best[height<=720]'])
                elif "480p" in quality:
                    cmd.extend(['-f', 'bestvideo[height<=480]+bestaudio/best[height<=480]'])
                elif "360p" in quality:
                    cmd.extend(['-f', 'bestvideo[height<=360]+bestaudio/best[height<=360]'])
                else:
                    # Meilleure qualité par défaut
                    cmd.extend(['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'])
                
                cmd.extend(['--merge-output-format', 'mp4'])
            else:
                cmd.extend(['-x', '--audio-format', 'mp3'])
                
                # Appliquer la qualité audio
                if "320" in quality:
                    cmd.extend(['--audio-quality', '0'])
                elif "256" in quality:
                    cmd.extend(['--audio-quality', '256k'])
                elif "192" in quality:
                    cmd.extend(['--audio-quality', '192k'])
                elif "128" in quality:
                    cmd.extend(['--audio-quality', '128k'])
                else:
                    cmd.extend(['--audio-quality', '0'])
            
            # Options communes
            cmd.extend([
                '-o', output_template,
                '--no-playlist' if not self.is_playlist else '--yes-playlist',
                '--newline',
                '--no-warnings',
                '--progress',
                url
            ])
            
            if self.is_playlist:
                self.message_queue.put(("log", f"📚 Playlist détectée : {self.playlist_name}", "info"))
                self.message_queue.put(("log", f"📁 Dossier de la playlist : {destination}", "info"))
            else:
                self.message_queue.put(("log", "🚀 Téléchargement démarré...", "info"))
                self.message_queue.put(("log", f"📁 Destination : {destination}", "info"))
            
            # Exécuter yt-dlp
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                creationflags=self._get_creation_flags(),
                universal_newlines=True
            )
            
            # Variables pour suivre la progression
            total_videos = 0
            current_video = 0
            
            # Lire la sortie en temps réel
            for line in process.stdout:
                line = line.strip()
                if line:
                    # Détecter le nombre total de vidéos dans une playlist
                    if '[playlist]' in line and 'Downloading' in line:
                        match = re.search(r'Downloading (\d+) items', line)
                        if match:
                            total_videos = int(match.group(1))
                            self.message_queue.put(("log", f"📊 Nombre total de vidéos : {total_videos}", "info"))
                    
                    # Détecter quand une nouvelle vidéo commence
                    if '[download]' in line and 'Downloading item' in line:
                        match = re.search(r'Downloading item (\d+) of', line)
                        if match:
                            current_video = int(match.group(1))
                            if total_videos > 0:
                                self.message_queue.put(("log", f"🎬 Téléchargement de la vidéo {current_video}/{total_videos}", "info"))
                    
                    # Parser la progression
                    if '[download]' in line and '%' in line:
                        # Extraire le pourcentage
                        match = re.search(r'(\d+\.?\d*)%', line)
                        if match:
                            percent = float(match.group(1))
                            # Calculer la progression globale pour les playlists
                            if total_videos > 0 and current_video > 0:
                                # Progression de la vidéo actuelle
                                video_progress = percent / 100
                                # Progression globale
                                overall_progress = ((current_video - 1) + video_progress) / total_videos * 100
                                progress_text = f"Playlist: {current_video}/{total_videos} ({percent:.1f}%) - {line}"
                                self.message_queue.put(("progress", overall_progress, progress_text))
                            else:
                                self.message_queue.put(("progress", percent, line))
                    
                    # N'afficher que les messages importants
                    if any(keyword in line.lower() for keyword in ['download', 'merging', 'destination', 'error', 'warning', 'extract']):
                        if not line.startswith('[youtube]') or 'error' in line.lower():
                            self.message_queue.put(("log", line, "info"))
            
            process.wait()
            
            if process.returncode == 0:
                if self.is_playlist:
                    self.message_queue.put(("log", f"✅ Playlist téléchargée avec succès! ({total_videos} vidéos)", "success"))
                    self.message_queue.put(("log", f"📁 Tous les fichiers sont dans : {destination}", "success"))
                else:
                    self.message_queue.put(("log", "✅ Téléchargement terminé avec succès!", "success"))
                    self.message_queue.put(("log", f"📁 Fichier enregistré dans : {destination}", "success"))
                self.message_queue.put(("complete", True))
            else:
                self.message_queue.put(("log", "❌ Échec du téléchargement", "error"))
                self.message_queue.put(("log", f"Code d'erreur: {process.returncode}", "error"))
                self.message_queue.put(("complete", False))
        
        except FileNotFoundError:
            error_msg = "yt-dlp n'est pas trouvé. "
            if self.is_exe:
                error_msg += "Placez yt-dlp.exe dans le même dossier que l'application."
            else:
                error_msg += "Installez-le avec: pip install yt-dlp"
            
            self.message_queue.put(("log", f"❌ {error_msg}", "error"))
            self.message_queue.put(("complete", False))
        except Exception as e:
            self.message_queue.put(("log", f"❌ Erreur lors du téléchargement: {str(e)[:200]}", "error"))
            self.message_queue.put(("complete", False))
    
    def process_queue(self):
        """Traiter la file de messages"""
        try:
            while True:
                message = self.message_queue.get_nowait()
                
                if message[0] == "log":
                    self.log_message(message[1], message[2])
                elif message[0] == "type":
                    self.video_type.set(message[1])
                elif message[0] == "progress":
                    self.progress_bar['value'] = message[1]
                    self.progress_label.config(text=message[2])
                elif message[0] == "complete":
                    self.is_downloading = False
                    self.download_btn.config(state="normal", text="⬇️  TÉLÉCHARGER")
                    self.progress_bar['value'] = 100 if message[1] else 0
                    if message[1]:
                        self.progress_label.config(text="✅ Téléchargement terminé!")
                        if self.is_playlist:
                            self.log_message("✅ Téléchargement de la playlist terminé!", "success")
                        else:
                            self.log_message("✅ Téléchargement terminé avec succès!", "success")
                    else:
                        self.progress_label.config(text="❌ Échec du téléchargement")
                        self.log_message("❌ Le téléchargement a échoué", "error")
        except:
            pass
        
        self.root.after(100, self.process_queue)
    
    def log_message(self, message, msg_type="info"):
        """Ajouter un message au journal"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Couleurs selon le type
        colors = {
            "info": "#2c3e50",
            "success": "#27ae60",
            "warning": "#f39c12",
            "error": "#e74c3c"
        }
        
        # Configurer les tags
        for tag, color in colors.items():
            self.log_text.tag_config(tag, foreground=color)
        
        # Ajouter le message
        self.log_text.insert("end", f"[{timestamp}] ", "info")
        self.log_text.insert("end", f"{message}\n", msg_type)
        self.log_text.see("end")


def main():
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
