"""
Implements emotion detection functionality for client applications
"""
import requests
import json

EMPTY_RESPONSE = { "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None }
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

def emotion_detector(text_to_analyze):
    """
    Leverages Watson AI API to detect and score the emotion(s) in the input text
    """
    if not text_to_analyze or text_to_analyze == '':
        return EMPTY_RESPONSE # No sense in doing any work without valid input

    myobj = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(URL, json = myobj, headers=HEADERS)

    status = resp.status_code
    if status == 400:
        return EMPTY_RESPONSE

    data = json.loads(resp.text)

    # extract useful data
    anger = data["emotionPredictions"][0]["emotion"]["anger"]
    disgust = data["emotionPredictions"][0]["emotion"]["disgust"]
    fear = data["emotionPredictions"][0]["emotion"]["fear"]
    joy = data["emotionPredictions"][0]["emotion"]["joy"]
    sadness = data["emotionPredictions"][0]["emotion"]["sadness"]

    hiScore = anger
    dominant = "anger"

    if disgust > hiScore:
        hiScore = disgust
        dominant = "disgust"

    if fear > hiScore:
        hiScore = fear
        dominant = "fear"

    if joy > hiScore:
        hiScore = joy
        dominant = "joy"

    if sadness > hiScore:
        hiScore = sadness
        dominant = "sadness"

    return { "anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness, "dominant_emotion": dominant }
