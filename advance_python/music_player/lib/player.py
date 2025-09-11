import os
import pygame

def song_player(music_folder, song):
    song_path = os.path.join(music_folder, song)
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    print(f"\n▶ Now playing: {song}")

class Song:
    def __init__(self, song):
        self.previous=None
        self.song=song
        self.next=None

class Playlist:
    def __init__(self, music_folder):
        self.head=None
        self.tail=None
        self.current_song = None
        self.music_folder=music_folder

    def add_song(self, new_song):
        new_song_in_playlist = Song(new_song)
        if self.head==None:
            self.head=new_song_in_playlist
            self.tail=new_song_in_playlist
            return
        self.tail.next= new_song_in_playlist
        new_song_in_playlist.previous = self.tail
        self.tail=new_song_in_playlist
        self.head.previous = self.tail
        self.tail.next = self.head

    def play_song(self, song):
        if self.head == None:
            print("No song present in the playlist")
            return

        self.current_song = self.head
        while self.current_song != self.tail:
            if song == self.current_song.song:
                song_player(music_folder=self.music_folder, song=self.current_song.song)
                return
            self.current_song= self.current_song.next

        if self.current_song == self.tail:
            song_player(music_folder=self.music_folder, song=self.current_song.song)
            return

    def play_previous_song(self):
        self.current_song=self.current_song.previous
        pygame.mixer.music.stop()
        song_player(music_folder=self.music_folder, song=self.current_song.song)

    def play_next_song(self):
        self.current_song = self.current_song.next
        pygame.mixer.music.stop()
        song_player(music_folder=self.music_folder, song=self.current_song.song)