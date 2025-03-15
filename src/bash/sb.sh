#!/bin/bash

function hex2string () {
  I=0
  while [ $I -lt ${#1} ];
  do
    echo -en "\x"${1:$I:2}
    let "I += 2"
  done
}

function ucs2string () {
	L=4
	I=0
  
	while [ $I -lt ${#1} ]; do
		echo -en "\U"${1:$I:$L}
		let "I += $L"
	done

	echo
}

# hex2string "48656C6C6F2074686572652021"

#Привет
#U+041F U+0440 U+0438 U+0432 U+0435 U+0442
ucs2string "041F044004380432043504420021"


