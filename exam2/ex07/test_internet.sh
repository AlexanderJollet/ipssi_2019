#!/bin/bash

set -e

if [ -z $1 ]; then
	echo "donnez un nom de site"
	exit 1

	else
		if curl -s -I $1 >/dev/null; then
			 echo $(date "+%Y-%m-%d:%H:%M:%S, internet ok") >> internet.log
		else
			echo $(date "+%Y-%m-%d:%H:%M:%S, test FAIL") >> internet.log
			exit 2
		fi
fi

exit 0
