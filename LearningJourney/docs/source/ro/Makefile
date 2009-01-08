# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD = /home/tibi/workspace_g/LearningJourney/bin/sphinx-build
PAPER         =

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/source/ro

.PHONY: help clean html web pickle htmlhelp latex changes linkcheck

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  pickle    to make pickle files"
	@echo "  json      to make JSON files"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  changes   to make an overview over all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"

clean:
	-rm -rf /home/tibi/workspace_g/LearningJourney/docs/*

html:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/html/ro /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/html/ro
	@echo
	@echo "Build finished. The HTML pages are in /home/tibi/workspace_g/LearningJourney/docs/html/ro."

pickle:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/pickle/ro /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/pickle/ro
	@echo
	@echo "Build finished; now you can process the pickle files."

web: pickle

json:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/json/ro /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/json/ro
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/htmlhelp/ro /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/htmlhelp/ro
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in /home/tibi/workspace_g/LearningJourney/docs/htmlhelp/ro."

latex:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/latex/ro /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/latex/ro
	@echo
	@echo "Build finished; the LaTeX files are in /home/tibi/workspace_g/LearningJourney/docs/latex/ro."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/changes/ro /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/changes/ro
	@echo
	@echo "The overview file is in /home/tibi/workspace_g/LearningJourney/docs/changes."

linkcheck:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/linkcheck/ro /home/tibi/workspace_g/LearningJourney/docs/doctrees/ro
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/linkcheck/ro
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in /home/tibi/workspace_g/LearningJourney/docs/linkcheck/ro/output.txt."
