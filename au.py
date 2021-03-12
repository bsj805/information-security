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
r.sendline(binascii.hexlify(newstr.encode()))

r.recvuntil("string:")
numb=r.recvuntil("\n")
a=numb.decode()
idx=a.find("\x1b[34m")
endidx=a.find("\x1b[0")
newstr=a[idx+7:endidx]
r.sendline(binascii.unhexlify(newstr.encode()))

r.recvuntil("this:")
numb=r.recvuntil("\n")
a=numb.decode()
idx=a.find("\x1b[34m")
endidx=a.find("\x1b[0")
newstr=a[idx+5:endidx]
plusidx=newstr.find("+")
a=newstr[:plusidx]
b=newstr[plusidx+1:]
a=a.strip()
b=b.strip()

r.sendline(str(int(a)+int(b)).encode())

r.recvuntil("this:")
numb=r.recvuntil("\n")
a=numb.decode()
idx=a.find("\x1b[34m")
endidx=a.find("\x1b[0")
newstr=a[idx+5:endidx]
newstr=newstr.strip()
print("lv5")
print(newstr)
li1=newstr.split(" ")
li1.sort()
li2=[]
li3=[]
li4=[]
for i in li1:
	li2.append(str(i).strip())
for i in li2:
	li3.append(len(i))
count=0
tempstr=""
while(len(li3)>0):
	mini=100
	minidx=-1
	for idx,val in enumerate(li3):#length array
		if mini>val:
			mini=val
			minidx=idx
	ma=li3.pop(minidx)
	mb=li2.pop(minidx)
	li4.append(mb)
print("sortedlist:",li4)
li5=[]
tempstr=""
for i in li4:
	li5.append(int(i))
	tempstr+=i+" "
tempstr=tempstr[:-1]
r.sendline(tempstr.encode())


			

	



