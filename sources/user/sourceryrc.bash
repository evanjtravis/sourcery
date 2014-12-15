echo -e "\t${USR}/sourceryrc.bash"

#####################################################################
# Environment Variables
#####################################################################

export INIT='--initialize'
export CLEAN='--clean'
export RESET='--reset'

alias sourcery.clean="sourcery.bash ${CLEAN};sourcery"
alias sourcery.init="sourcery;sourcery.bash ${INIT};sourcery"
alias sourcery.reset="sourcery.bash ${RESET};sourcery"
alias tosourcery="cd ${SETTINGS}"

#####################################################################
# Favorites
#####################################################################


