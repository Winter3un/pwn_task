end = '2029bc3c'

import sys   
sys.setrecursionlimit(1000000)

def get(end):
	if end == 1234:
		return True
	if end <1234:
		return False
	if (end - 12) % 34 !=0:
		return False
	for x in xrange(1,0xff+1):
		flag = get((end - 12) / 34 -x)
		if flag:
			print hex(end),hex(x)
			return True
		else:
			continue
				
for x in xrange(0,0xfffffff):
	tmp  = int(hex(x).replace('0x','')+end,16)
	if get(tmp):
		print 'end'