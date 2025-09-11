import os
from lib.player import Playlist
import pygame

# Path to your folder containing mp3 files
music_folder = "E:/code/coding/advance_python/music_player/playlist"
play_list = Playlist(music_folder)

# Get all mp3 files from folder
song_list = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
#song_list.sort()  # sort alphabetically
for song in song_list:
    play_list.add_song(song)

print("\nControls:")
print("p = pause, r = resume, s = stop, n = next, b = back, q = quit\n")

# Initialize mixer
pygame.mixer.init()
#starting with first song in the playlist
play_list.play_song(song_list[0])

while True:
    command = input("Enter command: ").strip().lower()
    if command == "p":  # pause
        pygame.mixer.music.pause()
        print("⏸ Paused")

    elif command == "r":  # resume
        pygame.mixer.music.unpause()
        print("▶ Resumed")

    elif command == "s":  # stop
        pygame.mixer.music.stop()
        print("⏹ Stopped")

    elif command == "n":  # next song
        play_list.play_next_song()

    elif command == "b":  # previous song
        play_list.play_previous_song()

    elif command == "q":  # quit
        pygame.mixer.music.stop()
        print("👋 Exiting player")
        break

    else:
        print("Invalid command. Use p/r/s/n/b/q.")