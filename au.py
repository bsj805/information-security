from pwn import *
import binascii
def hextobin(a):
    return str(int(a,16)).encode()


r= process("./automation")

r.recvuntil("string:")
numb=r.recvuntil("\n")
print("str:",numb,"@@")
a=numb.decode()
print(a)
idx=a.find('0x')
endidx=a.find('\x1b[0')
newstr=a[idx:endidx]
print("finalstr:",newstr)#,"\n",hextobin(newstr))
r.sendline(hextobin(newstr))

r.recvuntil("string:")
numb=r.recvuntil("\n")
a=numb.decode()
idx=a.find("\x1b[34m")
endidx=a.find("\x1b[0")
newstr=a[idx+5:endidx]
r.sendline(binascii.hexlify(newstr))

r.recvuntil("string:")
numb=r.recvuntil("\n")
a=numb.decode()
idx=a.find("\x1b[34m")
endidx=a.find("\x1b[0")
newstr=a[idx+7:endidx]
r.sendline(binascii.unhexlify(newstr))

r.recvuntil("solve:")
numb=r.recvuntil("\n")
a=numb.decode()
idx=a.find("\x1b[34m")
endidx=a.find("\x1b[0")
newstr=a[idx+5:endidx]
plusidx=newstr.find("+")
a=[:plusidx]
b=[plusidx+1:]

r.sendline(str(a+b).encode())





