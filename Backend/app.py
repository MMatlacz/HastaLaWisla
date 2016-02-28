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
	def __init__(self, identyfikator, nazwa, lat, longit, kategoria, opis, zdjecie_main, zdj1, zdj2, zdj3, cena, otwarcie, zamkniecie):
		self.identyfikator = identyfikator
		self.nazwa = nazwa					 #bez enterow!!!
		self.longitue = longit
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
		obj['latitude'] = self.latitude
		obj['longitue'] = self.longitue
		obj['zdjecie_main'] = photos_path + self.identyfikator + '/' + self.zdjecie_main
		obj['zdj1'] = photos_path + self.identyfikator + '/' + self.zdj1
		obj['zdj2'] = photos_path + self.identyfikator + '/' + self.zdj2
		obj['zdj3'] = photos_path + self.identyfikator + '/' + self.zdj3
		obj['cena'] = self.cena
		obj['otwarcie'] = self.otwarcie
		obj['zamkniecie'] = self.zamkniecie
		return obj
		#json.dumps(obj)

PomostOpis = 'Miejsce kreatywnego relaksu na Powiślu dla mieszkańców Warszawy i jej gości, strefa w której spotykają się różne środowiska, by wspólnie poimprezować i wypocząć. Atmosferę miejsca podgrzewa przyjemna muzyka nie zagłuszająca rozmów odpoczywających gości, a w weekendy mega imprezy dla wymagających klubowiczów. Pomost 511 to połączenie kulturalnej klubokawiarni i wodniackiego miejsca z przystanią na rzece i kameralną piaszczystą plażą.'
Pomost511 = Miejsce('Pomost511', 'Pomost 511', '52.229086', '21.0435052', 'Muzyka', PomostOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', 'Tanio', '13:00', '4:00')

PlazowaOpis = 'Plażowa / Pantai Warsaw / Miejskie Granie'
Plazowa = Miejsce('Plazowa', 'Plazowa',  '52.2378957', '21.0427988', 'Gastronomia', PlazowaOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', "Przystępnie", '11:00', '1:00')

Park_linowyOpis = 'Parki Linowy Warszawa to specjalnie przygotowany teren dla zabaw z użyciem lin. U nas bawić się mogą ludzie bez żadnego doświadczenia w tym kierunku, zarówno dzieci, młodzież jak i dorośli. Zapewniamy niezapomniane wrażenia, adrenalinę i zabawę na świeżym powietrzu. Proponujemy organizację urodzin dla dzieci, wieczorów panieńskich i kawalerskich. Imprezy integracyjne dla firm.'
Park_linowy = Miejsce('Park_linowy', 'Park linowy', '52.2546913', '21.0209791', 'Ruch', Park_linowyOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', "Przystępnie", '9:00', '23:00')

Wyspy_zawadowskieOpis = 'Na południu Warszawy znajduje się rezerwat Wyspy Zawadowskie. Zlokalizowany jest on na Wiśle w obrębie dwóch dzielnic: Wawra oraz Wilanowa. Obszar rezerwatu wykracza również poza granice Warszawy i zajmuje część gminy Konstancin - Jeziorna oraz miasta Józefów. Rezerwat został utworzony 23.12.1998 roku. Obszar chroniony ma powierzchnię 530,28 ha. Głównym celem powołania do życia rezerwatów była ochrona ekosystemów wodnych w obrębie koryta Wisły. Chroniony obszar jest miejscem gniazdowania wielu rzadkich i cennych gatunków ptaków, jak również stanowi ostoję zwierząt związanych ze środowiskiem wodnym.'
Wyspy_zawadowskie = Miejsce('Wyspy_zawadowskie', 'Wyspy Zawadowskie', '52.135795', '21.1838098', 'Natura', Wyspy_zawadowskieOpis, '0.jpg', '1.jpg', '2.jpg', '3.jpg', "Za darmo", '6:00', '23:00')

HockiKlockiOpis = "Założeniem klubu jest powrót do krainy dzieciństwa. Hocki Klocki znajdują się przy Bulwarze Flotylli Wiślanej, w niedalekim sąsiedztwie ulicy Ludnej.W otoczeniu drzew i z kawałkiem plaży- idealna przestrzeń do wakacyjnego relaksu."
HockiKlocki = Miejsce("HockiKlocki","Hocki Klocki","52.232311" ,"21.041103","Muzyka", HockiKlockiOpis,"0.jpg","1.jpg","2.jpg","3.jpg","Tanio","11:00","2:00")

CudNadWislaOpis = "Bez wahania można powiedzieć, że to Cud nad Wisłą zapoczątkował tradycję spędzania długich wieczorów przy zacnej muzyce nad samą rzeką. Cud jest z nami już od pięciu lat i ani myśli, mimo pojawiających się co roku mocnych konkurentów, wynosić znad Wisły."
CudNadWisla = Miejsce("CudNadWisla","Cud Nad Wisłą","52.228424", "21.044472","Muzyka", CudNadWislaOpis,"0.jpg","1.jpg","2.jpg","3.jpg","Tanio","15:00","2:00")

Plaza_z_ogniskamiOpis = 'Plaża miejska z kilkoma miejscami pod ogniska. Wspaniałe miejsce na wieczorne ognisko przy zachodzie słońca z widokiem na Stare Miasto.'
Plaza_z_ogniskami = Miejsce('Plaza_z_ogniskami', 'Plaża z Ogniskami', '52.2349795' , '21.0437078,19', 'Ogniska', Plaza_z_ogniskamiOpis, "0.jpg","1.jpg","2.jpg","3.jpg","Za darmo","0:01","23:59")

lista_miejsc = [Pomost511, Plazowa, Park_linowy, Wyspy_zawadowskie, HockiKlocki, CudNadWisla, Plaza_z_ogniskami]

java_table = []

for miejsce in lista_miejsc:
	java_table.append(miejsce.get_places())

#print json.dumps(java_table)


@app.route(app_url + '/places/')
def pmst():
	return json.dumps(java_table)




if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, app)
    httpd.serve_forever()

