import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.toystory",
                        "youtube_trailer")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "An avatar of a boy and his toys that come to life",
                        "http://www.avatar",
                        "youtube_trailer")
#print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
