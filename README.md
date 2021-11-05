## Keroline - Russian-speaking Voice Assistant App Python for Windows
\
![ ](https://i.ibb.co/vhR78xh/image.png)

### App features:
* Recognize and synthesize speech
* Play random greetings and goodbyes
* Make a Google search
* Get information about the weather forecast (the city is specified by default in the settings)
* Run certain applications (Spotify, Telegram, Browser, Office) if you register the path to exe in the settings
* Speak date and time
* Perform simple math operations (sum, subtraction, multiplication, division, sqrt, exp)
* Flip coin
* Give a random answer when asked yes or no

### To install all dependencies use the command:
`pip install --r requirements.txt`

If you got an error while installing PyAudio, then check availability of Microsoft Visual C++ Build Tools or do follow:\
`pip install pipwin` \
`pipwin install pyaudio` 

### To run the application, go go to directory ‘src’ and enter the command:
`python app.py` 

### Used third party libraries:
Library  | Function
----------------|----------------------
Kivy |Interface
PyAudio | Capturing audio from a microphone
SpeechRecognition | Speech recognition
pyttsx3	| Speech synthesis