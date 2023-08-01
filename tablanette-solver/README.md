# Tablić solver

- Polaznik: Aleksa Vuković
- Saradnici: Andrej Bantulić

## Uvod

Ovaj projekat ima za cilj da razvije efikasan sistem za digitalnu obradu
slike za tačno određivanje zbira svih karata prisutnih na datoj slici.
Ovaj algoritam moze da se primenjuje u automobilskoj, gaming, pa i
poljoprivrednoj industriji za prebrojavanje objekata.

## Postupak razvoja

1. Filtrirati slike. Potrebno je olakšati da se detektuju karte. Uzeti u obzir morfološke operacije, kao i tehnike segmentacije slike.
2. Pronaći karte tako što ćete detektovati njihove ivice.
3. Pronađite vrednosti svake pojedinačne karte nevezano od znaka.

## Dodatne mogućnosti

- Karte mogu da se naslažu jedna na drugu
- Dodavanje senki na slikama

## Rezultat

Traženi rezultat je broj koji predstavlja sumu svih karata na talonu.
Detaljno obrazložiti postupak rada, od filtriranja slike do samog
prebrojavanja.
