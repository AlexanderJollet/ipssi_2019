#!/usr/bin/python3

img = 'image:'

images = []

with open('docker-compose.yml') as f:
   for line in f:
       if img in line:
           print(line.strip().split()[1])

f.close
