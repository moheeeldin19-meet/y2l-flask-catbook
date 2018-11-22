from flask import Flask, request
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_details(id):
	cat = get_cat(id)
	return render_template("cat.html",cat=cat)


@app.route('/create_cats')
def catbook_create():
    if request.method=='GET':
		return render_template('create_cats.html')
    else :
    	cat_name =request.form('name')
    	create_cats(cat_name)
if __name__ == '__main__':
   app.run(debug = True)
