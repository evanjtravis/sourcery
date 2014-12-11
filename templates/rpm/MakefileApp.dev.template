# 1. If you haven't already:
# 	 Run 'Makefile' located in this directory
# 2. Copy this file into the project's BASE_DIR
# 3. Run
#
#
# This makefile is designed to automate the building of an RPM
# within the context of SDG virtual environment and python distutils.
PACKAGE=ComputerRegistration
TMP=$(HOME)/tmp
PROJ_PATH=$(HOME)/$(PACKAGE)
VERSION=5.4rc1
RPM=$(PACKAGE)-$(VERSION)-1.el6.noarch.rpm

all: clean build permission done

clean:
	rm -rf $(TMP)
	rm -rf $(PROJ_PATH)/build
	rm -rf $(PROJ_PATH)/dist

build:
	python $(PROJ_PATH)/setup.py bdist_rpm
	mkdir $(TMP)
	cp $(PROJ_PATH)/dist/$(RPM) $(TMP)

permission:
	chmod g+rx $(TMP)
	chown .$(SERVICE) $(TMP)
	chmod g+r $(TMP)/$(RPM)
	chown .$(SERVICE) $(TMP)/$(RPM)

done:
	@echo '---------->DONE'
