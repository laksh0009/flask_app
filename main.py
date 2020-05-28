from flask import Flask, render_template

app = Flask(__name__)
'''
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not get you...Please try again.")
'''


@app.route('/')
def home():
    # return "<center><a href='http://127.0.0.1:5000/index'><button type='button'>Click....!</button></a></center>"
    # return "Hiiii"
    return render_template('home.html')


@app.route('/index')
def index():
    return "<center><h1>Hello<br> Thanks for your support.</h1><br/><center>"


if __name__ == '__main__':
    app.run(debug=True)
