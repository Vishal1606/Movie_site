import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of a boy and toys that comes alive",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https:www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
  
avatar = media.Movie("Avtar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/bO/Avatar-Teaser-Post",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School of rock","using rock movie to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille","A rat is chief in paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in paris", "Going back in time to meet the author",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger games","A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7HObo")

movies =[toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)

