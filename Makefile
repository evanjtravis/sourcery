all:
	
init.o:
	export SETTINGS=/home/ejtravis/settings
	export MYPYLIB=/home/ejtravis/settings/mypylib
	export PYTHONPATH=$(PYTHONPATH):$(MYPYLIB)
	make -f /home/ejtravis/settings/templates/Makefile

clean.o:
	make -f /home/ejtravis/settings/templates/Makefile clean.o

done.o:
	@echo '----------> Done'
