#!/bin/bash

# 
# spotContractions.bash                                                               
# 
# D. Clarke 
# 
# I keep putting in contractions out of force of habit. 
# 

for file in *.tex
do
    sed -i 's/e'\''ll/e will/g' $file
    sed -i 's/sn'\''t/s not/g' $file
    sed -i 's/dn'\''t/d not/g' $file
done

grep "e'll" *.tex
grep "sn't" *.tex
grep "dn't" *.tex
