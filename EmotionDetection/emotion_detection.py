import requests
import json

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_dict = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_dict, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions_dict.items(), key=lambda x: x[1])[0]

        return {
            'anger': emotions_dict['anger'],
            'disgust': emotions_dict['disgust'],
            'fear': emotions_dict['fear'],
            'joy': emotions_dict['joy'],
            'sadness': emotions_dict['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }