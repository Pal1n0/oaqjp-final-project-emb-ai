"""
Test server for emotion detection application
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detection")

@app.route("/")
def homescreen():
    """
    Rendering homescreen.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    """
    Returning detected emotions.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyse)

    dominant_emotion = output["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = output["anger"]
    disgust = output["disgust"]
    fear = output["fear"]
    joy = output["joy"]
    sadness = output["sadness"]

    return f"""For the given statement, the system response is
        'anger': {anger}, 'disgust': {disgust}, 
        'fear':{fear}, 'joy': {joy} and 'sadness': {sadness}. 
        The dominant emotion is {dominant_emotion}."""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
