import commands
usuarios=[]
data = commands.getoutput("who")
data=data.split("\n");
for linea in data:
	texto=linea.split(" ")
	if not texto[0] in usuarios:
		usuarios.append(texto[0])
for usuario in usuarios:
	print usuario

