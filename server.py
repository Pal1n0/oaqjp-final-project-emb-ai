from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detection")

@app.route("/")
def homescreen():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection(text_to_analyse):
    output = emotion_detector(text_to_analyse)
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

