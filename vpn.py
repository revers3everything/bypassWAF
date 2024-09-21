import os
import subprocess
from datetime import datetime
os.system("clear")
puerto = 1

#Scan each 10 ports with different IP

while puerto <= 65535:
    inf = subprocess.check_output("windscribe connect", shell=True)
    inf = inf.decode("utf-8")
    print(inf)
    inf = inf.splitlines()[3]
    indice = inf.find("to")
    ip = inf[indice+3:]
    fecha_hora = str(datetime.now())

    if puerto == 65531:
        comando = "nmap -p %d-%d ip" %(puerto, puerto+4)
        archivo_nombre = "Rango %d-%d_%s_%s.txt" %(puerto, puerto+4, ip, fecha_hora)
    else:
        comando = "nmap -p %d-%d ip" %(puerto, puerto+9)
        archivo_nombre = "Rango %d-%d_%s_%s.txt" %(puerto, puerto+9, ip, fecha_hora)
    
    archivo = open(archivo_nombre, "w")
    salida = subprocess.check_output(comando, shell=True)
    print(salida)
    archivo.write(salida.decode("utf-8"))
    archivo.close()
    puerto = puerto + 10