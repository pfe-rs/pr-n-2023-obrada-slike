# Panorama

- Polaznik: Rada Novakov
- Saradnik: Srđan Radović

## Uvod

Dato je nekoliko slika iste scene koje treba spojiti u jednu panoramsku
sliku. Pretpostaviti da je panorama samo horizontalna (sve slike su u
istoj visini, kamera se pomera samo levo-desno), da postoji preklapanje
između susednih slika i da su slike poređane u smeru sa leva na desno.

## Postupak razvoja

1. Izdvojiti karakteristične tačke sa slika (uz koriščenje gotove implementacije)
2. Iskoristiti gotov feature detektor i algoritam za uparivanje tačaka
3. Povezati susedne slike u panoramu
4. Izjednačiti osvetljenje između slika i/ili ga postepeno menjati, radi glatkog uklapanja između susednih slika

## Dodatne mogućnosti

- Umesto gotove implementacije algoritma za uparivanje tačaka, ručno implementirati dati algoritam

## Literatura

- [Panoramic photography](https://en.wikipedia.org/wiki/Panoramic_photography)

## Rezultat

Idealan rezultat je da spajanje slika radi relativno robusno (sličan
kvalitet na različitim slikama) i da je kvalitet prelaza zadovoljavajuć
(usklađeno osvetljenje).

U slučaju nedostatka vremena, može se posmatrati samo dataset sa
translacijom.
