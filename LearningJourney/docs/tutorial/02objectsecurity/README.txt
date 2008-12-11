Securitatea obiectelor
----------------------
In acest pachet avem:
* o clasa continut simpla `Book` - mostenirea clasei Persistent nu e necesara,
  dar ajuta la salvarea automata a modificarilor clasei
* aceasta clasa este configurata in zcml sa aiba atributele disponibile prin
  declaratia <class>
* exista un view care adauga nou continut (addpage.html).
* acest continut va aparea intr-un listing de continut in ZMI
 

Explicatii
----------
Integrarea dintre Zope si ZODB face posibila stocarea oricaror tipuri de obiecte
python, chiar si cele mai simple clase. Adaugarea unui obiect in baza de date
este la fel de simpla ca instantierea obiectului si adaugarea lui, cu un nume
(cheie) la context, ce se comporta ca un dictionar. Numele obiectului (cheia
din dictionar) va fi folosita in URL pentru accesarea obiectului

Toate atributele unui obiect sunt protejate de Zope, de aceea trebuie sa 
declaram ce securitate dorim pentru acestea folosind declaratiile de securitate
pentru clasa si acele atribute. Exista doua tipuri de permisiuni pentru 
accesarea atributelor: permisiuni de citire (declarate cu `attributes`
si permisiuni de scriere, declarate cu `set_attributes`.