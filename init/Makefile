all:

init: .FORCE
	make -f $(SETTINGS)/templates/Makefile
	$(SETTINGS)/vim/vundle.sh
	$(SETTINGS)/init/init.sh

clean:
	make -f $(SETTINGS)/templates/Makefile clean

done:
	@echo '----------> Done'

.FORCE:
