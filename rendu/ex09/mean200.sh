#!/bin/bash

while read stdin; do
	mean=$(($mean+$stdin))
	div=$(($div+1))
done
mean=$(($mean/$div))
echo "$mean"
