import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp as youtube_dl

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Video Downloader")
        self.geometry("400x300")

        # URL input
        self.url_label = tk.Label(self, text="YouTube URL:")
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        # Download button
        self.download_button = tk.Button(self, text="Download", command=self.download_video)
        self.download_button.pack(pady=20)

        # Options for resolutions and audio
        self.resolution_var = tk.StringVar(value="video")
        self.resolution_label = tk.Label(self, text="Select Resolution:")
        self.resolution_label.pack(pady=5)

        self.resolution_menu = tk.OptionMenu(self, self.resolution_var, "Audio", "360p", "480p", "720p", "1080p")
        self.resolution_menu.pack(pady=5)

        # Status label
        self.status_label = tk.Label(self, text="")
        self.status_label.pack(pady=10)

    def download_video(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
            return

        resolution = self.resolution_var.get()
        ydl_opts = {
            'format': 'bestaudio/best' if resolution == "Audio" else f'bestvideo[height<={resolution}]+bestaudio/best',
            'outtmpl': f'{filedialog.askdirectory()}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',  # Specify format for merging video and audio
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", "Download completed successfully.")
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()