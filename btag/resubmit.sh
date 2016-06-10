#!/bin/bash
# usage source resubmit.sh condorDir [submit]
condorDir=$1
submit=$2

#find $condorDir -name "*.err" | xargs grep "Error"
#echo $fileList
filesWithError="$(grep -l 'Error' $condorDir/*.err)"

for fileWithError in $filesWithError; do
    echo Following job had an error : 
    echo "      $fileWithError"
    stringsError="$(grep 'Error' $fileWithError)"
    shouldResubmit=false 
    for stringError  in $stringsError; do
        if [[ $stringError == *".root" ]]; then
            if test -e $stringError; then
                shouldResubmit=true
                break
            fi
        fi
    done
    if $shouldResubmit; then
        cmdFileName="${fileWithError/err/cmd}"
        echo "      File actually exists"
        ls $stringError
        if [ "$submit" == "submit" ]; then
            echo "      Resubmitting $cmdFileName..."
            condor_submit $cmdFileName
        else
            echo "      Will though not resubmit the job, use 'submit' option to do so"
        fi
    else
        echo "      Normal since file does not exists"
    fi
done
