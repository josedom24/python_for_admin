f=open("/etc/hosts","r")
lineas=f.readlines()
lineas.insert(3,"192.168.6.5\tpepito.com\n")
f.close()
f=open("/etc/hosts","w")
for linea in lineas:
	f.write(linea)
f.close()


