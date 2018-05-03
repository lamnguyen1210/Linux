#!/bin/sh
echo "nhap ten file:"
read filename
if [ ! -f "$filename" ]; then
	echo " $filename not exists"
	exit 1
fi
answer=""
count=0
numlines=`wc -l $filename|sed 's/^ *//'|cut -d " " -f 1`
echo " so dong: $numlines"
while [ "$answer" != "n" ]
do
	echo "tiep tuc(y/n)?"
	read answer
	if [ "$answer" = "y" -o "$answer" = "Y" ]; then
		if [ $count = $numlines ]; then
			echo "doc het file roi"
			exit 0
		fi
	fi
	count=$(($count+1))
	sed -n ${count}p $filename
done
exit 0
