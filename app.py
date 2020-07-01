from flask import Flask, render_template, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommendation', methods=['POST','GET'])
def recommendation():
    if request.method == 'POST':
        name = request.form['imdb']
        x = name.lower()
        cosScore = cosine_similarity(matrix)
        movies = pd.Series(df['name'].str.lower())
        if x in movies.tolist():
            def imdb(name, cosScore = cosScore):
                idx = movies[movies == name].index[0]
                similar = list(enumerate(cosScore[idx]))  
                similar = sorted(similar, key=lambda x: x[1], reverse=True)
                similar = similar[1:11]
                recommendation = [i[0] for i in similar]
                return df.iloc[recommendation]
        
            movie = imdb(x)

            return render_template('recommendation.html', name = name, movie = movie)

        else:
            return render_template('error.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    matrix = joblib.load('modelJoblib') 
    df = pd.read_csv('movies_cleaned.csv')
    app.run(debug=True)