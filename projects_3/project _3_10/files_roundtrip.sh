#!/bin/bash

for i in {1..10}; do
	touch  "test$i.txt"
	echo "Создал файл: test$i.txt"
done

for I in {10..1..1}; do
    while [ -e "test$I.txt" ]; do
    rm "test$I.txt"
    echo "Удалил файл test$I.txt"
    done
done

