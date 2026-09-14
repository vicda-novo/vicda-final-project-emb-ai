"""Emotion detection application using the Watson NLP library"""
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=input_json)

    # Convert response text to a dictionary
    res = json.loads(response.text)

    # Extract the emotion scores
    formatted_output = res['emotionPredictions'][0]['emotion']

    # Find the dominant emotion (highest score)
    dominant_emotion = max(formatted_output, key=lambda x: formatted_output[x])

    # Add dominant emotion to the output
    formatted_output['dominant_emotion'] = dominant_emotion

    return formatted_output