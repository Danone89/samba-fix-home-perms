import os
import subprocess
import re
for  dirname in os.listdir('./'):
	print(dirname)
	output = subprocess.Popen(["wbinfo", "-i "+dirname],stdout=subprocess.PIPE).communicate()[0]
	p = re.compile("3000([0-9]{3})")
	owner = p.search(output)
	if(owner):
		print(owner.group())
		subprocess.Popen(["chown", "-R",owner.group(),dirname],stdout=subprocess.PIPE).communicate()[0]
