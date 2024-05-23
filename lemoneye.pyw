import time
from pydub import AudioSegment
from pydub.playback import play

intro = AudioSegment.from_wav("startup.wav")
play(intro)

while True:
    time.sleep(1200.0)
    song = AudioSegment.from_wav("app_tone.wav")
    play(song)