"""
Emotion detection library
"""

import requests

def emotion_detector(text_to_analyse):
    """
    Fuction to detect emotion of given text, calling Watson NLP library.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input =  { "raw_document": { "text": text_to_analyse } } 

    response = requests.post(url, json=json_input ,headers = headers, timeout = 10)

    if response.status_code != 200:
        print(f"Error from external service: {response.status_code} - {response.text}")


    if response.status_code == 400:
        results_for_empty_str = (
        {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        )

        return results_for_empty_str

    json_response = response.json()

    max_score = 0
    max_score_emotion = None

    for emotion, score in json_response["emotionPredictions"][0]["emotion"].items():
        if score > max_score:
            max_score = score
            max_score_emotion = emotion

    anger_score = json_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = json_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = json_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = json_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = json_response["emotionPredictions"][0]["emotion"]["sadness"]

    emotion_results = (
    {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': max_score_emotion
    }
    )
    return emotion_results



