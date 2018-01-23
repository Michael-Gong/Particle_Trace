#!/bin/bash
for ((ia=0;ia<=40;ia++))
do
  for ((ig=0;ig<=40;ig++))
  do
    mkdir Dataa$[ia*5+20]g$[ig*75+500]
    cd Dataa$[ia*5+20]g$[ig*75+500]
    cp ../input.deck ./
    sed -i s%'a0=50'%'a0='$[ia*5+20]%g ./input.deck
    sed -i s%'gamma0=-500'%'gamma0=-'$[ig*75+500]%g ./input.deck
    cd ../
    echo distribution in Dataa$[ia*5+20]g$[ig*75+500] is ok!
  done
done
