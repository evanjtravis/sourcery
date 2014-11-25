all:

clean.o:
	make -f $(SETTINGS)templates/Makefile clean.o

done.o:
	@echo '----------> Done'
