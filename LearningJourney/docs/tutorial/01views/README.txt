View-uri 
--------
View-urile sunt componente generale ce prezinta un aspect al unui context, 
intentionat pentru vizualizarea de catre un utilizator. View-urile pentru 
browser (browser views) sunt view-uri vizualizate prin browser (http). Exista
3 tipuri de view-uri in Zope 3, ceea ce creeaza o anume confuzie:
 
* browser pages
* browser views
* view-uri generale (zope views)

Diferenta dintre browser views si browser pages este ca destinatia paginilor 
este cea de a interactiona cu utilizatorul, de a fi publicabile prin web. 
Destinatia view-urilor este una interna, prin care se publica un aspect al unui
obiect dar nu va fi publicata ca pagina de sine statatoare catre utilizator.  


Explicatii
----------
Orice "continut" sau "pagina" sau actiune accesibila in Zope prin browser 
trebuie sa fie generate de un browser view. De obicei acest browser view este
scris ca o simpla clasa, derivata din `object`, sau dintr-un template ZPT.
View-urile si paginile browser sunt inregistrate folosind namespace-ul 
http://namespaces.zope.org/browser, cu directivele `page` si `view`. 

Un view se genereaza atunci cand i se apeleaza metoda __call__. Daca declaratia
browser:page continue o optiune `attribute`, atunci acea metoda va fi folosita
pentru generarea paginii. Rezultatul acelei metode trebuie sa fie potrivita
afisarii in browser, deci trebuie sa fie un string sau o pagina de template
deja procesata.  

In interiorul template-ului clasa de browser view este disponibila prin  
obiectul `view`.

Inside the template, the browser view class is available as the `view` object. 
There is also a global collection of views accessible for the context 
available under the `views` mapping.

Pages are usually registered for an interface, so they will be available only 
to objects that implement that declare to implement that interface. To make a 
page accessible to all object types, use ``for="*"``


Alte forme de view-uri
----------------------

Exemplul 1
~~~~~~~~~~
Un view fara template

In modulul hello.py:

    class Hello:
        def __call__(self):
            return "Hello world"

In fisierul configure.zcml:

    <browser:page
        for="*"
        name="hello.html"
        class="hello.Hello"
        permission="zope.View"
        />

* Se navigheaza apoi catre http://localhost:8080/hello.html

Exemplul 2
~~~~~~~~~~
Putem accesa clasa ce genereaza view-ul prin obiectul `view` din template.

* in modulul hello.py
    class Hello:
        def greet(self, name):
            return "Hello, %s" % name

* in template.pt:
    <span tal:content="python: view.greet(name='World')"/>

* in configure.zcml
    <browser:page
        for="*"
        name="hello.html"
        class="hello.Hello"
        permission="zope.View"
        template="template.pt"
        />

* Navigheaza catre http://localhost:8080/hello.html  

Examplul 3
~~~~~~~~~~
Folosirea unui atribut al clasei pentru generarea clasei

* module hello.py same as Example 2
* configure.zcml
    <browser:page
        for="*"
        name="hello.html"
        class="hello.Hello"
        permission="zope.View"
        attribute="greet"
        />

* greet() will now be executed when you view the hello.html page