# Speech2Text

## Requirements:
* Windows OS (preffered)
* Python3 (with some libraries)
* Internet connection
* (?) OBS Studio (to record your audio)
* (?) `ffmpeg` (to convert your file to *.wav)

##### Unfortunatelly Windows is preffered because I cannot install PyAudio on my Llinux quickly :smile:

## How to start? 
1. Prepare your system: <br/>
    * install `Python3` and required librearies, you can use `prepare_python.bat` script if you have pip3 installed, install `PyAudio` may be very funny (below is described how to do that in case of some issues and problems)
    * download and install [OBS Studio](https://obsproject.com/download)
    * download and install [FFmpeg](https://ffmpeg.org/download.html), [quick setup tutorial](https://video.stackexchange.com/questions/20495/how-do-i-set-up-and-use-ffmpeg-in-windows)
2. Prepare your config_file.py
3. Start `create_transcription.bat`
4. Enjoy your transcription

## How to install pyaudoi/ portaudio?
Solution working on Linux Mint:
https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error
\+ possibly: `sudo apt-get install python-pyaudio python3-pyaudio `

Solution for Windows:
https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14
