'''
starts web app interface with Flask on localhost:5000 to receive text input,
pass to Watson for Emotion detection and return results with dominant emotion
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def report_emotion():
    '''Send input text from web to emotion_detector function and return formatted response '''
    #analyse is input of emotion_detector,Analyze is var used in webscript
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    #below was ''' ''' but pylint says pointless string statement so commenting out each
    #static mywebscript.js and templates index.html provided
    #Below is alternate code idea in case return by key .format errors or does not work,
    #keeping for reference
    #angerval = response['anger']
    #disgustval = response['disgust']
    #fearval = response['fear']
    #joyval = response['joy']
    #sadval = response['sadness']
    #domemot = response['dominent_emotion']
    #emotion_list = list(emotion)
    ##line split below to pass pylint, one line in prog
    #return "For the given statement, the system response is
    # 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, and 'sadness': {}.
    #  The dominant emotion is <b>{}</b>".format(angerval,
    #   disgustval, fearval, joyval, sadval, domemot)"""

    if response['dominant_emotion'] == 'None': #if dominant emotion None (no input), error
        return 'Invalid text! Please try again'

    #(valid input)
    #return by key value with .format changed to string var and fprint per pylint
    #was return "string {}.format(response['key'])"
    #\ continues line
    outtext = f"For the given statement, the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': \
    {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is \
    <b>{response['dominant_emotion']}</b>"
    return outtext
@app.route("/")
def render_index_page():
    '''Renders main web app page with Flask'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
