# Interpolacija zumiranja

- Polaznik: Stefan Stojković
- Saradnici: Nikola Ristanović

## Uvod

Prilikom zumiranja i prenošenja slika iz jednog rastera u drugi, često
se mogu pojaviti “rupe”, između piksela čije vrednosti znamo, odnosno
potrebno je estimirati vrednosti novih piksela između prethodno poznatih
piksela. Ovaj proces se zove interpolacija. Zadatak je da se neke od
slika transformišu i zumiraju a da se očuva veličina slike u pikselima.

## Postupak razvoja

1. **Transformisati sliku:** Proizvoljno je translirati, rotirati i/ili zumirati.
2. **Primena interpolacije:** Novonastale crne tačke (“Rupe”) zameniti interpolacijom sa okolnim tačkama. Upotrebiti bar 2 različite metode interpolacije. Nije dozvoljeno korišćene ugrađenih funkcija.
3. **Kvantitativna metrika:** Istražiti i definisati kvantitativnu metriku za evaluaciju rezultata interpolacije, u smislu kvaliteta slike. Uporediti sve implementirane metode interpolacije po pitanju kvantitativnih metrika za kvalitet slike, kao i brzine izvršavanja.

## Dodatne mogućnosti

- Primeniti 1 tip adaptivne interpolacije

## Literatura

- [Interpolacija](https://medium.com/@nuwanthidileka/image-interpolation-5e4cbe90603a) - metode

## Rezultat

Na kraju projekta polaznik je implementirao bar 2 različite metode
interpolacije i kvantitativno je procenio njihove performanse. Ukoliko
poslednji korak nije urađen, polaznik i dalje može kvalitativno da
proceni koji metod interpolacije daje bolje rezultate.
