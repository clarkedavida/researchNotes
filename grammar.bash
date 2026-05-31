#!/bin/bash

# 
# grammar.bash                                                               
# 
# D. Clarke 
# 
# I keep putting in contractions out of force of habit. Also I
# decide to use formulae instead of formulas and so on.
# 

# Claude helped with this
CURL=$(python3 -c "import sys; sys.stdout.write('\u2019')")

for file in *.tex
do
    sed -i 's/e'\''ll/e will/g' $file
    sed -i "s/e${CURL}ll/e will/g" $file
    sed -i 's/ou'\''re/ou are/g' $file
    sed -i "s/ou${CURL}re/ou are/g" $file
    sed -i 's/sn'\''t/s not/g' $file
    sed -i "s/sn${CURL}t/s not/g" $file
    sed -i 's/can'\''t/cannot/g' $file
    sed -i "s/can${CURL}t/cannot/g" $file
    sed -i 's/don'\''t/do not/g' $file
    sed -i "s/don${CURL}t/do not/g" $file
    sed -i 's/dn'\''t/d not/g' $file
    sed -i "s/dn${CURL}t/d not/g" $file
    sed -i 's/ormulas/ormulae/g' $file
    sed -i 's/ell-defined/ell defined/g' $file
    sed -i 's/inimums/inima/g' $file
    sed -i 's/aximums/axima/g' $file
    sed -i 's/nsatzes/nsätze/g' $file
    sed -i 's/What'\''s/What is/g' $file
    sed -i "s/What${CURL}s/What is/g" $file
    sed -i 's/what'\''s/what is/g' $file
    sed -i "s/what${CURL}s/what is/g" $file
    sed -i 's/That'\''s/That is/g' $file
    sed -i "s/That${CURL}s/That is/g" $file
    sed -i 's/that'\''s/that is/g' $file
    sed -i "s/that${CURL}s/that is/g" $file
    sed -i 's/let'\''s/let us/g' $file
    sed -i "s/let${CURL}s/let us/g" $file
    sed -i 's/Let'\''s/Let us/g' $file
    sed -i "s/Let${CURL}s/Let us/g" $file
    sed -i 's/Aren'\''t/Are not/g' $file
    sed -i "s/Aren${CURL}t/Are not/g" $file
    sed -i 's/aren'\''t/are not/g' $file
    sed -i "s/aren${CURL}t/are not/g" $file
    sed -i 's/it'\''s/it is/g' $file
    sed -i "s/it${CURL}s/it is/g" $file
    sed -i 's/It'\''s/It is/g' $file
    sed -i "s/It${CURL}s/It is/g" $file
done
