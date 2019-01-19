import media
import fresh_tomatoes

# Instances of Movies
harry_potter_1 = media.Movie("Harry Potter and the Sorcerer's Stone",
                             "An 11 year old boy learns that he is a wizard.",
                             "https://upload.wikimedia.org/wikipedia/en/7/7a/Harry_Potter_and_the_Philosopher%27s_Stone_banner.jpg",
                             "https://www.youtube.com/watch?v=PbdM1db3JbY")

pirates_1 = media.Movie("Pirates of the Caribbean: The Curse of the Black Pearl",
                        "A pirate and a blacksmith rescue a kidnapped woman from the cursed crew of the Black Pearl.",
                        "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
                        "https://www.youtube.com/watch?v=miuoza1nals")

star_wars_4 = media.Movie("Star Wars Episode IV: A New Hope",
                          "The Rebel Alliance attempts to destroy the Galactic Empire's Death Star.",
                          "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                          "https://www.youtube.com/watch?v=yYNSSNJ0z_U")

avengers = media.Movie("Marvel's The Avengers",
                       "S.H.I.E.L.D. recruits Tony Stark, Captain America, the Hulk, and Thor to form a team that must stop Loki from subjugating Earth.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

guardians = media.Movie("Guardians of the Galaxy Vol. 1",
                        "Peter Quill forms an alliance with a group of extraterrestrial criminals who are fleeing after stealing a powerful artifact.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",
                        "https://www.youtube.com/watch?v=d96cjJhvlMA")

lord_of_the_rings_1 = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                                  "The Fellowship of the Ring begin their journey to Mount Doom to destroy the One Ring.",
                                  "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                                  "https://www.youtube.com/watch?v=rAUJN48IHXw")

hunger_games = media.Movie("The Hunger Games",
                           "A girl takes her sister's place in the Hunger Games, an elaborate televised fight to the death.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=nvU1MnB_dAc")

# creates an array of movie objects
movies = [harry_potter_1, pirates_1, star_wars_4, avengers, guardians, lord_of_the_rings_1, hunger_games]

fresh_tomatoes.open_movies_page(movies)
