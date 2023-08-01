# Gde je slika na PDF-u?

- Polaznik: Denis Softić
- Saradnici: Milomir Stefanović

## Uvod

PDF fajlovi se sastoje od mešavine teksta, slika, naslova i linkova, a
detekcija i razdvajanje opisanih delova je od krucijalnog značaja za
dalju analizu dokumenata. Jedna od mogućih analiza podrazumeva
izdvajanje slika, a ona ima velike primene pri bržem razumevanju i
ispitivanju konteksta.

Uz ovaj zadatak, priloženi su primeri novosti koje je potrebno obraditi
tako da se izdvoje sve slike iz njih.

## Postupak razvoja

1. Analizirati i odrediti tačne postupke implementacije rešenja ove problematike (detekcije slika).
2. Primenom odabranih metoda filtriranja/transformacija, detektovati sve slike kao objekte, a zatim i njihove ivice.
3. Izvršiti izdvajanje delova koji upadaju u detektovani prostor (slike u novostima).
4. Čuvati sve izdvojene slike u jednom folderu.

Dozvoljeno je koristiti ugrađene funkcije u svakom koraku po potrebi.

## Dodatne mogućnosti

- Osposobljavanje što bolje detekcije.
- Pronalaženje dodatnih primera i provera valjanosti algoritma nad njima.

## Rezultat

Nakon svakog koraka prikazati sliku, objasniti primenjenu metodu obrade
i objasniti odabir konkretnih parametara. Finalni produkt treba da
predstavlja folder u kome se nalazi što više slika izdvojenih iz
prosleđene slike novina.

Komentarisati poteškoće kod detekcije ukoliko ih je bilo, kao i
potencijalne načine rešenja tih problema. Tačnije, šta je pravilo
problema kod detekcije određenih slika na novostima.
