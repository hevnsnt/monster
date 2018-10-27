#!/bin/sh

# This installs the monster in a box as a service and will start on boot.
#
# If you want to stop the monster, type the following command at the command prompt
#
# sudo systemctl stop monster.service
# 
# If you want to restart it, you just need to type the following
# sudo systemctl start myscript.service
#
#
sudo cp ./.install/monster.service /etc/systemd/system/monster.service
sudo systemctl enable monster.service