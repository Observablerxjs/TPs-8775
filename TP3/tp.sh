#!/bin/bash

key="$1"

case $key in
    -e)
    EX_PATH="$2"
    shift
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;

esac
shift
done

python3 ./sol.py $EX_PATH