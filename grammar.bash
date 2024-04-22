#!/bin/bash

# 
# grammar.bash                                                               
# 
# D. Clarke 
# 
# I keep putting in contractions out of force of habit. Also I
# decide to use formulae instead of formulas and so on.
# 

for file in *.tex
do
    sed -i 's/e'\''ll/e will/g' $file
    sed -i 's/sn'\''t/s not/g' $file
    sed -i 's/can'\''t/cannot/g' $file
    sed -i 's/don'\''t/do not/g' $file
    sed -i 's/dn'\''t/d not/g' $file
    sed -i 's/ormulas/ormulae/g' $file
    sed -i 's/inimums/inima/g' $file
    sed -i 's/aximums/axima/g' $file
    sed -i 's/nsatzes/nsätze/g' $file
done
