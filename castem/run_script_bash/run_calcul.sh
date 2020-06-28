#!/bin/bash

matrice="matrice.csv"
mfront="Voce_IRR.mfront"
data_calcul="data_calcul.dgibi"
calcul="NT_calc.dgibi"
post="NT_post.dgibi"

OLDIFS=$IFS
IFS=";"

[ ! -f $matrice ] && { echo "$matrice file not found"; exit 99; }
while read R0 R1 GTN LINEAR PHI
do
  echo "NT : $R0"
  echo "Notch radius : $R1"
  echo "Damage : $GTN"
  echo "Linear elements : $LINEAR"
  echo "Thermal fluence : $PHI"
  PHI0=${PHI:0:3}

# Calcul
  sed -i "/R0/c\ $R0 R0" $data_calcul
  sed -i "/R1/c\ $R1 R1" $data_calcul
  sed -i "/GTN/c\ $GTN GTN" $data_calcul
  sed -i "/LINEAR/c\ $LINEAR LINEAR" $data_calcul
  sed -i "/PHI0/c\ $PHI0 PHI0" $data_calcul


# Creer le repertoire de l essai
  mkdir -p NT"$R0"_phi$PHI0
  cd NT"$R0"_phi$PHI0
  cp ../NT$R0.med .
  cp ../$mfront .
  cp ../$data_calcul .
  cp ../$calcul .
  cp ../$post .

# Calcul
  mfront --obuild --interface=castem $mfront 

# Calcul
  castem19 $calcul > out_calcul_NT$R0

# Post-traitement
  mkdir -p POST/
  cd POST/
  cp ../*.sauv .
  cp ../$data_calcul .
  cp -r ../src/ .
  cp ../$post .
  castem19 $post > out_post_NT$R0

# Sortir du repertoire d essai
  cd ../..

done < $matrice
IFS=$OLDIFS
