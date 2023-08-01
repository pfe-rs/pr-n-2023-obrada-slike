# Izoštravanje

- Polaznik: Anastasija Milanović
- Saradnici: Jelena Marinković

## Uvod

Jedna od osnovnih manipulacija nad slikama je izoštravanje. Može se
koristiti iz estetskih razloga, da bi slike koje se objavljuju na
socijalnim mrežama bile manje mutne, ili radi dobijanja korisnih
informacija, čitanje registarskih tablica sa snimaka sigurnosnih kamera,
ili slično.

Cilj ovog zadatka je izoštriti slike iz datog skupa zamućenih slika.

## Postupak razvoja

Zadatak se radi iz više koraka:

1.  Izoštriti slike izdvajanjem ivica. Potrebno je dodatno zamutiiti sliku (koristiti ) pa ih oduzeti čime se dobijaju ivice. Zatim se ivice pomnože n puta (npr 10) pa kada se to doda na original dobija se izoštrena slika. U ovom koraku je potrebno varirati standardnu devijaciju Gausa i koliko se puta množe ivice da bi se našlo najbolje rešenje.
2.  Izoštravanje pomoću laplasijana. Pomoću laplasijana detektovati značajne ivice, pomnožiti nekim faktorom pa dodati na original.
3.  Uporediti uspešnost izoštravanja metoda u prva dva koraka

### Dodatne mogućnosti

- Pronaći treći metod izoštravanja i uporediti sa prethodna dva.

## Literatura

- [Skup podataka](https://www.kaggle.com/datasets/kwentar/blur-dataset)
- [Gaussian blur - Wikipedia](https://en.wikipedia.org/wiki/Gaussian_blur)
- [Spatial Filters - Laplacian/Laplacian of Gaussian](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)

## Rezultat

Željeni je rezultat da pri vizulenoj proveri dobijena slika izgleda
očigledno unapređena u odnosu na zamućenu sliku.
