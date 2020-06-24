from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tekore as tk
from dotenv import load_dotenv
import os
import pprint
import unittest
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#app.config is only to avoid an error

# initialize Spotify cursor
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
cred = tk.Credentials(CLIENT_ID,CLIENT_SECRET)
access_token = cred.request_client_token()
spotify = tk.Spotify(access_token)

@app.route('/')
def root():
    return "Try /songs or /prediction instead." 
#NOT intended to be accessed

@app.route('/songs')
def songs():
    tracks, = spotify.search('5 best songs',types=('track',), limit=5)
    result = ''
    for track in tracks.items:
        result = result + track.name + '\n'#' by ' + track.artists.name + 
    return result #Right now, will only return track names with no other information
#Output: If You're Happy And You Know It I'm A Little Teapot There Was An Old Lady Who Swallowed A Fly The Teddy Bears Picnic Hokey Pokey
@app.route('/prediction', methods=['POST'])
def predict():
    '''
    Receives input data, gets track features/analysis (feeds it to model), converts to .json object and returns it
    '''
    # Receive JSON of song id's
    song_inp_json = request.json
    song_inp = song_inp_json['song_id_list']
    song_count = song_inp_json['recommendation_count']
    print(song_inp)

    # Print song titles based on track id's
    features = []
    analyses = []
    # for song_id in song_inp:
    #     features.append(spotify.track_audio_features(song_id))
    #     analyses.append(spotify.track_audio_analysis(song_id))
    
    # #print song info received
    # print(str(features))
    # print('\n--------\n')
    # print(str(analyses))

    # pretend we have song recommendations
    song_out = ["7FGq80cy8juXBCD2nrqdWU",
                "20hsdn8oITBsuWNLhzr5eh",
                "7fPuWrlpwDcHm5aHCH5D9t",
                "2BOqDYLOJBiMOXShCV1neZ",
                "67O8CWXxPsfz8orZVGMQwf"
    ]
    # Get song features
    for song_id in song_out:
        features.append(spotify.track_audio_features(song_id))# Will display 5 songs
    
                
    song_out_json = {"recommended_song_id_list": song_out}

    return str(features)#song_out_json
#Heroku displays "METHOD NOT ALLOWED" currently for /prediction
@app.route('/testsongs')
    def testsongs():
        unittest.FunctionTestCase(songs())
#Error: "GET /testsongs HTTP/1.1" 500 290 
@app.route('/testpredict')
    def testpredict():
        unittest.FunctionTestCase(predict())
# Error:"GET /testpredict HTTP/1.1" 500 290 
#500: A catch-all error code that is affected by an internal conflict.
#Will look into this.
if __name__=='__main__':
    app.run(debug=True)