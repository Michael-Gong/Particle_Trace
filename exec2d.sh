#!/bin/bash
for ((ia=0;ia<=20;ia++))
do
  for ((iw=0;iw<=20;iw++))
  do
    date >> finish.deck
    mv Dataa$[ia*12+210]w$[iw*4+30]rr Data
    ./bin/gztrace
    mv Data Dataa$[ia*12+210]w$[iw*4+30]rr
    echo Dataa$[ia*12+210]w$[iw*4+30]rr is finished! >> finish.deck
  done
done
