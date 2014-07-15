#!/usr/bin/python

from bottle import route, run, template, error, static_file, template
staticDir = '/path/to/extract_image/web/static/'
@route('/')
@route('/secret.html')
def index():
	#First, open and parse the file:
	namesFile = open('fNameFile.txt', 'r')
	#Parse:
	files = []
	for line in namesFile:
		fileArr = line.split(', ')
		fileArr.pop()
		files.append(fileArr)
	return template('page', imageGrid=files)

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root=staticDir)

@error('404')
def error404(error):
	return 'Error: you have attempted to see the wrong secret things.'

run(host='localhost', port=8080)
#run(host='localhost', port=8080, reloader=True, debug=True)
