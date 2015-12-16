import webbrowser


class Movie():
    def __init__(self, movie_title, movie_date, movie_director, movie_tagline,
                 poster_image, trailer_youtube):
        """
        Initializes the class "Movie" to have the (above) attributes
        """
        self.title = movie_title
        self.date = movie_date
        self.director = movie_director
        self.tagline = movie_tagline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Define show_trailer function to open browser and show trailer
        for each instance of class Movie
        """
        webbrowser.open(self.trailer_youtube_url)
