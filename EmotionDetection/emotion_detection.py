import requests, json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #error if url not URL? due to webscript provided? all caps due to constant
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjson = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = myjson, headers = header)
    formatted_response = json.loads(response.text) #keys epred, prodid
    
    
    '''
    #next 2 lines moved to response ok if statement due to key error from empty input
    #emotionpredict = formatted_response['emotionPredictions'][0] #keys emot, targ, emotmen
    #emotion = emotionpredict['emotion'] #get emotion key val only
    '''

    if response.status_code == 200: #check code 200 (OK)
        emotionpredict = formatted_response['emotionPredictions'][0] #keys emot, targ, emotmen
        emotion = emotionpredict['emotion'] #get emotion key val only
        domkey = max(emotion, key=emotion.get) #assign max val emotion to domkey
        emotion['dominant_emotion'] = domkey #add dominant key and val
    
    if response.status_code == 400: #check status code blank contents
        emotion = {'anger':0, 'joy':0, 'sadness':0, 'disgust':0} #create replacement dictionary, with no input error emotion.Predictions key error  
        emotion = emotion.fromkeys(emotion, 'None') #set all keys value to None
        emotion['dominant_emotion']='None'
        
    return(emotion)
