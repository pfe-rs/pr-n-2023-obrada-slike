# Optimalni de-blur

- Polaznik: Darija Vasiljević
- Saradnici: Anđela Bogdanović

## Uvod

Problem uklanjanja šuma sa slike se često rešava blurovanjem same slike.
Mana ovakvog pristupa je što se gubi oštrina same slike. Postavka
problema je sledeća: Slika je blurovana Gausovim blurom i potrebno je
izvršiti proces de-blurovanja slike. Standardna devijacija Gausovog
blura može da varira, te je takođe potrebno izvršiti određenu procenu
parametara kojima je blurovana slika, pa potom izvršiti adekvatno
de-blurovanje.

## Postupak razvoja

1. **Rad sa bibliotečkim funkcijama:** Uzeti sliku, izvršiti blurovanje same slike pomoću bibliotečke funkcije (GaussianBlur), i varirati standardnu devijaciju i veličinu kernela. Ideja je da se stekne osećaj šta se dešava promenom ovih parametara.
2. **Implementacija de-blurovanja:** Implementirati samostalno algoritam de-blurovanja. U ovom delu je potrebno da za neku, unapred poznatu standardnu devijaciju (npr. 5) algoritam de-blurovanja daje razumne rezultate.
    - **Rezultat:** Originalna, Blurovana, Deblurovana slika
3. **Promenljiva standardna devijacija:** U ovom delu treba pretpostaviti da standardna devijacija blurovanja nije poznata. Filtar treba da daje dobre rezultate za više vrednosti standardne devijacije (npr. 2, 5, 10).
    - **Rezultat:** Originalna, Blurovana, Deblurovana slika za različite vrednosti standardne devijacije

## Dodatne mogućnosti

- Istražiti kako možemo da popravimo performanse de-blurovanja kada se varira i veličina kernela

## Literatura

- [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur)

## Rezultat

Na kraju je moguće pokazati performanse samog algoritma de-blurovanja.
