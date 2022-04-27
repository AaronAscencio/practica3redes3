import sys
import rrdtool
from  Notify import send_alert_attached
import time

rrdpath = '/home/tani/PycharmProjects/Introduccion_SNMP/5-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/tani/PycharmProjects/Introduccion_SNMP/5-AdministraciónDeRendimiento/IMG/'

def graphcomponent(comp):
    ultima_lectura = int(rrdtool.last("RRD/trend.rrd"))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 120

    ret = rrdtool.graphv( 
                        f"RRD/{comp}.png",
                        "--start",str(tiempo_inicial),
                        "--end",str(tiempo_final),
                        f"--vertical-label={comp} load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                        f"--title=Uso de {comp} del agente Usando SNMP y RRDtools \n Detección de umbrales",

                        f"DEF:carga{comp}=RRD/trend.rrd:{comp}:AVERAGE",

                        f"VDEF:cargaMAX=carga{comp},MAXIMUM",
                        f"VDEF:cargaMIN=carga{comp},MINIMUM",
                        f"VDEF:cargaSTDEV=carga{comp},STDEV",
                        f"VDEF:cargaLAST=carga{comp},LAST",

                        f"CDEF:umbral35=carga{comp},35,LT,0,carga{comp},IF",
                        f"CDEF:umbral80=carga{comp},80,LT,0,carga{comp},IF",
                        f"AREA:carga{comp}#01FFF7:Carga del {comp}",
                        f"AREA:umbral35#FF9F00:Carga {comp} mayor que 35",
                        f"AREA:umbral80#CA0000:Carga {comp} mayor que 80",
                        "HRULE:35#FF0000:Umbral 1 - 35%",
                        "HRULE:80#0013FF:Umbral 1 - 80%",
                        "PRINT:cargaLAST:%6.2lf",
                        "GPRINT:cargaMIN:%6.2lf %SMIN",
                        "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                        "GPRINT:cargaLAST:%6.2lf %SLAST" )
    #print (ret)

    ultimo_valor=float(ret['print[0]'])
    print(ultimo_valor)
    if ultimo_valor>=0 and ultimo_valor<=35:
        send_alert_attached(f"Componente:{comp} con un uso normal",'Normal no Mayor al 35%',comp)
        print("USO NORMAl")
    elif(ultimo_valor>35 and ultimo_valor<=80):
        send_alert_attached(f"Componente:{comp} con un carga ",'Con carga no Mayor al 80%',comp)
        print("CON CARGA")
    elif(ultimo_valor>80 and ultimo_valor<=100):
        send_alert_attached(f"Componente:{comp} en estado critico ",'Con carga mayor al 80%',comp)
        print("CON CARGA")


