"""
Defines the web application routes and handler functions
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

RESULT_TEMPLATE = """For the given statement, the system response is
                    'anger': {}, 
                    'disgust': {}, 
                    'fear': {}, 
                    'joy': {} and 
                    'sadness': {}. 
                    The dominant emotion is {}."""

@app.route("/")
def render_home():
    """
    Handles requests for home or root endpoint
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Handles GET requests for detecting emotion of input text
    """

    # extract input from GET request
    text_to_analyze = request.args.get('textToAnalyze')

    # call emotion detection module
    data = emotion_detector(text_to_analyze)

    # extract data from response
    dominant_emotion = data['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = data['anger']
    disgust = data['disgust']
    fear = data['fear']
    joy = data['joy']
    sadness = data['sadness']

    # return formatted result
    return RESULT_TEMPLATE.format(anger, disgust, fear, joy, sadness, dominant_emotion)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
