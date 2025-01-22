import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    data = json.loads(response.text)

    # extract useful data
    anger = data["emotionPredictions"][0]["emotion"]["anger"]
    disgust = data["emotionPredictions"][0]["emotion"]["disgust"]
    fear = data["emotionPredictions"][0]["emotion"]["fear"]
    joy = data["emotionPredictions"][0]["emotion"]["joy"]
    sadness = data["emotionPredictions"][0]["emotion"]["sadness"]

    hiScore = anger
    dominant_emotion = "anger"

    if disgust > hiScore:
        hiScore = disgust
        dominant_emotion = "disgust"
    
    if fear > hiScore:
        hiScore = fear
        dominant_emotion = "fear"

    if joy > hiScore:
        hiScore = joy
        dominant_emotion = "joy"
    
    if sadness > hiScore:
        hiScore = sadness
        dominant_emotion = "sadness"

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }