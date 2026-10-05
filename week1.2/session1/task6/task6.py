# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
favorite_music = { 
    "name": "Love Confession",
    "singer": "Jay Chou",
    "Songwriter": "Vincent Fang",
    "album":  "Jay Chou's Bedtime Stories",
    "release_year": 2016,
    "genre": "Pop R&B",
    "duration": "3:36",
    "rating": "9.5"
} 

# Pretty-print the data structure
pprint(favorite_music)

# Display details of one album recorded by a specific artist
v = favorite_music["album"]
print(v)