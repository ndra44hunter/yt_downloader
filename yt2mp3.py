import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp as youtube_dl

def download_audio():
    youtube_url = url_entry.get()
    
    if not youtube_url.strip():
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    # Choose the output folder
    output_folder = filedialog.askdirectory(title="Select Folder to Save MP3")
    if not output_folder:
        messagebox.showinfo("Cancelled", "Download cancelled. No folder selected.")
        return

    # yt-dlp options for downloading audio as MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Save as title.mp3 in the chosen folder
        'quiet': True,  # Suppress detailed logs
        'noplaylist': True  # Avoid downloading playlists
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        messagebox.showinfo("Success", "MP3 downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")

# Create the GUI window
root = tk.Tk()
root.title("YouTube to MP3 Downloader")
root.geometry("400x150")
root.resizable(False, False)

# URL Label
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack(pady=5)

# URL Entry Field
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download as MP3", command=download_audio)
download_button.pack(pady=20)

# Run the GUI loop
root.mainloop()