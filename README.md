# Data-Engineers
## Contains the Flask app that serves model predictions based on song id inputs
URL for this endpoint: [https://whispering-refuge-19940.herokuapp.com](https://whispering-refuge-19940.herokuapp.com)
### `.../predictions`
#### Request:
Feed this a POST request in the shape of json, it's 
looking for 2 fields:
 - `song_id_list:` an array of song id's as strings
 - `recommendation_count:` the requested number of 
```js
{
  "song_id_list":
  [
    "7FGq80cy8juXBCD2nrqdWU",
    "20hsdn8oITBsuWNLhzr5eh"
  ],
  "recommendation_count": 3
	
}
```

#### Response:
t will return json data with only the field `recommended_song_id_list:` followed by an array of song id's as strings
song outputs from the model

```js
[
  {
    "acousticness": 0.228,
    "album_image": "https://i.scdn.co/image/ab67616d0000b2736d5d2d5364c9ba375163e5ea",
    "artists": [
      "Chorus"
    ],
    "danceability": 0.684,
    "energy": 0.746,
    "instrumentalness": 0.0,
    "liveness": 0.196,
    "loudness": -5.847,
    "song_id": "3nGNIiz4PTsZ7cRhNNuSd2",
    "song_name": "Swami Samartha Majhe Aai",
    "speechiness": 0.0448,
    "tempo": 107.854,
    "valence": 0.745
  },
  {
    "acousticness": 0.0695,
    "album_image": "https://i.scdn.co/image/ab67616d0000b273ef7d21b6670eb2bad94301d6",
    "artists": [
      "Henri Salvador"
    ],
    "danceability": 0.425,
    "energy": 0.459,
    "instrumentalness": 0.0,
    "liveness": 0.21,
    "loudness": -6.648,
    "song_id": "25kL0XVBAcUR3Bc5iihs55",
    "song_name": "Adieu adios",
    "speechiness": 0.0326,
    "tempo": 108.288,
    "valence": 0.459
  }
]
```

I

---

### `.../songs`
Searches with the query "5 best songs" and displays what are evidently Spotify's 5 best songs (you may be surprised by the results)  
