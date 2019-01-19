import webbrowser


"""
The Movie Class contains the constructor for a
movie object and necessary  functionality to
display the trailer of the movie
"""


class Movie():

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image_url,
                 trailer_youtube_url):
        """
           Constructor of the Movie objet
           Args:
               self(Movie):
               movie_title(string): the title of the movie
               movie_storyline(string): description of the movie
               poster_image_url(string): url of movie poster
               trailer_youtube_url(string): url of movie trailer
                                            on youtube
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
