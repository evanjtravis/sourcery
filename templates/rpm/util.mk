check_defined = \
    $(foreach 1,$1,$(__check_defined))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $(value 2), ($(strip $2)))))

# Usage
# $(call check_defined, var [additoinal vars][, message-to-print])
# If the variable(s) are not defined, make errors and prints a message.
