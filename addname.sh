#!/bin/bash
function rename()
{
    cfilelist=$(ls -A)
    for cfilename in $cfilelist  
    do   
        if [[ $cfilename != 'addname.sh' ]]
        then 
            mv $cfilename $1${cfilename}	# 语句1
        fi
    done 
}
rename $1 
