import fresh_tomatoes
import media

""" Creating a movie objects and passing the arguments like
movie title,poster url and youtube link to Movie class which
is present in media file."""
kung_fu_panda = media.Movie(
    "Kung fu panda",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
    "https://www.youtube.com/watch?v=PXi3Mv6KMzY")


How_To_Train_Your_Dragon = media.Movie(
    "How To Train Your Dragon",
    "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_"
    "Dragon_Poster.jpg",
    "https://www.youtube.com/watch?v=oKiYuIsPxYk")


The_Fault_In_Our_Stars = media.Movie(
    "The Fault In Our Stars",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/The_Fault_in_Our_"
    "Stars_%28Official_Film_Poster%29.png/220px-The_Fault_in_Our_Stars_%"
    "28Official_Film_Poster%29.png",
    "https://www.youtube.com/watch?v=9ItBvH5J6ss")

The_Avengers = media.Movie(
    "The Avengers",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")
Spider_Man_Homecoming = media.Movie(
    "Spider Man: Homecoming",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Spider-Man_"
    "Homecoming_poster.jpg/220px-Spider-Man_Homecoming_poster.jpg",
    "https://www.youtube.com/watch?v=xrzXIaTt99U")

Boss_Baby = media.Movie(
    "Boss Baby",
    "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
    "https://www.youtube.com/watch?v=h24gEn3y82Q")
# Creating a list(movies) which contains all the movies details.
movies = [kung_fu_panda, How_To_Train_Your_Dragon, The_Fault_In_Our_Stars,
          The_Avengers, Spider_Man_Homecoming, Boss_Baby]
fresh_tomatoes.open_movies_page(movies)
