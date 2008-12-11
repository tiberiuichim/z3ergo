Local utilities
-----------------

* Local utilities are registered on local sites. Local utilities override each other in the tree
  (or their global utility counterpart)

* Changed the fortune utility to be Contained and Persistent - this will be the local utility
* The Global utility inherits from the local utility, and is instantiated (fortuneteller)
  (just like stage 21)
* There are new interfaces defined in ``interfaces``
* Added addMenuItem entry and the edit page to be able add/edit local utility

To do in the browser
~~~~~~~~~~~~~~~~~~~~~~
* Use the ++skin++DemoSkin path
* Add a new folder, make it site
* Inside the ++etc++ namespace, default folder, add a Fortune Utility, register for IFortuneTeller
* In the Settings page, change the command that is ran to /ls/bin
