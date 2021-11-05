# Keroline - Russian-speaking Voice Assistant App Python for Windows
\
![ ](https://i.ibb.co/vhR78xh/image.png)

 ### App features:
* Speech recognize and synthesize
* Random greetings and goodbyes playback
* Google search
* Receiving information about the weather forecast (the city specified by default in the settings)
* Executing certain applications (Spotify, Telegram, Browser, Office) if you set up the path to .exe in the settings
* Date and time voice notification
* Simple math operations (sum, subtraction, multiplication, division, sqrt, exp)
* Coin flipping
* Random answering when asked yes or no

### To install all dependencies use the command:
`pip install --r requirements.txt`

If you got an error while installing PyAudio, then check availability of Microsoft Visual C++ Build Tools or do follow:\
`pip install pipwin` \
`pipwin install pyaudio` 

### To run the application, go to directory ‘src’ and enter the command:
`python app.py` 

### Used third-party libraries:
Library           | Function
------------------|----------------------
Kivy              | Interface
PyAudio           | Capturing audio from a microphone
SpeechRecognition | Speech recognition
pyttsx3	          | Speech synthesis
