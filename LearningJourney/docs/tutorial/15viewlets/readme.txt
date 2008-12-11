Viewlets & Viewlet Managers
-----------------------------

* Viewlets Managers are content providers that aggregate other viewlets/content providers
* They are responsible for a region (identified by a `marker` interface)

* Added viewlet manager declaration in interfaces
* Added viewlet manager registration in configure.zcml (browser:viewletManager)

* Viewlets are content providers
* Viewlets are registered for object, request, view + viewlet manager

* Declared two viewlets, content providers & templates
* Changed template_tablelayout to include the viewlet manager
