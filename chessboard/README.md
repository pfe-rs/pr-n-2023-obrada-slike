# Šahovska tabla

- Polaznik: Marko Mihajlović
- Saradnik: Luka Simić (priprema), Pavle Pađin (mentor)

## Uvod

Ovaj domaći zadatak obuhvata program kojem je data slika šahovske table,
koju on treba da uspešno detektuje i ispravi.

## Postupak razvoja

1. Napisati Harisov detektor ćoškova, iscrtati tačke na slici na mestima gde su detektovani ćoškovi radi testiranja. Nije dozvoljeno koristiti bibliotečke funkcije koje implementiraju ovaj detektor.
2. Transformisati šahovsku tablu korišćenjem ugrađenih bibliotečkih funkcija, na osnovu detektovanih ćoškova iz prethodnog koraka. Ukoliko prethodni korak nije realizovan, moguće je koristiti i bibliotečke funkcije pri detekciji ćoškova za realizaciju ovog koraka.

## Dodatne mogućnosti

- Srediti da se i table sa 3D zakrivljenostima (afine transformacije) isprave.

## Literatura

- [Skup podataka](https://www.kaggle.com/datasets/danielwe14/stereocamera-chessboard-pictures)
- [Harris corner detector](https://en.wikipedia.org/wiki/Harris_corner_detector) na Vikipediji
- [Harris Corner Detection Explained](https://www.baeldung.com/cs/harris-corner-detection)

## Rezultat

U program ulaze zakrivljene slike šahovskih tabli, a izlaze ispravljene.
