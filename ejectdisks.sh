#!/bin/zsh
#
# File: ejectdisks.sh
# Description: Eject all external disks. To be called by keyboard maestro, probably.
# Author: Andy Holt
# Date: Sat 18 Jan 2020 15:24

# ensure time machine backup isn't currently running
tmutil stopbackup

# get list of currently mounted disks
mounted_disks=$(diskutil list external | awk '/external/ { print $1; }')

# turn list into an array
disk_array=($(echo $mounted_disks))

for d in "${disk_array[@]}"
do
    # echo "Ejecting disk " $d
    diskutil eject $d
done
