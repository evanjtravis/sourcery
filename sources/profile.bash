#!/usr/bin/bash

# PROMPT_COMMAND is cleared here and added to later on during 'sourcery' commands.
export PROMPT_COMMAND=""

NAME=$(uname -o)
export MYNAME

if [ "${NAME}" == "Cygwin" ]; then
    MYNAME=${USER}
else
    MYNAME=${TTY_OWNER}
fi

export MYHOME=/home/${MYNAME}
export SOURCERY=${MYHOME}/sourcery
export SOURCES=${SOURCERY}/sources
export STATIC=${SOURCERY}/static

#====================================================================
# Git Aware Prompt
#--------------------------------------------------------------------
export GITAWAREPROMPT=${SOURCES}/utils/git-aware-prompt
source $GITAWAREPROMPT/main.sh
export PS1="\n\[$txtgrn\]\u@\h\n\$git_branch\[$txtred\]\$git_dirty\[$txtylw\]@: \w\n\[$txtrst\]\$ "
#====================================================================

echo -e "Sourced:\n\t${SOURCES}/profile.bash"

source ${SOURCES}/all/main

