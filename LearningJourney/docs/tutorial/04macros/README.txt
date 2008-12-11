Folosirea macro-urilor in template-uri
--------------------------------------
Datorita faptului ca Zope 3 nu ofera publicarea directa a template-urilor si
atasarea lor de orice tip de context, folosirea macro-urilor in Zope 3 este mai
anevoioasa.

Metoda clasica in Zope 3 de folosire a macro-urilor este inregistrarea unor
pagini care ofera macro-uri intr-o lista dintr-o pagina denumita 
`standard_macros`. Folosirea lor poate fi observata in cadrul pachetului
`learningjourney.ui.site`. 

Pentru a face mai usoara utilizarea acestora, comunitatea Zope a realizat un
pachet de extensie, `z3c.macro`, ce inregistreaza un nou tip de expresie TAL,
`macro` si care poate fi folosit pentru inregistrarea directa paginilor care
ofera macro-uri.