# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO fact_songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
""")

user_table_insert = ("""
INSERT INTO dim_users (user_id, first_name, last_name, gender, level)
VALUES (?, ?, ?, ?, ?);
""")

song_table_insert = ("""
INSERT INTO dim_songs (song_id, title, artist_id, year, duration)
VALUES (?, ?, ?, ?, ?);
""")

artist_table_insert = ("""
INSERT INTO dim_artists (artist_id, name, location, latitude, longitude)
VALUES (?, ?, ?, ?, ?);
""")


time_table_insert = ("""
INSERT INTO dim_time (start_time, hour, day, week, month, year, weekday)
VALUES (?, ?, ?, ?, ?, ?, ?);
""")

# FIND SONGS

song_select = ("""
SELECT song_id, songs.artist_id FROM dim_songs 
JOIN dim_artists ON artists.artist_id = songs.artist_id
WHERE title = ?
AND name = ?
AND duration = ?;
""")

