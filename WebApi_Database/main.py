import flask
from flask import jsonify, request, render_template
import sqlite3
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return "<h1>Biblioteca online</h1>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    database = sqlite3.connect('db/books.db')   
    c = database.cursor()
    c.execute("SELECT * FROM books ORDER BY year_published")    
    all_books = c.fetchall()    
    return jsonify(all_books)  
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    database = sqlite3.connect('db/books.db')
    c = database.cursor()
    print(request.args) 
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Errore: Non è stato immesso alcun id"

    c.execute(f"SELECT * FROM books WHERE id LIKE '{id}'")  
    book = c.fetchall()

    return jsonify(book) 


@app.route('/api/v1/addBook', methods=['GET'])
def api_create():
    query_parameters = request.args

    title = query_parameters.get('title')
    author = query_parameters.get('author')
    year_published = query_parameters.get('year_published')

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('INSERT INTO Biblioteca(title,author,year_published) VALUES(?,?,?)', (title, author, year_published,))
    conn.commit() 

    conn.close()

    return '<h1>Dati aggiunti con successo!</h1><p>Clicca per vedere: http://127.0.0.1:5000/api/v1/resources/books/all</p>'


app.run()