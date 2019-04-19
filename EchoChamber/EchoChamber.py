from pwn import *
context(arch = 'i386', os = 'windows')

conn = remote('echo.tghack.no', 5555)


c=0
while c < 51:

    r = conn.recvline()
    print(r)
    conn.send(r)
    c += 1
    pass

