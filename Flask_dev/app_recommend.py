import pandas as pd
import numpy as np
from flask import Flask
import os

path0=os.path.abspath(os.path.dirname(__file__))
file_0=os.path.join(path0, 'movie_title.csv')
file_1=os.path.join(path0, 'movies_indices_neighbors.csv')
df_movie_title = pd.read_csv(file_0, index_col=0)
df_movie_rec = pd.read_csv(file_1, index_col=0).values

app = Flask(__name__) # Creer app et charger les fonctionalités de Flask


def similar_movies_knn(id):
   
    if id not in df_movie_rec:
        return "error: This movie is not found"
    
    dict_movie = {}
    for id in df_movie_rec[id]: 
        
        dict_movie[id]=df_movie_title.iloc[id]['movie_title']
    return  'The movie chosen and the 5 similar ones:', dict_movie
             
        

@app.route('/recommend/<int:id>', methods=['GET']) # Décorateur,page d'acceuil, executer la fonction ci-desous aprés, http://127.0.0.1:2000/ (Associer l'URL à une fonction) 
def recommendation (id):
    movies = similar_movies_knn(id)
    return str(movies)

if __name__== '__main__': #Executer directement
    app.run(debug=True, port=6060) #Lancer le serveur local (localhost/adresse ip 127.0.0.1)

