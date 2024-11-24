#!/bin/bash 


#set up dir
directory="/var/lib/pufferpanel/backups/"

#change dir
cd "$directory"

#start backup
python3 garbage.py
