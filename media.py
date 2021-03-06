class Movie():

    # Constructor for Movie class. Initializes variables for movie title,
    # storyline, poster image URL, trailer URL, rating, and IMDB page URL.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating, imdb_page):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.imdb_url = imdb_page
