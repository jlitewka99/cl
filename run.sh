#!/bin/bash

find . -maxdepth 1 -type f \( -iname \*.pdf -o -iname \*.jpg \) -print0 | sort -z | while read -d $'\0' filepicture
do


	

	echo $filepicture

	part1picture=$(dirname "$filepicture") 
	part2picture=$(basename "$filepicture")

	part2picture=${part2picture//[[:blank:]]/}

	part1picture="${part1picture:1}"

	onlyname="${part2picture%.*}"

	echo "${onlyname}"
	mkdir "${onlyname}"

	mv "${filepicture}" "${onlyname}"/example.pdf

	cp script1.sh "${onlyname}"
	cp script2.sh "${onlyname}"/sc2.sh
	cp script3.sh "${onlyname}"/sc3.sh
	cp a.py "${onlyname}"
	cp b.py "${onlyname}"
	cp c.py "${onlyname}"

	echo "${onlyname}"/script1.sh
	cd  "${onlyname}"
	sh script1.sh
	cd ..


	




done 