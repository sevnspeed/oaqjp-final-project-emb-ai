import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myjson, headers = header)
    formatted_response = json.loads(response.text)
    emotionpredict = formatted_response['emotionPredictions'][0]
    emotion = emotionpredict['emotion']
    domkey = max(emotion, key=emotion.get)
    emotion['dominant_emotion']=domkey
    return(emotion)
