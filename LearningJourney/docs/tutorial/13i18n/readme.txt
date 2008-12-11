Simple Internationalization & Localization
-----------------------------------------------

* i18n (internationalization) - 18 characters: making a product translatable
* l10n (Localization) - 10 characters: sinonim 18n, mostly referring to currency,
  dates
* defined a new MessageIDFactory (as underscore _ )
* changes
   * interface
   * message set by ratingviews
   * BookSize adapter (look at the mapping argument for _ )
   * added a i18n:translate for "Extra bottom" in bookview.pt and a i18n:domain at the
     top of the file
* used i18nextract from zopeinstance/bin to extract the messages in a .pot file
* used poedit to generate a po file from the .pot
* created the locales/ro/LC_MESSAGES where placed the .mo + .po files
* added the locales declaration in configure.zcml
* configure Firefox to have Romanian as preferred language

NOTE: content translation is not done in this step