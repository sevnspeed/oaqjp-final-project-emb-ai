import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #error if url not URL? due to webscript provided? all caps due to constant
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = myjson, headers = header)
    formatted_response = json.loads(response.text) #keys epred, prodid
    emotionpredict = formatted_response['emotionPredictions'][0] #keys emot, targ, emotmen
    emotion = emotionpredict['emotion']
    domkey = max(emotion, key=emotion.get)
    emotion['dominant_emotion']=domkey
    return(emotion)
