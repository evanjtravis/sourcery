#!/bin/bash

SAVED="/home/ejtravis/.ptpython/history.saved"
touch $SAVED
echo '##############################' >> $SAVED
date +%F_%T >> $SAVED
echo '##############################' >> $SAVED
cat ~/.ptpython/history | sed 's/^\+//' | sed 's/^\#.*//' | tr -s '\n' >> $SAVED
cat $SAVED | less

