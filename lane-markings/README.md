# Linije na putu

- Polaznik: Nataša Kovačević
- Saradnici: Andrej Bantulić

## Uvod

Ovaj projekat se fokusira na razvoju efikasnog
sistema detekcije linija na putu. Relevantan je u kontekstu održivog
transporta. Precizna detekcija linija na putu može olakšati integraciju
autonomnih i električnih vozila, omogućavajući efikasno korišćenje
prostora na putu i smanjenje CO2 emisije. Usmeravanjem saobraćajnog toka
i unapređenjem navigacionih sistema, možemo napraviti značajan napredak
ka izgradnji bezbednijeg, kao i ekološki prihvatljivijeg transportnog
sistema.

Napomena: Detektovati linije sa desne i leve strane
vozila (linije koje oivičavaju put kojim se vozilo kreće). Ne
detektovati linije koje obuhvataju druge trake i slično.

## Postupak razvoja

1. Primenom odabranih transformacija i filtriranja izdvojiti samo ivice linija. Treba znati gde im je početak a gde kraj. Razmisliti na koji način analiza spektra boja može biti korisna prilikom detekcije.
2. Podeliti sliku na regione od interesa. Ako tražite linije, nebo i drveće sa strane vam nije bitno.
3. Pronaći linije na osnovu pronađenih ćoškova.
4. Filtrirati nerelevantne linije poput rupa na putu.
5. Uokviriti pronađene linije da bi se lepo video rezultat.

## Dodatne mogućnosti

- Analizirati snimke koji se nalaze unutar foldera. Napraviti automatsku detekciju linija na snimku.
- Paziti na pojavu mostova i tunela koji smanjuju osvetljenost snimka.

## Rezultat

Očekivani rezultat će biti slika na kojoj će da se
nalaze samo linije sa puta. Detaljno objasniti (priložiti slike)
realizaciju svakog koraka pri detekciji linija, filtriranja slike pa i
pronalasku ćoškova linija. Objasniti odabir parametara ukoliko je to u
nekom koraku neophodno.
