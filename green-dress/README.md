# Haljina

- Polaznik: Nikola Najić
- Saradnici: Pavle Pađin

## Uvod

Data je slika (bivše) engleske kraljice sa potpuno zelenom haljinom.
Potrebno je određenu boju/teksturu primeniti na datu haljinu. Potrebno
je da to izgleda realistično, odnosno da sva savijanja haljine i senke
koja su bila prisutna na inicijalnoj slici budu prisutne i na konačnoj
slici.

## Postupak razvoja

1.  **Izdvajanje maske:** Potrebno je iz originalne slike izdvojiti samo deo slike koji odgovara haljini, odnosno masku slike. Imati na umu da je s razlogom korišćena haljina čija boja značajno odstupa od ostatka slike.
2.  **Osnovna primena teksture:** Potrebno je na osnovu prethodnog koraka, primeniti teksturu koja je data samo na mestu gde je izdvojena maska haljine. Ne treba voditi računama o senkama i savijanjima same haljine u ovom delu.
3.  **Senke i savijanja:** Rezultat iz prethodnog koraka je potrebno učiniti realističnijim, odnosno da se vide sve senke koje padaju na haljinu, kao i delovi gde se haljina savija.

## Dodatne mogućnosti

- Napraviti grafički interfejs gde je prikazana slika i slajder koji određuje boju haljine. Kada se pomera slajder, boja haljine se menja u realnom vremenu.

## Rezultat

Rezultat celog projekta bila bi realistična slika kraljice sa novom
haljinom.
