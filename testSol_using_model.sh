#! /bin/bash

modelFile=$1

solFile=$2

if [ ! -f "$modelFile" ]
then
    echo "$modelFile: No such file"
    exit 1
fi

if [ ! -f "$solFile" ]
then
    echo "$solFile: No such file"
    exit 1
fi


testSol="/tmp/testSol.py"

sed -e 's/ / = int\(round\(/g' -e 's/$/\)\)/g' "$solFile" > $testSol

echo "constraints = [" >> $testSol

sed -n '/Subject/,/Binary/{//!p;}' "$modelFile"| sed -e 's/ = / == /g' -e 's/ x/ \* x/g' -e 's/ y/ \* y/g' -e 's/$/,/g'|sed -e 's/- \*/-/g' -e 's/+ \*/+/g' >> $testSol

echo "]" >> $testSol

echo 'print("Does the solution satsify all the constraints? %s" %str(all(constraints)))' >> $testSol

python $testSol
