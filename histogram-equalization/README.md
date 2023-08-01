# Ekvivalizacija histograma

- Polaznik: Stevanija Ciganović
- Saradnici: Andrej Lojdl

## Uvod

Adaptivna ekvivalizacija histograma je metoda koja za razliku od
klasične ekvivalizacije histograma, posmatra samo jedan deo slike i
adaptira histogram tog dela slike. Drugačije rečeno, za svaki piksel se
posmatra neka oblast oko njega kako bi se odradila ekvivalizacija
histograma i odredilo kako će se promeniti taj piksel.

## Postupak razvoja

Kako bi bilo jednostavnije raditi na zadatku, potrebno je raditi na
koracima koji će pomoći u samom razumevanju i povećalo verovatnoću da će
sam zadatak biti rešen do kraja. Preporučeni koraci su:

1. Iskoristiti ekvivalizaciju histograma na celoj slici, koristeći gotovu funkciju ekvivalizacije histograma iz biblioteke. Onda ponovo uraditi to isto, samo ovaj put primeniti adaptivnu ekvivalizaciju histograma. Preporuka je da se koristi OpenCV ili SciKit Image.
2. Potrebno je implementirati svoju ekvivalizaciju histograma nad celom slikom i uporediti da li radi isto kao funkcija iz biblioteke.
3. Implementirati adaptivnu ekvivalizaciju hostograma. Potrebno je uvećati sliku kako bi krajnje tačke imale dovoljno veliki broj suseda.

## Dodatne mogućnosti

- Moguće je nastaviti rad na zadatku time što će se uporediti “subjektivni kvalitet” adaptivne ekvivalizacije ako se koriste različite veličine regiona za adaptivnu ekvivalizaciju.
- Dodatno je moguće uraditi isto, ali proveriti na par primera kako tačno izgleda finalni histogram krajnje slike i proveriti matematički koliko se razlikuje od idealnog (ravnomerna raspodela).

## Literatura

- [Histogram equalization - Wikipedia](https://en.wikipedia.org/wiki/Histogram_equalization)
- [Adaptive histogram equalization - Wikipedia](https://en.wikipedia.org/wiki/Adaptive_histogram_equalization)
- [Histogram Equalization — skimage 0.21.0 documentation (scikit-image.org)](https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_equalize.html)
- [OpenCV: Histogram Equalization](https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html)

## Rezultat

Očekivano je da se samostano implementira adaptivna ekvivalizacija
histograma. Pored toga dodati su primeri nadogradnje zadatka.
