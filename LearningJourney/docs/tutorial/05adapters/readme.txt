Adapteri
--------
Adaptorul este o implementare a modelului AOP (aspect oriented programming). El
ajuta, cu ajutorul interfetelor, sa se obtina un aspect al unui obiect. In 
procesul de adaptere sunt implicate obiectul adaptat si interfata ce determina
aspectul care ne intereseaza asupra obiectului. Un exemplu:

Sa presupunem ca avem un container in care se afla diverse obiecte. Unele sunt
fisiere audio (mp3), altele sunt imagini, altele sunt fisiere text, etc. Ne 
intereseaza sa afisam dimensiunea specifica fiecaruia dintre aceste obiecte. 
Astfel, pentru fisierele audio va fi afisata marimea in timp, pentru imagini 
marimea in pixeli, etc. 

Solutiile care nu ar implica zope.component pot fi:
* Construirea unei clase care sa cunoasca modul in care se extrage informatia 
  din fiecare tip de obiect. Acest sistem este inflexibil: pentru a adauga
  un nou tip de obiect in acel folder, clasa ar trebui completata in asa fel
  incat sa stie despre acesta.
* Implementarea, de catre fiecare obiect, a unei metode speciale care sa 
  intoarca informatia care va fi afisata. Aceasta presupune ca acele obiecte
  sa stie deja in ce sisteme vor fi integrate si are ca si consecinta 
  supraincarcarea cu functionalitate a obiectelor.
  
Solutia oferita de adapteri este una eleganta, insa mai complexa:    

Vom avea o interfata IDisplaySize care defineste modul in care se afiseaza 
dimensiunea obiectelor:

class IDisplaySize(Interface):
    """Asigura informatii despre marimea obiectelor"""
    
    get_size():
        """Afiseaza marimea, pentru utilizatori"""

In codul care realizeaza afisarea marimii, aceasta va fi extrasa de pe fiecare
obiect construind un adapter pentru fiecare obiect:

    >>> size = getAdapter(IDisplaySize, obj).get_size()
    
Se remarca ca adaptorul ce este construit in urma apelarii getAdapter este o 
componenta ce asigura (provides) interfata IDisplaySize. Prin constructia 
adaptorului se poate obtine o implementare specifica fiecarui tip de context: 

class Mp3DisplaySize(object):
    zope.component.adapts(IMp3File)
    zope.interface.implements(IDisplaySize)
    
    def __init__(self, context):
        self.context = context
            
    def get_size(self):
        sound_length = extract_track_size(context) 
        return "%s seconds" % sound_length
        
class ImageDisplaySize(object)
    zope.component.adapts(IImage)
    zope.interface.implements(IDisplaySize)
    
    def __init__(self, context):
        self.context = context
    
    def get_size(self):
        width, height = get_image_size(context)
        return "%s x %s px" % (width, height)
        
Astfel, in functie de tipul contextului (IMp3File sau IImage), va fi selectata 
clasa care va fi folosita in constructia adapterului, obtinandu-se astfel un 
obiect diferit ce va sti cum sa extraga informatia dorita din context.

In loc de getAdapter(...) poate fi folosita ca si scurtatura constructia:

    >>> IDisplaySize(obj).get_size()

Exista si multiadapteri, care adapteaza mai mult de un obiect la o anumita 
interfata. Cel mai des intalnit exemplu de multiadapter este pagina 
(sau view-ul), ce adapteaza request-ul - informatia provenita de la utilizator,
impreuna cu obiectul context, la un o informatie de tip IBrowserPublisher ce
va fi intoarsa utilizatorului. Paginile sunt inregistrate ca multiadapteri cu 
nume, asa ca nu mai trebuie sa specificam intefata la care vrem sa adaptam
cele doua obiecte, pentru ca este una singura pentru acel nume si acel tip
de request:

    >>> view = getMultiAdapter((context, request), name='index.html')
    >>> page_content = view()