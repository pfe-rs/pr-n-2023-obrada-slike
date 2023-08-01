# Bar kod detektor

- Polaznik: Lenka Jakovljević
- Saradnici: Luka Simić

## Uvod

Ideja ovog domaćeg zadatka jeste izrada programa koji sa slike ume da
pročita bar kod, koji može biti i nakrivljen, i ispiše njegov sadržaj.

## Postupak razvoja

1.  **Bar kod detekcija:** Pronaći oblast sa bar kodom na slici, i uokviriti je (ili ispraviti) kako bi se znalo iz koje oblasti slike i u kom smeru program treba da čita bar kod. Nije dozvoljeno korišćenje bibliotečkih funkcija za detekciju objekata na slici, ali jeste za transformacije slike.
    - Za početak testirati na nezakrivljenim/nerotiranim slikama bar kodova, zatim probati i na rotiranim.
    - 3D zakrivljenosti (afine transformacije) mogu da budu rešene i kao četvrti korak ovog projekta.
2.  **Bar kod čitanje:** Pročitati bar kod u EAN-13 formatu. Ispisati sadržaj bar koda. Nije dozvoljeno korišćenje bibliotečkih funkcija za dekodovanje bar kodova.
3.  Testirati program na celom skupu podataka i ispisati njegovu ukupnu tačnost.

## Dodatne mogućnosti

- Podržati više bar kod standarda (videti [ostale bar kod skupove podataka](https://github.com/BenSouchet/barcode-datasets)).

## Literatura

- [Skup podataka](http://artelab.dista.uninsubria.it/downloads/datasets/barcode/medium_barcode_1d/medium_barcode_1d.html)
- [Barcode](https://en.wikipedia.org/wiki/Barcode) na Vikipediji (za generalni način funkcionisanja bar kodova)
- [International Article Number](https://en.wikipedia.org/wiki/International_Article_Number) na Vikipediji (za način funkcionisanja EAN-13 bar koda koji se koristi u gorepomenutom skupu podataka)

## Rezultat

Program uspešno detektuje bar kodove sa nekih slika, i može da se
testira nad celim skupom podataka. Polaznik je upoznat sa nedostacima
svog algoritma (jasno mu je gde i zašto ne radi).

Ukoliko bar kod detekcija ispadne preveliki izazov, moguće je
realizovati samo bar kod čitanje. U tom slučaju skup podataka se može
generisati nekim [onlajn generatorom bar kodova](https://barcode.tec-it.com/en/EAN13).
