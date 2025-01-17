import os
from yt_dlp import YoutubeDL

def download_video_or_playlist(url, destination, resolution=None):
    try:
        # Set download options
        ydl_opts = {
            'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Combine video and audio into mp4
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Ensure the output is in mp4 format
            }],
        }

        # If resolution is specified, use it (for single videos)
        if resolution:
            ydl_opts['format'] = f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]'
        else:
            # For playlists, download the highest quality available
            ydl_opts['format'] = 'bestvideo+bestaudio/best'

        # Download the video or playlist
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed! Files saved to {destination}")

    except Exception as e:
        print(f"An error occurred: {e}")

def get_available_resolutions(url):
    # Fetch available formats
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)

        # If it's a single video, extract resolutions
        if 'entries' not in info_dict:
            formats = info_dict.get('formats', None)
            resolutions = set()
            for fmt in formats:
                height = fmt.get('height')
                if height is not None:  # Only include formats with a valid height
                    resolutions.add(height)
            return sorted(resolutions, reverse=True)
        else:
            # If it's a playlist, return the playlist title
            return info_dict.get('title', 'playlist')

def main():
    # Set default download directory
    default_destination = "./downloads"
    os.makedirs(default_destination, exist_ok=True)

    while True:
        # Ask for YouTube URL
        url = input("Enter the YouTube video or playlist URL: ")

        # Ask for destination folder (default to "./downloads" if left blank)
        base_destination = input(f"Enter the base destination folder to save the video(s) (press Enter for default '{default_destination}'): ").strip() or default_destination

        # Fetch available resolutions (only for single videos) or playlist title
        result = get_available_resolutions(url)

        if isinstance(result, list):  # Single video
            resolutions = result
            print("Available Resolutions:")
            for i, resolution in enumerate(resolutions, start=1):
                print(f"{i}. {resolution}p")

            # Ask the user to choose a resolution by number
            while True:
                try:
                    choice = int(input("Choose the resolution by entering the corresponding number: "))
                    if 1 <= choice <= len(resolutions):
                        selected_resolution = resolutions[choice - 1]
                        break
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Download the single video with the selected resolution
            download_video_or_playlist(url, base_destination, selected_resolution)
        else:  # Playlist
            playlist_title = result
            # Create a unique folder for the playlist
            playlist_folder = os.path.join(base_destination, playlist_title)
            os.makedirs(playlist_folder, exist_ok=True)
            print(f"Downloading playlist '{playlist_title}' into folder: {playlist_folder}")

            # Download the playlist in the highest quality
            download_video_or_playlist(url, playlist_folder)

        # Ask the user if they want to continue or exit
        while True:
            continue_choice = input("Do you want to continue? (Y/N): ").strip().lower()
            if continue_choice in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

        if continue_choice == 'n':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()