# Promena palete scene

- Polaznik: Marko Milivojević
- Saradnik: Jelena Marinković

## Uvod

Paleta boja može predstavljati sve boje koje se prolanaze na slici ili
određeni broj boja koje se nalaze u najvećem broju. Najčešće paletu boja
predstavlja šest nijansi. Ako želimo da dve slike izgledaju skladno, npr
kao što prepoznajemo umetnike po stilu, možemo ih modifikovati tako da
imaju istu paletu boja.

CIlj ovog zadatka je primeniti paletu boja jedne slike na drugu.

## Postupak razvoja

Zadatak se radi iz više koraka:

1.  Odrediti paletu boja slike pomoću bibliotečke funkcije.
2.  Odrediti palete boja slika bez korišćenja bibliotečke funkcije.
3.  Za primenjivanje palete boja jedne slike na drugu koristi se proces specifikacije histograma (histogram matching). To se vrši modifikacijom kumulativnog histograma jedne slike prema kumulativnom histogramu druge. Kod slike u boji je potrebno proces ponoviti za svaki od kanala boje ponaosob.

### Dodatne mogućnosti

- Podeliti sliku na delove pa svaki modifikovati paletama boja različitih slika.

## Literatura

- [Image Color Extraction with Python in 4 Steps \| by Boriharn K \| Towards Data Science](https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e)
- [Histogram matching - Wikipedia](https://en.m.wikipedia.org/wiki/Histogram_matching)

## Rezultat

Željeni rezultat je dobijanje dve slike koje izgledaju kao da su urađene
sa istim ograničenim skupom boja.
