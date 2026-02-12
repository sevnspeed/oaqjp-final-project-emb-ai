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


'''
#below is testing code above is good code
import requests, json

def emotion_detector(text_to_analyse):
    #1st line for testing outside online!!!
    response = {"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myjson, headers = header)
    formatted_response = json.loads(response.text)
    emotionpredict = formatted_response['emotionPredictions'][0]
    emotion = emotionpredict['emotion']
    '''
    anger_score = float(emotion['anger'])
    disgust_score = float(emotion['disgust'])
    fear_scorescore = float(emotion['fear'])
    joy_scorescore = float(emotion['joy'])
    sadness_score = float(emotion['sadness'])
    '''
    domkey = max(emotion, key=emotion.get)
    emotion['dominant_emotion']=domkey
    print(emotion)
'''
print(formatted_response)
emotionpredict = formatted_response['emotionPredictions'][0]
emotion = emotionpredict['emotion']
typetest = type(emotion)
print(typetest)
print(emotion)
emotion1 = float(emotion['anger'])

typetest = type(emotion1)
print(emotion1)
'''


'''
    anger_label = formatted_response['emotionPredictions']['label']
    anger_score = formatted_response['emotionPredictions']['score']
    disgust_label = formatted_response['emotionPredictions']['label']
    disgust_score = formatted_response['emotionPredictions']['score']
    fear_label = formatted_response['emotionPredictions']['label']
    fear_score = formatted_response['emotionPredictions']['score']
    joy_label = formatted_response['emotionPredictions']['label']
    joy_score = formatted_response['emotionPredictions']['score']
    sadness_label = formatted_response['emotionPredictions']['label']
    sadness_score = formatted_response['emotionPredictions']['score']
'''

 
    #label = formatted_response['documentSentiment']['label']
    #score = formatted_response['documentSentiment']['score']
    #return {'label': label, 'score': score}
'''
