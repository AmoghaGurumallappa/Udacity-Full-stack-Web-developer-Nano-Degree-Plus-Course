import fresh_tomatoes
import media


Toy= media.Movie("Toy Story",
                 "The movie is about a boy and his toys",
                 "http://images.m-magazine.com/uploads/posts/image/46533/toy-story-hotel.jpg",
                 "https://www.youtube.com/watch?v=JcpWXaA2qeg")
#print(Toy.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.idg.bg/wp-content/uploads/2016/07/Avatar-2009-Film.jpg?4762b9",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

Znmd= media.Movie("Znmd",
                  "3 Friends road trip in spain",
                  "http://www.indicine.com/images/gallery/bollywood/movies/running-with-the-bulls/49280-znmd2-large.jpg",
                  "https://www.youtube.com/watch?v=FJrpcDgC3zU")

Om = media.Movie("Om",
                 "Story based on underworld",
                 "http://image6.buzzintown.com/files/movie/upload_20000/upload_original/540269-om-kannada.jpg",
                 "https://www.youtube.com/watch?v=wZNSEBgIjjA")

shivaji = media.Movie("Shvaji",
                      "Fighting against corruption",
                      "https://i.ytimg.com/vi/II6b066lD9k/maxresdefault.jpg",
                      "https://www.youtube.com/watch?v=8nh_aDr3aK0")
Lagaan = media.Movie("Lagaan",
                     "Playing cricket, a sport completely foreign to India to avoid tax",
                     "http://static.rogerebert.com/uploads/movie/movie_poster/lagaan-once-upon-a-time-in-india-2002/large_rtn5EYKMrnRE88JlxciRgzjbDgk.jpg",
                     "https://www.youtube.com/watch?v=oSIGQ0YkFxs")

#Znmd.show_trailer()
#avatar.show_trailer()
movies = [Toy, avatar, Znmd, Om, shivaji, Lagaan]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
