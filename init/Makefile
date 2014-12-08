all:

init: .FORCE
	make -f $(SETTINGS)/templates/Makefile
	$(SETTINGS)/vim/vundle.sh
	$(SETTINGS)/init/init.sh

clean:
	make -f $(SETTINGS)/templates/Makefile clean
	rm -f $(SETTINGS)/init/get-pip.py

done:
	@echo '----------> Done'

.FORCE:
