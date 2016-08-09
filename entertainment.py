import media
import fresh_tomatoes

Toy= media.Movie("Toy Story",
                 "The movie is about a boy and his toys",
                 "http://images.m-magazine.com/uploads/posts/image/46533/toy-story-hotel.jpg",
                 "https://www.youtube.com/watch?v=JcpWXaA2qeg")
print(Toy.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.idg.bg/wp-content/uploads/2016/07/Avatar-2009-Film.jpg?4762b9",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)

Znmd= media.Movie("Znmd",
                  "3 Friends road trip in spain",
                  "https://www.google.com/search?q=znmd&espv=2&biw=1366&bih=599&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi6ra2_u7POAhWK6yYKHVPOCaIQ_AUIBygC&dpr=1#imgrc=Kck9Kkk45Ne4DM%3A",
                  "https://www.youtube.com/watch?v=FJrpcDgC3zU")

#Znmd.show_trailer()
#avatar.show_trailer()
movies = [toy, avatar, znmd ]
fresh_tomatoes.open_movie_page(movies)
