TEMPLATES=$(HOME)/settings/templates/

MAIN_SRC=$(TEMPLATES)main/
MAIN_DST=/home/ejtravis/

RPM_SRC=$(TEMPLATES)rpm/
RPM_DST=$(RPM_SRC)

EXTENSION=.ejtravis.temp
DUMMY=dummy$(EXTENSION)

COPY_TEMPLATES=$(MYPYLIB)copy_templates.py
#####################################################################

all: main.o rpm.o source.o done.o

main.o:
	python $(COPY_TEMPLATES) $(MAIN_SRC) $(MAIN_DST)

rpm.o:
	python $(COPY_TEMPLATES) $(RPM_SRC) $(RPM_DST)

source.o:
	source ~/.bash_profile

clean.o:
	rm -f $(MAIN_DST)*$(EXTENSION) $(MAIN_DST).*$(EXTENSION)
	rm -f $(RPM_DST)*$(EXTENSION) $(RPM_DST).*$(EXTENSION)

done.o:
	@echo '----------> Done'
