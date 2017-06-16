import fresh_tomatoes
import media

# Instances of the mocie class
age_of_ultron = media.Movie("Age of Ultron", "http://ia.media-imdb.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@", "https://www.youtube.com/watch?v=tmeOjFno6Do")
civil_war = media.Movie("Civil War", "http://ia.media-imdb.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@", "https://www.youtube.com/watch?v=dKrVegVI0Us")
the_winter_soldier = media.Movie("The Winter Soldier", "http://ia.media-imdb.com/images/M/MV5BMzA2NDkwODAwM15BMl5BanBnXkFtZTgwODk5MTgzMTE@", "https://www.youtube.com/watch?v=7SlILk2WMTI")
dawn_of_justice = media.Movie("Dawn of Justice", "http://ia.media-imdb.com/images/M/MV5BNTE5NzU3MTYzOF5BMl5BanBnXkFtZTgwNTM5NjQxODE@", "https://www.youtube.com/watch?v=IwfUnkBfdZ4")
man_of_steel = media.Movie("Man of Steel", "http://ia.media-imdb.com/images/M/MV5BMjI5OTYzNjI0Ml5BMl5BanBnXkFtZTcwMzM1NDA1OQ@@", "https://www.youtube.com/watch?v=T6DJcgm3wNY")
guardians = media.Movie("Guardians of the Galaxy", "https://image.tmdb.org/t/p/w185/9gm3lL8JMTTmc3W4BmNMCuRLdL8.jpg", "https://www.youtube.com/watch?v=crIaEzXgqto,2014")

#Joining them together in a list
movies = [age_of_ultron, civil_war, the_winter_soldier, dawn_of_justice, man_of_steel, guardians]

#Create and Open the movies page
fresh_tomatoes.open_movies_page(movies)