import shutil 
import os 
import datetime
import subprocess

now = datetime.datetime.now()
date = now.date()

def log(command):
	with open('command_log.txt', 'a') as log_file:
		try:
			log_file.write(f"Command: {command} executed succsessfully at {now}\n")
		except subprocess.CalledProcessError as e:
			log_file.write(f"Command: {command} failed at {now} with error: \n{e.stderr}\n")

destination = f"/var/lib/pufferpanel/backups/backup_from_{date}"
source = "/var/lib/pufferpanel/servers/2c1ff730/world"

#shuts the server down


#does the copying 
if not os.path.exists(destination):
	shutil.copytree(source, destination)
	log("copytree")
	print("it has copied hopium")
else:
	log("tried to backup on the same day do it tommorrow xdd")


#activates the server again 

command = ['java', '-Xmx16G', '-Xms16G', '-jar', 'fabric-server.jar']
changedir = ['cd', '/var/lib/pufferpanel/servers/2c1ff730']

try:
	start = subprocess.run(changedir, capture_output=True, text=True, check=True)
	print(start.stdout)
	result = subprocess.run(command, capture_output=True, text=True, check=True)
	print(result.stdout)
	log(f"server start")
except:
	log(f"server start")
