# (Syntax: open('filename',mode='',encoding='',))
f = open('file-handling.txt','w')
f.write('''hello
my''')
f.write("name\nis\nPrashast")
f.close()

# Text mode gives decoded data
# (mode = 'r') this is text read 
f = open('file-handling.txt',mode='r')
data =f.read()
print(data)
f.close()

# Binary mode gives encoded data
# (mode = 'rb') this  is binary read
f = open('file-handling.txt',mode='rb')
data =f.read()
print("This is encoded data:",data)
f.close()