import tkinter as tk
from tkinter import filedialog
import os
import pygame
from lib.player import Playlist

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini MP3 Player")
        self.root.geometry("400x200")
        self.playlist=None

        # Initialize mixer
        pygame.mixer.init()
        
        # UI Buttons
        self.load_btn = tk.Button(root, text="📂 Load Folder", command=self.load_folder, width=12)
        self.play_btn = tk.Button(root, text="▶ Play", command=self.play_song, width=12, state="disabled")
        self.pause_btn = tk.Button(root, text="⏸ Pause", command=self.pause_song, width=12, state="disabled")
        self.resume_btn = tk.Button(root, text="▶ Resume", command=self.resume_song, width=12, state="disabled")
        self.next_btn = tk.Button(root, text="⏭ Next", command=self.next_song, width=12, state="disabled")
        self.prev_btn = tk.Button(root, text="⏮ Prev", command=self.prev_song, width=12, state="disabled")
        self.stop_btn = tk.Button(root, text="⏹ Stop", command=self.stop_song, width=12, state="disabled")

        # Label to show current song
        self.label = tk.Label(root, text="No song loaded", fg="blue")

        # Place buttons
        self.label.pack(pady=10)
        self.load_btn.pack(pady=5)
        self.play_btn.pack(pady=5)
        self.pause_btn.pack(pady=5)
        self.resume_btn.pack(pady=5)
        self.next_btn.pack(pady=5)
        self.prev_btn.pack(pady=5)
        self.stop_btn.pack(pady=5)

    def load_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.playlist = Playlist(folder) #important backend code

            # Get all mp3 files from folder
            song_list = [f for f in os.listdir(folder) if f.endswith(".mp3")]
            #song_list.sort()  # sort alphabetically
            if song_list:
                for song in song_list:
                    self.playlist.add_song(song)

                self.label.config(text=f"Ready: {os.path.basename(song_list[0])}")
                self.play_btn.config(state="normal")
                self.next_btn.config(state="normal")
                self.prev_btn.config(state="normal")
                self.stop_btn.config(state="normal")

    def play_song(self):
        self.playlist.play_song(song=self.playlist.head.song)

        self.label.config(text=f"Playing: {os.path.basename(self.playlist.current_song.song)}")
        self.pause_btn.config(state="normal")
        self.resume_btn.config(state="disabled")

    def pause_song(self):
        pygame.mixer.music.pause()

        self.label.config(text="Paused")
        self.pause_btn.config(state="disabled")
        self.resume_btn.config(state="normal")

    def resume_song(self):
        pygame.mixer.music.unpause()

        self.label.config(text=f"Playing: {os.path.basename(self.playlist.current_song.song)}")
        self.pause_btn.config(state="normal")
        self.resume_btn.config(state="disabled")

    def stop_song(self):
        pygame.mixer.music.stop()

        self.label.config(text="Stopped")
        self.pause_btn.config(state="disabled")
        self.resume_btn.config(state="disabled")

    def next_song(self):
        self.playlist.play_next_song()

        self.label.config(text=f"Playing: {os.path.basename(self.playlist.current_song.song)}")

    def prev_song(self):
        self.playlist.play_previous_song()

        self.label.config(text=f"Playing: {os.path.basename(self.playlist.current_song.song)}")

# Run Tkinter app
root = tk.Tk()
app = MP3Player(root)
root.mainloop()
