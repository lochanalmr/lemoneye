# lemoneye
a python script that sends an audio reminder every 20 minutes, for those who want to use the 20-20-20 rule to protect their eyes.

## prerequisites
- ffmpeg
- pydub
- pyaudio

## setup (if you don't have the prerequisites)
1. first, install the latest version of python from python.org.
2. then using powershell or terminal, install pydub and pyaudio packages. (pip install *)
3. install ffmpeg, using the instructions on ffmpeg.org/download.
4. download the code, extract the zip file, and click on lemoneye.pyw to run the file.

## setup (if you have the prerequisites)
1. download the code, extract the zip file, and click on lemoneye.pyw to run the file.

## customization
you can replace the startup and app_tone audio files with wav files. just make sure that the startup tone is not too long and that the app_tone is not longer than 30 seconds maximum.
this script can be used to repetitively play any music, but the audio files should be wav files, and the files should be renamed to startup.wav, and app_tone.wav.
you can adjust the waiting duration by changing the time.sleep() line in the python script. change the duration within parenthesis. (by default it is 1200.0)
