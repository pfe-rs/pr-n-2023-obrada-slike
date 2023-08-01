# Čitanje tablice

- Polaznik: Vasilije Hadži-Purić
- Saradnici: Pavle Pađin

## Uvod

Prilikom slikanja predmeta jako često se javljaju različite vrste šuma,
najčešće usled pomeranja kamere ili samog objekta koji se snima. U
slučaju predmeta koji se pomeraju ovaj šum se naziva motion blur.
Zadatak je da motion blur na kolima sa slike uklonimo dovoljno da se
tablice na njima mogu pročitati od stane čoveka.

## Postupak razvoja

1. **Istražiti dekonvoluciju**: Ispitati kako metoda radi i kako može da se primeni. U MATLAB-u postoji ugrađena funkcija za deblurovanje, te je moguće videti efekte same transformacije. Izdvojiti bar dve metode deblurovanja.
2. **Implementacija deblura** : Implementirati odabrane metode deblurovanja. Kvalitativno uporediti rezultate
3. **Kvantitativna metrika:** Istražiti i pronaći kvantitativnu metriku (metrike) za evaluaciju kvaliteta slike. Evaluate performanse implementiranih deblur tehnika.

## Dodatne mogućnosti

- Odrediti pravac motion blura na slici i u skladu s tim popraviti performanse izoštravanja

## Literatura

- [Dekonvolucija](https://www.mathworks.com/help/images/deblurring-images-using-the-blind-deconvolution-algorithm.html)

## Rezultat

Na kraju bi trebalo dobiti odmućenu sliku sa čitljivim tablicama.
Ukoliko je i poslednji korak odrađen, može se kvantitativno odrediti
najbolja od navedenih metoda.
