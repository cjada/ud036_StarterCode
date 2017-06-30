import movie
import fresh_tomatoes

nemo = movie.Movie("Finding Nemo",
	"https://www.youtube.com/watch?v=wZdpNglLbt8",
	"A clown fish searches the ocean for his son",
	"Finding_Nemo.jpg")

office_space = movie.Movie("Office Space",
	"https://www.youtube.com/watch?v=dMIrlP61Z9s",
	"A corporate drone hates his job and stops caring",
	"office_space.jpg")

casino_royale = movie.Movie("Casino Royale",
	"https://www.youtube.com/watch?v=36mnx8dBbGE",
	"James Bond takes on a financier to terrorist organizations",
	"casino_royale.jpg")

no_country = movie.Movie("No Country For Old Men",
	"https://www.youtube.com/watch?v=38A__WT3-o0",
	"Llewelyn Moss discovers a suitcase full of money after a drug deal went bad.  Mayhem ensues.",
	"no_country.jpg")

blood = movie.Movie("There Will Be Blood",
	"https://www.youtube.com/watch?v=3PXf5iSGIL4",
	"Daniel Plainview strikes oil and becomes a ruthless tycoon.",
	"blood.jpg")

frozen = movie.Movie("Frozen",
	"https://www.youtube.com/watch?v=TbQm5doF_Uc",
	"Anna travels into the wilderness to find her sister Elsa, who has cast a spell over their town that causes it to be winter.",
	"frozen.jpg")

movies = [nemo, office_space, casino_royale, no_country, blood, frozen]


fresh_tomatoes.open_movies_page(movies)
