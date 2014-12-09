#!/bin/bash
# Get line number ranges of a file.

FILENAME=$1
START=$2
END=$3

NUMOFLINES=$(wc -l < "$FILENAME")

ENDDIFF=$(( NUMOFLINES - END ))

if [ "$START" -lt "$ENDDIFF" ]; then
    < "$FILENAME" head -n $END | tail -n +$START
else
    < "$FILENAME" tail -n +$START | head -n $(( END-START+1 ))
fi
