#!/bin/bash
#
#   RUN AS SUDO
#
apt update
apt install autoconf automake
# Download coap-client package
cd /usr/src
wget http://downloads.sourceforge.net/project/libcoap/coap-18/libcoap-4.1.1.tar.gz

# Install coap-client
tar -xf libcoap-4.1.1.tar.gz
cd libcoap-4.1.1
autoconf
./configure
make
cp examples/coap-client /usr/local/bin/
