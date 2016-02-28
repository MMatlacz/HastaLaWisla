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
	def __init__(self, identyfikator, nazwa, longit, lat, kategoria, opis, zdjecie_main, zdj1, zdj2, zdj3, cena, otwarcie, zamkniecie):
		self.identyfikator = identyfikator
		self.nazwa = nazwa					 #bez enterow!!!
		self.longitude = longit
		self.latitude = lat
		self.kategoria = kategoria		 	#string {natura, ruch, gastronomia, muzyka}
		self.opis = opis
		self.otwarcie = otwarcie
		self.zamkniecie = zamkniecie
		self.zdjecie_main = zdjecie_main	#wszystkie zdjecia to tak naprawde sciezki z /img/
		self.zdj1 = zdj1
		self.zdj2 = zdj2
		self.zdj3 = zdj3
		self.cena = cena

	def get_places(self):
		obj = {}
		obj['identyfikator'] = self.identyfikator
		obj['nazwa'] = self.nazwa
		obj['kategoria'] = self.kategoria
		obj['opis'] = self.opis
		obj['longitue'] = self.longitude
		obj['latitude'] = self.latitude
		obj['zdjecie_main'] = photos_path + self.nazwa + '/' + self.zdjecie_main
		obj['zdj1'] = photos_path + self.nazwa + '/' + self.zdj1
		obj['zdj2'] = photos_path + self.nazwa + '/' + self.zdj2
		obj['zdj3'] = photos_path + self.nazwa + '/' + self.zdj3
		obj['cena'] = self.cena
		obj['otwarcie'] = self.otwarcie
		obj['zamkniecie'] = self.zamkniecie

		return json.dumps(obj)

PomostOpis = 'Miejsce kreatywnego relaksu na Powiślu dla mieszkańców Warszawy i jej gości, strefa w której spotykają się różne środowiska, by wspólnie poimprezować i wypocząć. Atmosferę miejsca podgrzewa przyjemna muzyka nie zagłuszająca rozmów odpoczywających gości, a w weekendy mega imprezy dla wymagających klubowiczów. Pomost 511 to połączenie kulturalnej klubokawiarni i wodniackiego miejsca z przystanią na rzece i kameralną piaszczystą plażą.'
Pomost511 = Miejsce('sdlfkj', 'Pomost 511', '52.229086', '21.0435052', 'Muzyka', PomostOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', 1, '13:00', '4:00')

PlazowaOpis = 'Plażowa / Pantai Warsaw / Miejskie Granie'
Plazowa = Miejsce('Plz', 'Plazowa',  '52.2378957', '21.0427988', 'Gastronomia', PlazowaOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', 2, '11:00', '1:00')

Park_linowyOpis = 'Parki Linowy Warszawa to specjalnie przygotowany teren dla zabaw z użyciem lin. U nas bawić się mogą ludzie bez żadnego doświadczenia w tym kierunku, zarówno dzieci, młodzież jak i dorośli. Zapewniamy niezapomniane wrażenia, adrenalinę i zabawę na świeżym powietrzu. Proponujemy organizację urodzin dla dzieci, wieczorów panieńskich i kawalerskich. Imprezy integracyjne dla firm.'
Park_linowy = Miejsce('Prklnw', 'Park linowy', '52.2546913', '21.0209791', 'Ruch', Park_linowyOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', 2, '9:00', '23:00')

Wyspy_zawadowskieOpis = 'Na południu Warszawy znajduje się rezerwat Wyspy Zawadowskie. Zlokalizowany jest on na Wiśle w obrębie dwóch dzielnic: Wawra oraz Wilanowa. Obszar rezerwatu wykracza również poza granice Warszawy i zajmuje część gminy Konstancin - Jeziorna oraz miasta Józefów. Rezerwat został utworzony 23.12.1998 roku. Obszar chroniony ma powierzchnię 530,28 ha. Głównym celem powołania do życia rezerwatów była ochrona ekosystemów wodnych w obrębie koryta Wisły. Chroniony obszar jest miejscem gniazdowania wielu rzadkich i cennych gatunków ptaków, jak również stanowi ostoję zwierząt związanych ze środowiskiem wodnym.'
Wyspy_zawadowskie = Miejsce('WspZdwk', 'Wyspy Zawadowskie', '52.135795', '21.1838098', 'Natura', Wyspy_zawadowskieOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', 0, '6:00', '23:00'


@app.route(app_url + '/places/pomost511')
def pmst():
	return Pomost511.get_places()

@app.route(app_url + '/places/plazowa')
def plzw():
	return Plazowa.get_places()

@app.route(app_url + '/places/park_linowy')
def prkln():
	return Park_linowy.get_places()

@app.route(app_url + '/places/wyspy_zawadowskie')
def wspzwdsk():
	return Wyspy_zawadowskie.get_places()



if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, app)
    httpd.serve_forever()
