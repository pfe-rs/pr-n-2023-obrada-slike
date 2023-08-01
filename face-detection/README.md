# Detekcija lica

- Polaznik: Anđela Ristić
- Saradnici: Marija Nedeljković

## Uvod

Poslednjih par godina je detekcija lica postala poprilično popularna
tema u obradi slike i ima jako puno načina na koji se rešava ovaj
problem. Ideja zadatka je da se implementira detekcija lica na slici
obradom ulazne slike i prepoznavanjem kontura lica, nakon čega se
maskira površina lica.

## Postupak razvoja

Kako bi rad na zadatku bio jednostavniji potrebno je raditi na zadatku u
inkrementalnim koracima, tako da nas svaki korak vodi bliže rešenju:

1.  Prebaciti fotografiju u crno-belu fotografiju, jer je na takvoj jednostavnije detektovati lice. To jest odraditi binarizaciju slike.
2.  Morfološkim operacijama ukloniti sve artifakte
3.  Detekcija okvira maske
4.  Računanje uspešnosti detekcije

## Dodatne mogućnosti

- Poboljšati detekciju pojedinačnih delova lica korišćenjem dodatnih transformacija na fotografijama pre same detekcije.

## Literatura

- [Face detection - Wikipedia](https://en.wikipedia.org/wiki/Face_detection)

## Rezultat

Maksimalni očekivani rezultat je pravougaonik koji ide preko originalne
fotografije i preklopi samo lice maskom.
