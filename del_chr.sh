#!/bin/bash

if [[ $1 =~ ../data/(.+\..)+ ]]; then
ref = $[BASH_REMATCH[2]]
fi

echo $1
echo ref

#sed -e "s/Chr//" $1 >    

