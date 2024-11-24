import shutil 
import os 
import datetime
import subprocess
import time

now = datetime.datetime.now()
date = now.date()

def log(command):
	with open('command_log.txt', 'a') as log_file:
		try:
			log_file.write(f"executed {command} succsessfully at {now} {command}\n")
		except subprocess.CalledProcessError as e:
			log_file.write(f"Command: {command} failed at {now} with error: \n{e.stderr}\n{command}\n")

def pidlog(pid):
	with open('pid_log.txt', 'a') as log_file:
		try: 
			log_file.write(f"server started at {now} pid\n{pid}\n")
		except subprocess.CalledProcessError as e: 
			log_file.write(f"failed {e.stderr}\n{pid}\n")

def getpid():
	with open('pid_log.txt', 'r') as log_file:
		try:
			for line in reversed(list(log_file)):
				if line.strip():
					return line.strip()
		except subprocess.CalledProcessError as e:
			return None

def starttmux(name, command):
	tmux_command = f"tmux new-session -d "
	process = subprocess.Popen(tmux_command, shell =True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	pid = process.pid
	pidlog(pid)
	if stdout:
		print(stdout.decode())
	if stderr:
		print(stderr.decode())


	mc = f"tmux send-keys -t 0 '{command}' Enter"
	start = subprocess.Popen(mc)




destination = f"/var/lib/pufferpanel/backups/backup_from_{date}"
source = "/var/lib/pufferpanel/servers/2c1ff730/world"

#shuts the server down
pid = getpid()
print(pid)
if pid is not None:
	try:
		subprocess.run(['kill', str(pid)], check= True)
		time.sleep(60)
	except subprocess.CalledProcessError as e:
		print("Error terminating process", e)


#does the copying 
#if not os.path.exists(destination):
#	shutil.copytree(source, destination)
#	log("copytree")
#else:
#	log("tried to backup on the same day do it tommorrow xdd")



#time.sleep(30)
#activates the server again 
start = ['tmux', 'new-seesion', '-s' 'minecraftserver','-d', '"bash"']
command = ['java', '-Xmx22G', '-Xms22G', '-jar', 'fabric-server.jar']
changedir = ['cd', '/var/lib/pufferpanel/servers/2c1ff730']

#starttmux("mcserver", "java -Xmx16G -Xms16G -jar fabricserver.jar ")

#screen = subprocess.run(start)
result = subprocess.Popen(command, stdout=subprocess.PIPE)
#while True:
#	output = result.stdout.readline()
#       if output == b'':
#   		break
#	print(output.decode())
pid = result.pid 
# logs the pid so i know which process to kill when starting it again
pidlog(pid)
