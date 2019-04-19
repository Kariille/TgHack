from pwn import *
context(arch = 'i386', os = 'windows')

conn = remote('math.tghack.no', 10000)


c=0
while c < 101:

    r = conn.recvline()
    print(r)
    r = conn.recvline()
    print(r)
    liste = r.split()
    print(liste)
    if liste[1] == '+':
         a = int(liste[0]) + int(liste[2])
         pass
    else:
        if  liste[1] == '-':
            a = int(liste[0]) - int(liste[2])
            pass
        else:
            if liste[1] == '*':
                a = int(liste[0]) * int(liste[2])
                pass
            else:
                a = int(liste[0]) / int(liste[2])
                pass
            pass
    print(a)
    re = conn.send(str(a))
    print(re)
    r = conn.recvline()
    print(r)
    
    c += 1
    pass

