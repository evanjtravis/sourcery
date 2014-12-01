all:

init:
	make -f /home/ejtravis/settings/templates/Makefile


clean:
	make -f /home/ejtravis/settings/templates/Makefile clean.o

done.o:
	@echo '----------> Done'
