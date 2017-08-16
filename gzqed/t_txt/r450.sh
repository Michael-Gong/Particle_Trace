#!/bin/bash
for file in *.txt
do
  mv $file "q250_"${file#.txt}
done
