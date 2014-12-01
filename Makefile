all:

init:
	make -f $(SETTINGS)templates/Makefile


clean:
	make -f $(SETTINGS)templates/Makefile clean

done:
	@echo '----------> Done'
