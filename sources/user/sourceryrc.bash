echo -e "\t${USR}/sourceryrc.bash"

#####################################################################
# Environment Variables
#####################################################################

INIT='--initialize'
CLEAN='--clean'
RESET='--reset'

alias sourcery.clean="sourcery.bash ${CLEAN};sourcery"
alias sourcery.init="sourcery;sourcery.bash ${INIT};sourcery"
alias sourcery.reset="sourcery.bash ${RESET};sourcery"
alias tosourcery="cd ${SETTINGS}"

#####################################################################
# Favorites
#####################################################################


