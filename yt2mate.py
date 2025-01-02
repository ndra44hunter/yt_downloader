import os
import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        yt = YouTube(url)
        
        # Pilih format (MP4 atau MP3)
        if format_var.get() == "MP4":
            # Pilih resolusi video terbaik
            video_stream = yt.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()
            # Pilih lokasi penyimpanan
            download_path = filedialog.askdirectory(title="Select Download Folder")
            if download_path:
                video_stream.download(download_path)
                messagebox.showinfo("Success", f"Video downloaded successfully to {download_path}")
        elif format_var.get() == "MP3":
            # Pilih audio stream terbaik
            audio_stream = yt.streams.filter(only_audio=True).first()
            # Pilih lokasi penyimpanan
            download_path = filedialog.askdirectory(title="Select Download Folder")
            if download_path:
                audio_stream.download(download_path, filename=f"{yt.title}.mp3")
                messagebox.showinfo("Success", f"Audio downloaded successfully to {download_path}")
        else:
            messagebox.showerror("Error", "Please select a valid format")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setup GUI
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200")

# URL input
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Format selection
format_var = tk.StringVar(value="MP4")
mp4_radio = tk.Radiobutton(root, text="MP4", variable=format_var, value="MP4")
mp3_radio = tk.Radiobutton(root, text="MP3", variable=format_var, value="MP3")
mp4_radio.pack()
mp3_radio.pack()

# Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

root.mainloop()
