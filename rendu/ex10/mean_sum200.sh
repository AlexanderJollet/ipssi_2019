#!/bin/bash

while read stdin; do

	mean=$(($mean+$stdin))
	div=$(($div+1))
done
meana=$(($mean/$div))
echo "$meana"
echo "$mean"
