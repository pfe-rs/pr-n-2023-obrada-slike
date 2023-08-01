# Adaptivni medijan

- Polaznik: Marko Paramentić
- Saradnici: Nikola Ristanović

## Uvod

U slučajevima kada se prilikom prenosa ili skladištenja podataka može
doći do nagle promene informacija, može doći do deformacije slike u vidu
pojedinačnih, potpuno (ili skoro potpuno) beli ili crni pikseli.
Adaptivni median filter menja svoje parametre na osnovu količine šuma u
slici. U koliko neki piksel ima značajno drugačiju vrednost u odnosu na
piksele oko njega, on se tretira kao šum.

## Postupak razvoja

1. **Generisati slike:** Generisati slike za obradu pošumljivanjem, sa različitom količinom šuma (20%, 40%, 60% …)**   **
2. **Implementirati:** algoritam za filtriranje **bez** korišćenja bibliotetičkih funkcija za filtriranje šuma (ne adaptivni)
3. **Implementirati:** algoritam za filtriranje **bez** korišćenja bibliotetičkih funkcija za filtriranje šuma (adaptivni) koji će menjati svoje parametre u zavisnosti od količine šuma u slici. Potrebno je odraditi procenu količine šuma za svaku sliku i u skladu sa tim podesiti parametre adaptivnog median filtra.
4. **Uporediti uticaj** adaptivnog i neadaptivnog filtra za različite količine šuma na slici

## Dodatne mogućnosti

- Analizirati kako parametri filtra utiču na suzbijanje šuma i kvalitet slike nakon filtriranja
- Uporediti koji je filtar brži: filtar bibliotetičke funkcije ili filtar napravljen bez upotrebe biblioteka. Kvantifikovati (izmeriti) razliku

## Literatura

- [Median filtar](https://en.wikipedia.org/wiki/Median_filter)
- [Adaptivni median filtar](https://www.irjet.net/archives/V6/i10/IRJET-V6I10148.pdf)

## Rezultat

Na kraju se mogu primetiti razlike između različitih kombinacija
parametara adaptivnog medijanog filtra, kao i između
