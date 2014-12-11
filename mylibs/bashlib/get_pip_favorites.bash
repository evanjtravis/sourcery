echo "Installing python packages using pip."

if [ -d "/services" ]; then
    echo "Cannot install pip on this system."
    exit 0
fi

#####################################################################
# Start Pip Package Installation
#####################################################################
