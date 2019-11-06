#!/bin/bash

set -e

if curl -s -I  $1 >/dev/null ;then
	echo "OK"
else

	echo "FAIL"
fi
