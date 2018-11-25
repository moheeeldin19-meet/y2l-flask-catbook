from flask import Flask, request
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>',methods=['GET','POST'])
def cat_details(id):
	if request.method== "GET":
		cat = get_cat(id)
		return render_template("cat.html",cat=cat)
	else:
		vote=get_vote(id)
		return redirect("/")


@app.route('/create_cats',methods=["GET",'POST'])
def catbook_create():
    if request.method=='GET':
		return render_template('create_cats.html')
    else :
    	name =request.form.getlist('name')
    	create_cat(name,0)
    	return redirect("/")
if __name__ == '__main__':
   app.run(debug = True)
