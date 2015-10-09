import fresh_tomatoes
import media

black_mass = media.Movie("Black Mass", "While his brother Bill (Benedict Cumberbatch) remains a powerful leader in the Massachusetts Senate, Irish hoodlum James (Whitey) Bulger (Johnny Depp) continues to pursue a life of crime in 1970s Boston. Approached by FBI agent John Connolly (Joel Edgerton), the lawman convinces Whitey to help the agency fight the Italian mob. As their unholy alliance spirals out of control, Bulger increases his power and evades capture to become one of the most dangerous gangsters in U.S. history.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c0/Black_Mass_%28film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=R_F-lVhSfx8")

#print(black_mass.storyline)

the_martian = media.Movie("The Martian", "When astronauts blast off from the planet Mars, they leave behind Mark Watney (Matt Damon), presumed dead after a fierce storm. With only a meager amount of supplies, the stranded visitor must utilize his wits and spirit to find a way to survive on the hostile planet. Meanwhile, back on Earth, members of NASA and a team of international scientists work tirelessly to bring him home, while his crew mates hatch their own plan for a daring rescue mission.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI")

#print(the_martian.storyline)

sicario = media.Movie("Sicario", "After rising through the ranks of her male-dominated profession, idealistic FBI agent Kate Macer (Emily Blunt) receives a top assignment. Recruited by mysterious government official Matt Graver (Josh Brolin), Kate joins a task force for the escalating war against drugs. Led by the intense and shadowy Alejandro (Benicio Del Toro), the team travels back-and-forth across the U.S.-Mexican border, using one cartel boss (Bernardo Saracino) to flush out a bigger one (Julio Cesar Cedillo).",
                      "https://upload.wikimedia.org/wikipedia/en/4/4b/Sicario_poster.jpg",
                      "https://www.youtube.com/watch?v=sR0SDT2GeFg")

#print(sicario.storyline)

the_good_dinosaur = media.Movie("The Good Dinosaur", "A young dinosaur (Raymond Ochoa) named Arlo develops an unlikely friendship with a boy.",
                                "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
                                "https://www.youtube.com/watch?v=daFnEiLEx70")

#print(the_good_dinosaur.storyline)


star_wars = media.Movie("Star Wars: The Force Awakens", "The further adventures of Luke Skywalker (Mark Hamill), Han Solo (Harrison Ford) and Princess Leia (Carrie Fisher).",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Star_Wars_The_Force_Awakens_Teaser_Poster.jpg/220px-Star_Wars_The_Force_Awakens_Teaser_Poster.jpg",
                        "https://www.youtube.com/watch?v=OMOVFvcNfvE")


legend = media.Movie("Legend", "Identical twin gangsters Ronald and Reginald Kray terrorize London during the 1950s and 1960s.",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcQD8GqQY23eo1dTlHCnQa3v0hUgIiJ5yHpWBJ1S19ji-WOVG_TE",
                     "https://www.youtube.com/watch?v=yI3v6KfR9Mw")


movies = [black_mass, the_martian, sicario, the_good_dinosaur, star_wars, legend]
fresh_tomatoes.open_movies_page(movies)
