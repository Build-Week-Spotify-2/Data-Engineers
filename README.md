# Data-Engineers
## Contains the Flask app that serves model predictions based on song id inputs

### `/predictions`
Feed this a POST request in the shape of json, it's looking for 2 fields:
 - `song_id_list:` an array of song id's as strings
 - `recommendation_count:` the requested number of song outputs from the model

It will return json data with only the field `recommended_song_id_list:` followed by an array of song id's as strings

---

### `/songs`
Searches with the query "5 best songs" and displays what are evidently Spotify's 5 best songs (you may be surprised by the results)  
