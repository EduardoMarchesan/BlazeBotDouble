import telebot
import requests


key_token="6507452851:AAE76zaxNriJN_cdWiE1MXVngCMnygY7CPk"




import requests
from datetime import *
import time

aposta=''
vitoria=0
derrota=0

while True:
    def envio():
        #chat_id="740375451"
        chat_id="-1001873780014"
        message = aposta_seg
        URL_telegram = 'https://api.telegram.org/bot'+key_token+'/sendMessage?chat_id='+chat_id+'&text='+message
        requests.get(URL_telegram)



    now = datetime.now()
    hora_att=now+timedelta(hours=3)
    current_time = hora_att.strftime("%H:%M:%S")
    print(current_time)
    #current_date= now.strftime("%d/%m/%Y")
    current_date= hora_att.strftime("%Y-%m-%d")
    print(current_date)

    #Tivemos um erro interno de servidor,porem,foi a mudança inexperada da link da api,algum dado esta indo errado(no caso foi a data)


    url=f"https://blaze.com/api/roulette_games/history?startDate=2023-07-14T23:45:41.336Z&endDate={current_date}T{current_time}Z&page=1"

    reques=requests.get(url)
    resultado=reques.json()

    #print(resultado["records"][0]["color"])
    lista=[]
    for i in range(0,5):
        cor=f"{resultado['records'][i]['color']}"
        lista.append(cor)


    if aposta=="red":
        if aposta!=lista[0]:
            derrota+=1
            aposta=''
        else:
            vitoria+=1
            aposta=''
    elif aposta=='black':
        if aposta!=lista[0]:
            derrota+=1
            aposta=''
        else:
            vitoria+=1
            aposta=''

    
    unique_cor=set(lista)
    if len(set(lista))==1:
        if 'red' in unique_cor:
            aposta_seg=f"""\U000026AB
Vitorias={vitoria}
Derrotas={derrota}"""
            aposta='black'
            envio()
        elif 'black' in unique_cor:
            aposta_seg=f"""\U0001F534
Vitorias={vitoria}
Derrotas={derrota}"""
            aposta='red'
            envio()

    time.sleep(30)

