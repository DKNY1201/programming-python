"""
Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
Example 2:

Input:
userSongs = {
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
},
songGenres = {}

Output: {
   "David": [],
   "Emma":  []
}
"""

import unittest


def calc_favorite_genres(user_songs, song_genres):
    res = {}

    for user in user_songs:
        res[user] = []

    if not song_genres:
        return res

    map_song_to_genres = {}
    for genre in song_genres:
        for song in song_genres[genre]:
            map_song_to_genres[song] = genre

    for user in user_songs:
        map_genre_to_listen_times = {}
        max_listen_times = float("-Inf")

        for song in user_songs[user]:
            genre = map_song_to_genres[song]
            listen_time = map_genre_to_listen_times.get(genre, 0)
            listen_time += 1
            map_genre_to_listen_times[genre] = listen_time
            max_listen_times = max(listen_time, max_listen_times)

        for genre, listen_time in map_genre_to_listen_times.items():
            if listen_time == max_listen_times:
                res[user].append(genre)

    return res


class Test(unittest.TestCase):
    def test_calc_favorite_genres(self):
        user_songs = {
            "David": ["song1", "song2", "song3", "song4", "song8"],
            "Emma": ["song5", "song6", "song7"]
        }

        song_genres = {
            "Rock": ["song1", "song3"],
            "Dubstep": ["song7"],
            "Techno": ["song2", "song4"],
            "Pop": ["song5", "song6"],
            "Jazz": ["song8", "song9"]
        }

        expected = {
            "David": ["Rock", "Techno"],
            "Emma": ["Pop"]
        }

        self.assertEqual(expected, calc_favorite_genres(user_songs, song_genres),
                         "Should return correct dict of user and theirs favorite songs")

        user_songs = {
            "David": ["song1", "song2"],
            "Emma": ["song3", "song4"]
        }

        song_genres = {}

        expected = {
            "David": [],
            "Emma": []
        }

        self.assertEqual(expected, calc_favorite_genres(user_songs, song_genres),
                         "Should return empty list of favorite songs if there is empty song_genres")
