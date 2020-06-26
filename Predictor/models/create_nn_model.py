from my_kmeans_nn import My_kmeans_nn
import pandas as pd


if __name__ == "__main__":
    spotify_df = pd.read_csv("../data/SpotifyFeatures.csv")
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
    spotify_df = spotify_df[important_features]


    MM = My_kmeans_nn(n_clusters=30, iteration_n=10)
    MM.fit(spotify_df)
    breakpoint()
    # for i in range(100):
    #     print(MM.predict(X.iloc[i]))