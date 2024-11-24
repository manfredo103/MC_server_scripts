If you chose to use my badly written scripts, few things to setup before it works.

1. move all .py files except for garbage.py to the server file where you store the minecraft server
2. make a new dir using mkdir to store your backup worlds
3. change the dirs in all .sh files
4. make a crontab entry using "crontab -e" to schedule when what script should be done
5. move .sh to root dir so crontab can find them i guess 
