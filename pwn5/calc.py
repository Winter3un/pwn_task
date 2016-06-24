end = 'DEADBEEF'
# start = 5381
import sys   
sys.setrecursionlimit(1000000)

def get(end):
	if end == 1234:
		return True
	if end <1234:
		return False
	for x in range(1,0xff+1):
		if (end - 12) % 34 ==0:
			flag = get((end - 12) / 34 -x)
			if flag:
				print hex(end),hex(x)
				return True
			else:
				return False
				
for x in range(0,0xffffff):
	tmp  = int(hex(x).replace('0x','')+end,16)
	# if (tmp - 0xa) % 33 ==0:
	# 	if get((tmp - 0x0a) / 33):
	# 		print hex(tmp),hex(0x0a)
	# 		print 'end'
	# 		exit(0)
	if get(tem,16):
		print 'end'