#Import spacy and use "spacy.load('en_core_web_md')" for the comparison.
import spacy
nlp = spacy.load('en_core_web_md')
#This is going to define the initial movie.
starting_movie = "Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
#Open the document movies.txt to get the movie description
movies = open("movies.txt","r")

lines = movies.readlines()
#Creating a list to store what is being read from the document
movie_list = []
#Get the lines read and add it to the created list.
for line in lines:
    aux = line.strip()
    movie_list.append(aux)
#Close the document
movies.close
#Creating a function that will do the comparison and will give the best match for the next movie to watch.
def what_to_watch_next():

    model_movie = nlp(starting_movie)
    affinity = 0
    print("----------------------------------------------------------------------------------------------------------")
    '''With this loop for, I will check the similarity with the movie we want to compare
    and get the maximun value, labelled affinity'''
    for movie in movie_list:
        similarity = nlp(movie).similarity(model_movie)
        print(f"{movie}\nAffinity:\t{similarity}")
        if affinity < similarity:
            affinity = similarity
    print("----------------------------------------------------------------------------------------------------------")
    '''Once we got the maximun value, I will loop again to find that value again and print the
    movie description attached to it.'''
    for movie in movie_list:
        similarity = nlp(movie).similarity(model_movie)
        if affinity == similarity:
            movie_selected = movie
            
    print(f"Our next recomendation is:\n{movie_selected}")
    print("----------------------------------------------------------------------------------------------------------")

what_to_watch_next()
    
