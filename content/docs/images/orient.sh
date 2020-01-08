#!/bin/bash

JHEAD=jhead
SED=sed
CONVERT=convert

for f in *.JPG
do
        orientation=$($JHEAD -v $f | $SED -nr 's:.*Orientation = ([0-9]+).*:\1:p')

        if [ -z $orientation ]
        then
                orientation=0
        fi

        if [ $orientation -gt 1 ]
        then
                echo Rotating $f...
                mv $f $f.bak
                $CONVERT -auto-orient $f.bak $f
        fi
done

