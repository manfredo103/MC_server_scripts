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


def check_process_running(pid):
    """Checks if a process is running based on its PID.

    Args:
        pid (int): The PID of the process to check.

    Returns:
        bool: True if the process is running, False otherwise.
    """

    try:
        # Use `ps` command to check process status
        output = subprocess.check_output(["ps", "-p", str(pid)])
        return True
    except subprocess.CalledProcessError:
        # Process is not running
        return False

def startserver():
	result = subprocess.Popen(command, stdout=subprocess.PIPE)
	pid = result.pid 
	pidlog(pid)

command = ['java', '-Xmx22G', '-Xms22G', '-jar', 'fabric-server.jar']



destination = f"/var/lib/pufferpanel/backups/backup_from_{date}"
source = "/var/lib/pufferpanel/servers/2c1ff730/world"

#Gets Process ID from its log 
pid = getpid()
print(pid)
#does something when it gets something
if pid is not None:
	#checks if server is running Status is either True or False
	Status = check_process_running(pid)
	print(Status)
	#If condition is only met if Status is False
	if not Status:
		print("starting Server")
		#starts server
		startserver()
		log("automatic server start")


# rest is irrelevant

start = ['tmux', 'new-seesion', '-s' 'minecraftserver','-d', '"bash"']
changedir = ['cd', '/var/lib/pufferpanel/servers/2c1ff730']

#starttmux("mcserver", "java -Xmx16G -Xms16G -jar fabricserver.jar ")

#screen = subprocess.run(start)
#while True:
#	output = result.stdout.readline()
#	if output == b'':
#   		break
#	print(output.decode())
# logs the pid so i know which process to kill when starting it again
