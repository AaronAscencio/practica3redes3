import time
import rrdtool
from getSNMP import consultaSNMP
from trendGraph import graphcomponent
rrdpath = '/home/tani/PycharmProjects/Introduccion_SNMP/5-AdministraciónDeRendimiento/RRD/'
carga_CPU = 0


contador = 120
while 1:
    contador-=1

    carga_CPU = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.3.3.1.2.196608'))
    c_STG = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.2.3.1.5.36'))   
    u_STG = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.2.3.1.6.36'))
    carga_STG = int((u_STG/c_STG)*100)
    c_RAM = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.2.3.1.5.1'))   
    u_RAM = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.25.2.3.1.6.1'))
    carga_RAM = int((u_RAM/c_RAM)*100)



    valor = "N:" + str(carga_CPU) +':' +str(carga_RAM) +':'+ str(carga_STG)
    print (valor)
    rrdtool.update('RRD/trend.rrd', valor)
    rrdtool.dump('RRD/trend.rrd','RRD/trend.xml')
    c = ['CPU','RAM','STG']
    print(contador)
    if(contador==0):
        
        for i in c:
            graphcomponent(i)
            contador=120

    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)