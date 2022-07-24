#!/bin/bash

files=""

## przesyłanie obrazów
find . -type f \( -iname \*.png -o -iname \*.jpg \) -print0 | sort -z | while read -d $'\0' filepicture
do


	

	echo $filepicture

	part1picture=$(dirname "$filepicture") 
	part2picture=$(basename "$filepicture")

	part2picture=${part2picture//[[:blank:]]/}

	part1picture="${part1picture:1}"

	convert "${filepicture}" -trim "singlepages/new_${part2picture}"



	rm -rf "${filepicture}"




done 

convert -append "singlepages/*.png" out.png

python3 c.py


