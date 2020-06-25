import spotipy
import spotipy.util as util
from dotenv import load_dotenv
import os
import pandas as pd


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


def get_proper_dataframe(results):
    results_df = pd.DataFrame(results["tracks"]["items"])

    # album images
    results_df["album_image"] = results_df["album"].apply(lambda x: x["images"][0]["url"])
    # results_df[""]
    # breakpoint()
    return results_df