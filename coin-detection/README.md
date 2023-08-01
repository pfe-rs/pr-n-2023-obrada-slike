# Prepoznavanje novčića

- Polaznik: Kosta Petković
- Saradnici: Marija Nedeljković

## Uvod

Automatsko prepoznavanje novčića može biti korisna alatka u različitim
automatima. Postavka problema je sledeća: Imamo više slika novčića od po
jednog i od po pet dinara. Na svakoj slici su prisutna oba tipa novčića.
Potrebno je napraviti algoritam koji bi sabrao koliko novca je prisutno
na stolu.

## Postupak razvoja

1.  Prvi korak je pretprocesiranje slike. Ukloniti viškove na slici morfoloskim transformacijama. Svesti celu sliku na dve boje - jedna koja predstavlja novčiće, druga koja predstavlja pozadinu.
2.  Potrebno je izbrojati koliko novčića je na stolu (nezavisno kog su tipa). Nije dozvoljeno korišćenje bibliotečkih funkcija za filtriranje, obradu slike ili automatsku detekciju krugova.
3.  Drugi korak je za svaki od novčića, odrediti kog je tipa, te ispisati konačan zbir svih novčića na stolu. Ista pravila važe kao u prethodnom koraku.

## Dodatne mogućnosti

- Napraviti program koji u realnom vremenu snima sto (ili drugu ravnu površinu) i detektuje sve prisutne novčiće, kao i njihov zbir. Kada se novčić stavi ili skloni sa stola, zbir se promeni u skladu sa tim.
- Osposobiti algoritam za rad sa 1, 2 i 5 dinara.

## Literatura

- [Circle Hough Transform](https://en.wikipedia.org/wiki/Circle_Hough_Transform)
- [Erosion (morphology)](https://en.wikipedia.org/wiki/Erosion_(morphology))

## Rezultat

Nakon prvog koraka moguće je izbrojati broj novčića koji se nalaze na
stolu. Nakon svih koraka moguće je izračunati koliko dinara se nalazi na
stolu.
