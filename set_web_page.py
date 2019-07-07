#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='Joe')

@app.route('/receiver', methods = ['POST'])
def worker():
    # read json + reply
    print(request)
    data_cars = request.get_json(force=True)
    result = ''
    print(data_cars)
    for item in data_cars:
		# loop over every row
	    result += str(item['make']) + '\n'
    return result

if __name__ == '__main__':
	# run!
	app.run()
