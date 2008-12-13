# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD = /home/tibi/workspace_g/LearningJourney/bin/sphinx-build
PAPER         =

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d /home/tibi/workspace_g/LearningJourney/docs/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) /home/tibi/workspace_g/LearningJourney/parts/sphinx

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
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/html /home/tibi/workspace_g/LearningJourney/docs/doctrees
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/html
	@echo
	@echo "Build finished. The HTML pages are in /home/tibi/workspace_g/LearningJourney/docs/html."

pickle:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/pickle /home/tibi/workspace_g/LearningJourney/docs/doctrees
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

web: pickle

json:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/json /home/tibi/workspace_g/LearningJourney/docs/doctrees
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/htmlhelp /home/tibi/workspace_g/LearningJourney/docs/doctrees
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in /home/tibi/workspace_g/LearningJourney/docs/htmlhelp."

latex:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/latex /home/tibi/workspace_g/LearningJourney/docs/doctrees
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/latex
	@echo
	@echo "Build finished; the LaTeX files are in /home/tibi/workspace_g/LearningJourney/docs/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/changes /home/tibi/workspace_g/LearningJourney/docs/doctrees
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/changes
	@echo
	@echo "The overview file is in /home/tibi/workspace_g/LearningJourney/docs/changes."

linkcheck:
	mkdir -p /home/tibi/workspace_g/LearningJourney/docs/linkcheck /home/tibi/workspace_g/LearningJourney/docs/doctrees
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) /home/tibi/workspace_g/LearningJourney/docs/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in /home/tibi/workspace_g/LearningJourney/docs/linkcheck/output.txt."
