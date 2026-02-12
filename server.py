from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def report_emotion():
    text_to_analyse = request.args.get('textToAnalyze') #analyse is input of emotion_detector,Analyze is var used in webscript
    response = emotion_detector(text_to_analyse)
    
    '''
    #static mywebscript.js and templates index.html provided
    #Below is alternate code idea in case return by key .format errors or does not work, keeping for reference
    angerval = response['anger']
    disgustval = response['disgust']
    fearval = response['fear']
    joyval = response['joy']
    sadval = response['sadness']
    domemot = response['dominent_emotion']
    emotion_list = list(emotion)

    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, and 'sadness': {}. The dominant emotion is <b>{}</b>".format(angerval, disgustval, fearval, joyval, sadval, domemot)
    '''    
    #return by key value with .format    
    return "For the given statement, the system response is 'anger': {},  disgust': {}, 'fear': {}, 'joy': {}, and 'sadness': {}. The dominant emotion is <b>{}</b>".format(response['anger'], response['disgust'], response['fear'], response['joy'], response['sadness'], response['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
      
    app.run(host="0.0.0.0", port=5000)
