import requests

def emotion_detector(text_to_analyse):
    """
    Fuction to detect emotion of given text, calling Watson NLP library.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input =  { "raw_document": { "text": text_to_analyse } } 

    response = requests.post(url, json=json_input ,headers = headers, timeout = 10)

    return response.text



