from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import os
import sys
from datetime import datetime
from flask_app.forms import SearchForm, ChampionNoteForm
from flask_app.model import ChampionClient

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://mchin18:HuaiYu1738@cluster0.myuyw.mongodb.net/Week4?retryWrites=true&w=majority&appName=Cluster0' 
app.config['SECRET_KEY'] = os.urandom(16)
#OMDB_API_KEY = '6df90dc1' 
# DO NOT REMOVE OR MODIFY THESE 4 LINES (required for autograder to work)
if os.getenv('MONGO_URI'):
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
#if os.getenv('OMDB_API_KEY'):
    #OMDB_API_KEY = os.getenv('OMDB_API_KEY')

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

mongo = PyMongo(app)
champion_client = ChampionClient()

# --- Do not modify this function ---
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for('query_results', query=form.search_query.data))

    return render_template('index.html', form=form)

@app.route('/search-results/<query>', methods=['GET'])
def query_results(query):
    results = champion_client.search(query)
    return render_template('query_results.html', query=query, results=results)

@app.route('/champions/<champion_id>', methods=['GET', 'POST'])
def champion_detail(champion_id):
    champion = champion_client.retrieve_champion_by_id(champion_id)
    form = ChampionNoteForm()
    print("IMAGE URL:", champion.image_url, file=sys.stderr)
    if form.validate_on_submit():
        note = {
            'champion_id': champion_id,
            'commenter': form.name.data,
            'content': form.text.data,
            'date': current_time()
        }
        mongo.db.notes.insert_one(note)
        return redirect(url_for('champion_detail', champion_id=champion_id))
    
    notes = list(mongo.db.notes.find({'champion_id': champion_id}))
    labels = ['Attack', 'Defense', 'Magic', 'Difficulty']
    values = [
        champion.stats['attack'],
        champion.stats['defense'],
        champion.stats['magic'],
        champion.stats['difficulty'],
    ]
    stat_pairs = zip(labels, values)

    return render_template(
        'champion_detail.html',
        champion=champion,
        form=form,
        notes=notes,
        stat_pairs=stat_pairs
    )

@app.route('/champions')
def champion_directory():
    #print("Loading all champions...") 
    champions = champion_client.get_all_champions()
    return render_template('champion_directory.html', champions=champions)

# Not a view function, used for creating a string for the current time.
def current_time() -> str:
    return datetime.now().strftime('%B %d, %Y at %H:%M:%S')