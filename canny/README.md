# Kenijev filtar

- Polaznik: Miša Dobrota
- Saradnici: Pavle Pađin (priprema), Anđela Bogdanović (mentor)

## Uvod

Detekcija ivica je bitan problem u obradi slike. Jedan standardni
algoritam koji se koristi za rešavanje ovog problema jeste *Canny*
filtar. Prednost ovog algoritma u odnosu na alternative je što je
otporan na šum i dobar je u odbacivanju lažnih ivica. Ideja ovog
projekta je da se od nule implementira filtar.

## Postupak razvoja

1. Primeniti Gausov filtar za uklanjanje šuma nad originalnom slikom. Nije dozvoljeno korišćenje bibliotečkih funkcija, već je potrebno samostalno implementirati Gausov filtar.
2. Potrebno je prvo implementirati Sobelov filtar za detekciju horizontalnih i vertikalnih gradijenata, a onda od dobijenih slika kreirati slike intenziteta i uglova gradijenata. Nije dozvoljeno korišćenje bibliotečkih funkcija.
3. Potrebno je odraditi kvantizaciju gradijenata pomoću uglova, te onda implementirati potiskivanje lokalnih ne-maksimuma. Takođe nije dozvoljeno korišćenje bibliotečkih funkcija.
4. Potrebno je odrediti slabe i jake ivice. Slabe ivice se potom ili odbacuju, ili postaju jake.

## Dodatne mogućnosti

- Odraditi analizu kako se ponaša *Canny* filtar za različite vrednosti
  - granice za jake ivice
  - granice za slabe ivice
  - veličina kernela gausovog filtra

Uraditi analizu za više različitih slika

## Literatura

- [Sobel operator](https://en.wikipedia.org/wiki/Sobel_operator) na Vikipediji
- [Canny edge detector](https://en.wikipedia.org/wiki/Canny_edge_detector) na Vikipediji

## Rezultat

Nakon svih navedenih koraka dobija se ručno implementirani *Canny*
filtar. Nakon svakog od ranijih koraka dobija se neki od međurezultata
samog filtra.
