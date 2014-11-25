# 1. If you haven't already:
# 	 Run 'Makefile' located in this directory
# 2. Copy this file into the project's BASE_DIR
# 3. Run
#
#
# This makefile is designed to automate the building of an RPM
# within the context of SDG virtual environment and python distutils.
USR=$(shell whoami)
HOME=/home/$(USR)/
PACKAGE=ComputerRegistration
TMP=$(HOME)tmp/
PROJ_PATH=$(HOME)$(PACKAGE)/
VERSION=5.4rc1
RPM=$(PACKAGE)-$(VERSION)-1.el6.noarch.rpm
SVC=security-tools

all: clean.o build.o permission.o done.o

clean.o:
	rm -rf $(TMP)
	rm -rf $(PROJ_PATH)build
	rm -rf $(PROJ_PATH)dist

build.o:
	python $(PROJ_PATH)setup.py bdist_rpm
	mkdir $(TMP)
	cp $(PROJ_PATH)dist/$(RPM) $(TMP)

permission.o:
	chmod g+rx $(TMP)
	chown .$(SVC) $(TMP)
	chmod g+r $(TMP)$(RPM)
	chown .$(SVC) $(TMP)$(RPM)

done.o:
	@echo '---------->DONE'
