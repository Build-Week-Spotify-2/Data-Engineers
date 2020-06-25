from Searcher.methods import methods
# from methods import methods


def search(query, limit):
    # breakpoint()
    spotipy_obj = methods.get_spotify_token()
    results = spotipy_obj.search(q=query, limit=limit)
    # breakpoint()
    results_df = methods.get_proper_dataframe(results)
    return results_df.to_dict()