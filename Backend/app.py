#!/usr/bin/env python
# -*- coding: utf-8 -

import json

from wsgiref import simple_server

from flask import Flask

app_url = ''
app = Flask(__name__)
app.debug = True

photos_path = './photos/'

class Miejsce:
	def __init__(self, identyfikator, nazwa,lokalizacja, zdjecie_main, kategoria, opis, dodatkowe_parametry):
		self.identyfikator = identyfikator
		self.nazwa = nazwa
		self.lokalizacja = lokalizacja
		self.zdjecie_main = zdjecie_main
		self.kategoria = kategoria
		self.opis = opis
		self.dodatkowe_parametry = dodatkowe_parametry


	def get_places(self):
		obj = {}
		obj['identyfikator'] = self.identyfikator
		obj['nazwa'] = self.nazwa
		obj['lokalizacja'] = self.lokalizacja
		obj['zdjecie_main'] = photos_path + self.nazwa + '/' + self.zdjecie_main
		obj['kategoria'] = self.kategoria
		obj['opis'] = self.opis
		if 	self.dodatkowe_parametry != '':
			obj['dodatkowe_parametry'] = self.dodatkowe_parametry
		else:
			pass

		return json.dumps(obj)

Warszawa = Miejsce('XYZ', 'Warszawa', '52:21', 'zdjecie.jpg', 'Miasto', 'NaszeMiasto', '')
Cypel = Miejsce('sdu73f', 'Cypel', '52:21', 'zdjecie.jpg', 'picie', 'Troche nieleglane miejsce...', '')

@app.route(app_url + '/places/warszawa')
def wawa():
	return Warszawa.get_places()

@app.route(app_url + '/places/cypel')
def cypel():
	return Cypel.get_places()



if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, app)
    httpd.serve_forever()

