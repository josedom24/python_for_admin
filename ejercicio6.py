import os
usuario=raw_input("Usuario:")
usuariol=raw_input("Nombre:")
f=open("/etc/passwd","a")
f.write(usuario+":x:2000:2000:"+usuariol+",,,:/home/"+usuario+":/bin/bash")
f.close()

f=open("/etc/group","a")
f.write(usuario+":x:2001:")
f.close()

os.mkdir("/home/"+usuario)

