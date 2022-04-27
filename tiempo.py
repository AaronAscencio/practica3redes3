import time

cold = 12
while(True):
    cold -=1
    print(cold)
    time.sleep(5)
    if(cold==0):
        print("Enviar correo")
        cold=12