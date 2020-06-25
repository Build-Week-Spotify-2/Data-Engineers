from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tekore as tk
from dotenv import load_dotenv
import os
from Predictor import predictor

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#app.config is only to avoid an error
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

# initialize Spotify cursor
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
cred = tk.Credentials(CLIENT_ID,CLIENT_SECRET)
access_token = cred.request_client_token()
spotify = tk.Spotify(access_token)
def validate_post_data(data_object):
    if ('Results_gathered' in data_object or "recommended_song_id_list" in data_object):
        return True
    else:
        return False
#This function will be to validate everything is functioning properly
#and will also specify that a user's inputs are wrong.
@app.route('/')
def root():
    return "Try /songs or /prediction instead." 
#NOT intended to be accessed

@app.route('/songs')
def songs():
    tracks, = spotify.search('5 best songs',types=('track',), limit=5)
    result = ''
    for track in tracks.items:
        result = result + track.name  + '\n'#' by ' + track.artists.name + 
    return result
    if validate_post_data(data_object=result):
        correct = {'Results_gathered':result}
    else:
        return "Not a valid input!" #Right now, will only return track names with no other information

@app.route('/prediction', methods=['POST'])
def prediction():
    '''
    Receives input data, gets track features/analysis (feeds it to model), converts to .json object and returns it
    '''
    # Receive JSON of song id's
    song_inp_json = request.json
    song_inp = song_inp_json['song_id_list']
    song_count = song_inp_json['recommendation_count']

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

    # song_out = ["7FGq80cy8juXBCD2nrqdWU",
    #             "20hsdn8oITBsuWNLhzr5eh",
    #             "7fPuWrlpwDcHm5aHCH5D9t",
    #             "2BOqDYLOJBiMOXShCV1neZ",
    #             "67O8CWXxPsfz8orZVGMQwf"
    # ]
    song_out_json = predictor.predict(song_inp, song_count)

    # Get song features
    # for song_id in song_out:
    #     features.append(spotify.track_audio_features(song_id))# Will display 5 songs
    
                
    # song_out_json = {"recommended_song_id_list": song_out}

    return song_out_json

if __name__=='__main__':
    app.run(debug=True)
