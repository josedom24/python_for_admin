import sys
coincidencia = False
try:
    usuario = sys.argv[1]
    with open('/etc/passwd','r') as doc:
        passwd = doc.readlines()
        for i in passwd:
            if i.split(":")[0] == usuario:
                coincidencia = True
                if int(i.split(":")[3]) == 0:
                    print("El usuario introducido es administrador.")
                else:
                    print("El usuario introducido no es administrador.")
        if coincidencia == False:
            print("El usuario introducido no existe.")
except:
    print("No has introducido ningún usuario.")
