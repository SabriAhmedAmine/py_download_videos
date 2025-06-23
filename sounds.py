import os
from yt_dlp import YoutubeDL

def download_audio(url, destination, audio_quality=None):
    try:
        # Set download options for audio only
        ydl_opts = {
            'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': audio_quality if audio_quality else '192',
            }],
            'extract_audio': True,  # Extract audio
            'audio_format': 'mp3',  # Convert to mp3
            'audio_quality': audio_quality if audio_quality else '192',  # Audio quality in kbps
        }

        # Download the audio
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Audio download completed! Files saved to {destination}")

    except Exception as e:
        print(f"An error occurred: {e}")

def get_available_audio_qualities():
    # Common audio qualities in kbps
    return ['64', '96', '128', '192', '256', '320']

def get_content_info(url):
    # Fetch content information
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        
        # Check if it's a playlist or single video
        if 'entries' not in info_dict:
            # Single video
            return {'type': 'video', 'title': info_dict.get('title', 'video')}
        else:
            # Playlist
            return {'type': 'playlist', 'title': info_dict.get('title', 'playlist')}

def main():
    # Set default download directory
    default_destination = "./audio_downloads"
    os.makedirs(default_destination, exist_ok=True)

    while True:
        # Ask for YouTube URL
        url = input("Enter the YouTube video or playlist URL: ")

        # Ask for destination folder
        base_destination = input(f"Enter the base destination folder to save the audio(s) (press Enter for default '{default_destination}'): ").strip() or default_destination

        # Get content info
        content_info = get_content_info(url)
        
        # Show available audio qualities
        audio_qualities = get_available_audio_qualities()
        print("Available Audio Qualities:")
        for i, quality in enumerate(audio_qualities, start=1):
            print(f"{i}. {quality} kbps")
            
        # Ask the user to choose an audio quality
        while True:
            try:
                choice = int(input("Choose the audio quality by entering the corresponding number: "))
                if 1 <= choice <= len(audio_qualities):
                    selected_quality = audio_qualities[choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if content_info['type'] == 'playlist':
            # Create a unique folder for the playlist
            playlist_folder = os.path.join(base_destination, content_info['title'])
            os.makedirs(playlist_folder, exist_ok=True)
            print(f"Downloading playlist '{content_info['title']}' audio into folder: {playlist_folder}")
            
            # Download the playlist audio
            download_audio(url, playlist_folder, selected_quality)
        else:
            # For single video, download to the base destination
            print(f"Downloading audio for video: {content_info['title']}")
            download_audio(url, base_destination, selected_quality)

        # Ask the user if they want to continue or exit
        while True:
            continue_choice = input("Do you want to download more audio? (Y/N): ").strip().lower()
            if continue_choice in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

        if continue_choice == 'n':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()