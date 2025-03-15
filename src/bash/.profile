#
# ~/.profile
#
#

[[ "$XDG_CURRENT_DESKTOP" == "KDE" ]] || export QT_QPA_PLATFORMTHEME="qt5ct"
export EDITOR=/usr/bin/mcedit

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/Data/System/bin" ]; then
    PATH="./:$HOME/Data/System/bin:$PATH"
fi

#  Go Lang
export GOPATH=$HOME/go

#if [ -d "$HOME/Data/Go/Path" ]; then
#    export GOPATH="$HOME/Data/Go/Path"
#fi

