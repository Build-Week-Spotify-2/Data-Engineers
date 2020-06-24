from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tekore as tk
from dotenv import load_dotenv
import os
import pprint

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# initialize Spotify cursor
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
cred = tk.Credentials(CLIENT_ID,CLIENT_SECRET)
access_token = cred.request_client_token()
spotify = tk.Spotify(access_token)

@app.route('/')
def root():
    return "You don't want to look at this page"

@app.route('/songs')
def songs():
    tracks, = spotify.search('5 best songs',types=('track',), limit=5)
    result = ''
    for track in tracks.items:
        result = result + track.name + '\n'#' by ' + track.artists.name + 
    return result

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
        features.append(spotify.track_audio_features(song_id))
    
                
    song_out_json = {"recommended_song_id_list": song_out}

    return str(features)#song_out_json

if __name__=='__main__':
    app.run(debug=True)