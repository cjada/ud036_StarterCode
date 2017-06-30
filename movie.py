class Movie():
	"""
	Create a movie object complete with a title, trailer, description, and a poster image
	"""
	def __init__(self, title, trailer_youtube_url, description, poster_image):
		self.title = title
		self.trailer_youtube_url = trailer_youtube_url
		self.description = description
		self.poster_image = poster_image


