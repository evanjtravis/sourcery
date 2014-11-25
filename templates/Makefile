SETTINGS=$(HOME)settings/
HERE=$(SETTINGS)templates/

all: bash.o source.o

bash.o:
	python copy_templates.py $(HERE) ~/

source.o:
	source ~/.bash_profile
