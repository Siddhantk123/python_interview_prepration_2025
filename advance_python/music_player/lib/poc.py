class Song:
    def __init__(self, song):
        self.previous=None
        self.song=song
        self.next=None

class Playlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.current_song = None

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
                print(f"============= Playing song: {self.current_song.song}========================")
                return
            self.current_song= self.current_song.next

        if self.current_song == self.tail:
            print(f"==============Playing song: {self.current_song.song}=========================")
            return
    
        print("Given song not present in the playlist")

    def play_previous_song(self):
        self.current_song=self.current_song.previous
        print(f"===============Playing song: {self.current_song.song}=====================")

    def play_next_song(self):
        self.current_song = self.current_song.next
        print(f"===============Playing song: {self.current_song.song}=========================")

if __name__ == "__main__":
    play_list = Playlist()
    song_list = [
                "Ram aayenge.mp3",
                "Tum ho to.mp3",
                "Sapphire.mp3",
                "Bekhayali.mp3",
                "Saiyara.mp3",
                ]
    for song in song_list:
        play_list.add_song(song)

    user_input = None
    while user_input != "quit":
        user_input = input("Enter > or playing next sing\n"
                       "Enter < for playing previous song\n"
                       "Enter || to play song\n"
                       "Write 'quit' to close playlist\n"
                       )
        if user_input == ">":
            play_list.play_next_song()

        if user_input == "<":
            play_list.play_previous_song()

        if user_input == "||":
            song = input("Enter song you want to play\n")
            play_list.play_song(song)

        if user_input == "quit":
            continue

    
        


    


        

