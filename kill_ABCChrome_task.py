import subprocess

#task Kill command

command = "TASKKILL /F /IM ABCChrome86.exe /T"

 

 

processs = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

 

stdout, stderr = processs.communicate()

 

 

if processs.returncode==0:

    print("Command Sucessfull")

    print("Output:",stdout.decode())

else:

    print("Command Successful")

    print("Error:",stderr.decode())