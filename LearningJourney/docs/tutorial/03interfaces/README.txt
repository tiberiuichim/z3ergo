Interfete
---------

O interfata este o declaratie a capabilitatilor unei clase. Clasele declara
ca implementeaza acea interfata folosind zope.interface.implements(). O 
interfata contine documentatie despre comportamentul clasei, declaratii despre
metode (fara o implementare), declaratii de atribute si invariante, ce 
functioneaza ca validatori pentru valorile clasei ce implementeaza interfata.

In ZCML, oriunde apare necesitatea declararii unui tip de obiect se pot folosi
interfete ce sunt implementate de acel tip de obiect. In general attributul 
"for" din zcml necesita interfete (insa i se pot specifica si direct clase).

Interfetele care nu declara nimic sunt denumite "interfete marker"


Pagini implicite
----------------
Pagina implicita care va fi executata pentru un obiect atunci cand este 
vizitat direct este specificata de catre declaratia browser:defaultView in zcml.
In mod implicit, pentru toate obiectele, este folosita pagina index.html. 
Declarand o alta interfata decat cea implicita (zope.interface.Interface), se 
poate specifica o alta pagina implicita (de exemplu, detail.html) pentru 
obiectele de acel tip.


De citit
--------
Documentatia text din zope.interface (in mod special README.txt) 