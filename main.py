import requests
import requests
from datetime import *
import time


# Chave de autenticação para acessar o Bot  do Telegram
key_token="6507452851:AAE76zaxNriJN_cdWiE1MXVngCMnygY7CPk"


def envio(mensagem):
    """
        Envia uma mensagem para um chat no Telegram.

        Args:
            mensagem (str): A mensagem a ser enviada.

        Returns:
            None
    """
    chat_id="-1001873780014"  # ID do chat no Telegram
    URL_telegram = 'https://api.telegram.org/bot'+key_token+'/sendMessage?chat_id='+chat_id+'&text='+mensagem
    requests.get(URL_telegram)


aposta=''
vitoria=0
derrota=0

# Loop principal
while True:
    # Função para enviar mensagens para o chat no Telegram utilizando o bot
    



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
    for i in range(0,3):
        cor=f"{resultado['records'][i]['color']}"
        lista.append(cor)


    if aposta=="red":
        if aposta!=lista[0]:
            derrota+=1
            envio(mensagem="Derrota")
            aposta=''
        else:
            vitoria+=1
            envio(mensagem="Vitoria")
            aposta=''
    elif aposta=='black':
        if aposta!=lista[0]:
            derrota+=1
            envio(mensagem="Derrota")
            aposta=''
        else:
            vitoria+=1
            envio(mensagem="Vitoria")
            aposta=''

    
    unique_cor=set(lista)
    if len(set(lista))==1:
        if 'red' in unique_cor:
            mensagem="\U000026AB"
            aposta='black'
            envio(mensagem=mensagem)
        elif 'black' in unique_cor:
            mensagem="\U0001F534"
            aposta='red'
            envio(mensagem=mensagem)

    time.sleep(30)

