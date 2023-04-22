
# Imports
from pygame import mixer
from time import sleep
import random, os

# Song Class
class Song:
    def __init__(self):
        pass

    def randomizeSong(self):
        path = os.getcwd()
        path = os.path.dirname(path)
        song_files_path = path + "\\" + "Song_WAV_Files"
        random_song_path = song_files_path + "\\" + random.choice(os.listdir(song_files_path))
        self.path = random_song_path

    # Starts playing a random song from the path asynchronously
    def startRandomSong(self):
        self.randomizeSong()
        mixer.init(devicename='AmazonBasics05')
        mixer.music.load(self.path)
        mixer.music.set_volume(0.7)
        mixer.music.play()

test = Song()
test.startRandomSong()
sleep(10)


