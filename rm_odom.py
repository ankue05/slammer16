import sys

fn = sys.argv[1]

f = open(fn,'r')

new_f= ''

for line in f.readlines():
	if line.startswith('ODOM'):
		continue
	else:
		new_f += line

f.close()

f = f = open(fn,'w')
f.write(new_f)
f.close
