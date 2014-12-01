all:

init:
	make -f $(SETTINGS)templates/Makefile


clean:
	make -f $(SETTINGS)templates/Makefile clean.o

done.o:
	@echo '----------> Done'
