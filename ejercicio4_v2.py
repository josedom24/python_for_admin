import sys
if len(sys.argv) != 2:
	print "Debes poner el usuario como parametro"
	sys.exit(-1)
usuario=sys.argv[1]
f=open("/etc/passwd","r")
lineas=f.read()
if lineas.find(usuario)==-1:
	print "Usuario no existe"
if lineas.find(usuario+":x:0:0")==-1:
	print "No es administrador"
else:
	print "Es administrador"


