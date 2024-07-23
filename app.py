from flask import Flask, render_template, request, url_for, redirect
import csv
import pandas as pd
from csv_search import db_search

df = pd.read_csv(r"urhobo-dictionary.csv")

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def search_result():
	data = db_search(request.form['phrase'])
	#find way to search csv file
	return render_template('search-result.html', specific=data['specific'], non_specific=data['non_specific'])

	
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)
