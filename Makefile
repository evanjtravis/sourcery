all:

init:
	make -f $(SETTINGS)templates/Makefile
	./vim/vundle.sh


clean:
	make -f $(SETTINGS)templates/Makefile clean

done:
	@echo '----------> Done'
