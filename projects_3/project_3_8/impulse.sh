#!/bin/bash

if [ $# -lt 2 ]; then echo "Ошибка, нужно 2 аргумента"; exit 1; fi

gen="$1"
level="$2"
echo "Экспрессия гена $gen составляет $level единиц"
