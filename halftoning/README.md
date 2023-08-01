# Polutoniranje

- Polaznik: Jovana Grujičić
- Saradnici: Nikola Drakulić

## Uvod

Halftoning ili polutoniranje je sistem štampanja koji ostavlja sitne
tačke na papiru koje se sa dovoljno velike udaljenosti čine uniformisanu
sliku (isti princip rada kao pikseli na monitoru). Ovi polutonovi se
pojavljuju periodično i ponekad mogu biti jako veliki/prenaglašeni i
zbog toga se uklanjaju kada je u pitanju digitalna slika.

## Postupak razvoja

1. **Analiza spektra slike:** zbog periodične prirode ovog šuma, moguće je primentiti filtar koji će eliminisati samo određene učestanosti.
2. **Uklanjanje šuma:** Nakon uspešne analize mogu se izbaciti frekvencije koje uzrokuju šum na svakom kanalu (low pass i band stop filtri)
3. **Prikazivanje razika frekventnih spektara :** Prikazati razlike spektara frekvencija pre i posle uklanjanja šuma. Uraditi ovo za svaki kanal boje, naznačiti vidne promene i prokomentarisati ih sa mentorom.

## Dodatne mogućnosti:

- Upotrebiti blur kako bi se slika dodatno ujednačila.
- Upotrebiti funkciju za izoštravanje kako bi slika postala izražajnija.

## Rezultat

Na kraju je moguće pokazati učinak ovog filtra za uklanjanje periodičnih
grešaka u slikama. Slika treba da bude jasna i uniformisana.
