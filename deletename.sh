#!/bin/bash
function rename()
{
    cfilelist=$(ls -A)
    for cfilename in $cfilelist  
    do   
        if [[ $cfilename != .DS_Store ]]
        then 
            mv $cfilename `echo $cfilename|sed "s/$1//g"`	# 语句1
        fi
    done 
}
rename 

