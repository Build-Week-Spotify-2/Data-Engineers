from dotenv import load_dotenv
import os
import pandas as pd
from pdb import set_trace as st
import spotipy
import spotipy.util as util
import sys
import pickle
import sklearn

def get_spotify_token():
    '''
    This function will initiate the spotify token
    return: spotipy object
    '''

    
    load_dotenv("../.env")
    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
    USERNAME = os.getenv("USERNAME")

    token = util.prompt_for_user_token(
        username=USERNAME,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI
    )

    sp = spotipy.Spotify(auth=token)
    return sp


def load_model():
    #import sklearn

    dbfile = open('Predictor/models/kmeans.pickl', 'rb')
    model = pickle.load(dbfile)
    dbfile.close()
    return model


def load_labled_spotify_songs():
    return pd.read_csv("Predictor/data/labled_songs_id.csv")


def get_songs_audio_features(song_id_list, spotipy_obj):
    temp_data = spotipy_obj.audio_features(song_id_list)
    spotify_audio_features = pd.DataFrame(temp_data)

    important_features = [
        # "genre",  # spotify genre doesn't match with kaggle genre
        # "popularity",  # don't know how to get it for the song, and it changes over time
        # "key",  # This is categorical
        # "mode",  # this is categorical
        # "time_signature"  # not for now
        "acousticness",
        "danceability",
        "energy",
        "instrumentalness",
        "liveness",
        "loudness",
        "speechiness",
        "tempo",
        "valence",
    ]
    return spotify_audio_features[important_features]


def get_n_similar_songs(song_label, labled_songs, n, spotipy_obj):
    '''
    args:
        song_label: the average song audio features
        labled_songs: the dataframe that has all the
            songs' cluster lables
        n: number of required recommendations
    
    return:
        list of recommended song ids
    '''

    same_cluster_songs = \
        labled_songs[labled_songs["label"] == song_label]\
        .loc[:, "track_id"]
        
    list_of_recommended_songs = same_cluster_songs.head(n).to_list()
    return list_of_recommended_songs


def add_artist_name_song_name(output_df, spotipy_obj):
    tracks = spotipy_obj.tracks(output_df["song_id"].to_list())
    list_of_tracks = tracks["tracks"]
    list_of_tracks_df = pd.DataFrame(list_of_tracks)
    
    output_df["artists"] = \
        list_of_tracks_df["artists"].apply(lambda x: [artist_dict["name"] for artist_dict in x])
    output_df["song_name"] = list_of_tracks_df["name"]
    
    return output_df