class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    _song_objects = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    
        Song._song_objects.append(self)


        Song.add_song_to_count()

        Song.genres.append(genre)
        Song.artists.append(artist)

        Song.genres = list(set(Song.genres))
        Song.artists = list(set(Song.artists))

        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {}
        for song in cls._song_objects:
            genre = song.genre
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {}
        for song in cls._song_objects:
            artist = song.artist
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
