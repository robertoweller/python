from time import sleep

from datetime import datetime

# agora = datetime.now() 

while True:
    sleep(.5)
    # Cortar a parte do tempo
    agora = str(datetime.now())[11:16]

    print(f'Hora atual {agora} ', end = '\r\r')


