TEMPLATES=$(SETTINGS)/templates

MAIN_SRC=$(TEMPLATES)/main
MAIN_DST=$(HOME)

RPM_SRC=$(TEMPLATES)/rpm
RPM_DST=$(RPM_SRC)

EXTENSION=.$(USER).temp

COPY_TEMPLATES=$(MYPYLIB)/copy_templates.py
#####################################################################

all: main rpm done

main:
	python $(COPY_TEMPLATES) $(MAIN_SRC) $(MAIN_DST)

rpm:
	python $(COPY_TEMPLATES) $(RPM_SRC) $(RPM_DST)

clean:
	rm -f $(MAIN_DST)/*$(EXTENSION) $(MAIN_DST)/.*$(EXTENSION)
	rm -f $(RPM_DST)/*$(EXTENSION) $(RPM_DST)/.*$(EXTENSION)

done:
	@echo '----------> Done'
