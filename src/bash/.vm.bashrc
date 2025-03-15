# .vm.bashrc 

MC=$(ps $PPID | grep 'mc')

if [ -n "$MC" ]; then
    MC="mc%"
fi

if [ -z "$SU" ]; then
	SU=$(ps $PPID | grep 'sudo')

	if [ -n "$SU" ]; then
	    export SU="SU*"
	fi
fi

PS1='\[\e[01;03;38;05;${PCOLOR}m\]${SU}${MC}\u@\h:\W\$ \[\e[22;23m\]'

# Add to ~/.bashrc:
# PCOLOR=94  # Local host user
# PCOLOR=162 # Local host superuser
# PCOLOR=25  # Remote host user
# PCOLOR=91  # Remote host superuser

# New colors
# #FFB000 = 214

# [[ -f ~/Data/System/bash/.vm.bashrc ]] && . ~/Data/System/bash/.vm.bashrc

# Bag in cdrkit package
alias wodim='wodim dev=/dev/sr0'
 
