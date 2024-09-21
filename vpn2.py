import os
import subprocess
from datetime import datetime
os.system("clear")
puerto = 1

##Scan each 10 ports with different IP and save the results
a = open("open_ports.txt","w")
c = open("closed_ports.txt","w")
f = open("filtered_ports.txt","w")
while puerto <= 65535:
    inf = subprocess.check_output("windscribe connect", shell=True)
    inf = inf.decode("utf-8")
    n = len(inf.splitlines())
    inf = inf.splitlines()[n-1]
    indice = inf.find("to")
    ip = inf[indice+3:]
    ip = ip.replace(" ","")
    print(ip)
    fecha_hora = str(datetime.now())
    fecha_hora = fecha_hora.replace(" ","_")
    fecha_hora = fecha_hora[0:19]
    if puerto == 65531:
        comando = "nmap -p %d-%d -Pn -n 127.0.0.1 -oA Rango%d-%d_%s_%s " %(puerto,puerto+4, puerto,puerto+4,ip,fecha_hora)
    else:
        comando = "nmap -p %d-%d -Pn -n 127.0.0.1 -oA Rango%d-%d_%s_%s " %(puerto,puerto+9, puerto,puerto+9,ip,fecha_hora)
    
    salida = subprocess.check_output(comando, shell=True)
    salida = salida.decode("utf-8")
    for linea in salida.splitlines():
        if linea.find("tcp open") != -1 or linea.find("udp open") != -1:
            a.write(linea)
            a.write("\n")
        elif linea.find("tcp closed") != -1 or linea.find("udp closed") != -1:
            c.write(linea)
            c.write("\n")
        elif linea.find("tcp filtered") != -1 or linea.find("udp filtered") != -1:
            f.write(linea)
            f.write("\n")
    puerto = puerto + 10
a.close()
c.close()
f.close()