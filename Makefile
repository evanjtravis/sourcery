ROOT=~/settings/
BASH=$(ROOT)bash/
MAIN=$(ROOT)main/

all: bash.o source.o

bash.o:
	cp $(MAIN).bash_profile.main ~/.bash_profile
	cp $(MAIN).gitconfig.main ~/.gitconfig

source.o:
	source ~/.bash_profile
