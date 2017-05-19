import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
            This is the constructor method that is called
            in our entertainment.py file and makes a separate space in  memory
            for each movie variables we input
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
            Opening the webbrowser with the correct URL.
        """
        webbrowser.open(self.trailer_youtube_url)
