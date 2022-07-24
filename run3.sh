#!/bin/bash

find . -type f \( -iname sc2.sh \) -print0 | sort -z | while read -d $'\0' filepicture
do


	

	echo $filepicture

	part1picture=$(dirname "$filepicture") 
	part2picture=$(basename "$filepicture")

	part2picture=${part2picture//[[:blank:]]/}

	#part1picture="${part1picture:1}"

	onlyname="${part2picture%.*}"

	cp example99.png "${part1picture}"/singlepages
	
	cd "${part1picture}"


	sh sc3.sh

	rm -rf a.py
	rm -rf b.py
	rm -rf c.py
	rm -rf sc3.sh
	rm -rf sc2.sh
	rm -rf script1.sh
	rm -rf out
	rm -rf singlepages
	rm -rf example.pdf

	cd ..

	mkdir -p drive/MyDrive/Matury/"${part1picture}"

	cp -R "${part1picture}" drive/MyDrive/Matury/



done 