from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pd.read_csv('Books.csv', low_memory=False)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           image=popular_df['Image-URL-M'].to_list(),
                           book_name=popular_df['Book-Title'].to_list(),
                           author=popular_df['Book-Author'].to_list(),
                           votes=popular_df['num-ratings'].to_list(),
                           ratings=popular_df['avg_rating'].to_list()
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    ind = np.where(pt.index == user_input)[0][0]
    same_sc = cosine_similarity(pt)
    similar_items = sorted(list(enumerate(same_sc[ind])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Title'].to_list())
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Author'].to_list())
        item.extend(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].to_list())

        data.append(item)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
