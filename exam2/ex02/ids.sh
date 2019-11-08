#!/bin/bash

cat /etc/passwd | cut -d: -f4 | sort -n | uniq

