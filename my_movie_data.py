import fresh_tomatoes_1
import media

#title
#date
#director
#tagline
#poster
#trailer


big_lebowski = media.Movie(
	"The Big Lebowski",
	"1998",
	"Joel Coen, Ethan Coen",
	"Her life was in their hands.<br>Now her toe is in the mail.",
	"https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
	"https://www.youtube.com/watch?v=cd-go0oBF4Y"
	)
	
buck = media.Movie(
	"Buck",
	"2011",
	"Cindy Meehl",
	"There&#146;s no wisdom worth having that isn&#146;t hard&nbsp;won",
	"https://upload.wikimedia.org/wikipedia/en/8/84/Buckthefilm.jpg",
	"https://www.youtube.com/watch?v=IShjmWYuHZ0"
	)
	
sweetgrass = media.Movie(
	"Sweetgrass",
	"2009",
	"Ilisa Barbash, Lucien&nbsp;Castaing-Taylor",
	"The Last Ride of the American&nbsp;Cowboy",
	"https://upload.wikimedia.org/wikipedia/en/6/62/SweetgrassPoster.jpg",
	"https://www.youtube.com/watch?v=AV9iah71iPQ"
	)
	
kiss_kiss = media.Movie(
	"Kiss Kiss Bang&nbsp;Bang",
	"2005",
	"Shane Black",
	"SeX. MurdEr. MyStery.<br>Welcome to the party.",
	"https://upload.wikimedia.org/wikipedia/en/6/61/Kiss_kiss_bang_bang_poster.jpg",
	"https://www.youtube.com/watch?v=__PnD1HWXSo"
	)
	
she_devil = media.Movie(
	"She-Devil",
	"1989",
	"Susan Seidelman",
	"Revenge Is Sweet&#133;And Low.",
	"https://upload.wikimedia.org/wikipedia/en/6/63/Shedevil.jpg",
	"https://www.youtube.com/watch?v=Nm4c5L9sWD8"
	)
	
fright_night_1985 = media.Movie(
	"Fright Night",
	"1985",
	"Tom Holland",
	"&#133;it&#146;ll be the night of your&nbsp;life.",
	"https://upload.wikimedia.org/wikipedia/en/e/e2/Fright_night_poster.jpg",
	"https://www.youtube.com/watch?v=1ISgM9sjza8"
	)
	
fright_night_2011 = media.Movie(
	"Fright Night",
	"2011",
	"Craig Gillespie",
	"You can&#146;t run from evil when it lives next&nbsp;door.",
	"https://upload.wikimedia.org/wikipedia/en/9/9b/FrightNight2011Poster.jpg",
	"https://www.youtube.com/watch?v=sUipgKdTi_k"
	)
	
inside_out = media.Movie(
	"Inside Out",
	"2015",
	"Pete Docter, Ronnie&nbsp;Del&nbsp;Carmen",
	"Meet the little voices inside your&nbsp;head.",
	"https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
	"https://www.youtube.com/watch?v=_MC3XuMvsDI"
	)
	
troll_hunter = media.Movie(
	"Troll Hunter",
	"2010",
	"Andr&eacute; Ovredal",
	"You believe it when you see&nbsp;it!",
	"https://upload.wikimedia.org/wikipedia/en/1/1e/TrollHunter.jpg",
	"https://www.youtube.com/watch?v=uvwEyHeRSvE"
	)
	
spinal_tap = media.Movie(
	"This is Spinal Tap",
	"1984",
	"Rob Reiner",
	"Does for rock and roll what &quot;The Sound of Music&quot; did for&nbsp;hills",
	"https://upload.wikimedia.org/wikipedia/en/c/c8/Thisisspinaltapposter.jpg",
	"https://www.youtube.com/watch?v=N63XSUpe-0o"
	)
	
theatre_of_blood = media.Movie(
	"Theatre of Blood",
	"1973",
	"Douglas Hickox",
	"It&#146;s curtains for his critics!",
	"https://upload.wikimedia.org/wikipedia/en/0/0d/Theatreofbloodposter.jpg",
	"https://www.youtube.com/watch?v=lGcT8gFzH14"
	)
	
love_and_death = media.Movie(
	"Love and Death",
	"1975",
	"Woody Allen",
	"If He&#146;s gonna test us, why doesn&#146;t He give us a written?",
	"https://upload.wikimedia.org/wikipedia/en/7/73/Love_and_death.jpg",
	"https://www.youtube.com/watch?v=pbk9YFxRDqE"
	)


	


movies = [
	big_lebowski,
	buck,
	sweetgrass,
	kiss_kiss,
	she_devil,
	fright_night_1985,
	fright_night_2011,
	inside_out,
	theatre_of_blood,
	troll_hunter,
	spinal_tap,
	love_and_death
	]
	
fresh_tomatoes_1.open_movies_page(movies)


