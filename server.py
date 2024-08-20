""" Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
    detects emotions over it using emotion_detector() function. 
    Returns a sentence stating scores on five emotions and 
    indicating the dominant emotion based on the scores
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']} "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"'{result['dominant_emotion']}'."
    )

@app.route("/")
def render_index():
    ''' This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
