import sys
import socket
import curses
from curses import wrapper
from threading import Thread

HOST = '0.0.0.0'
PORT = 40000

if len(sys.argv) > 1:
    HOST = sys.argv[1]


TAMANHO_MENSAGEM = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)
sock.accept() 

jogada = conn.recv(1024)
jogada.decode()
print(jogada)


tipos = ['pedra', 'papel', 'tesoura']

lista_comandos = {      # Lista de comandos que o usuário pode escolher
    "pedra": "PEDRA",
    "tesoura": "TESOURA",
    "papel": "PAPEL",
}

lista_acertos = ['perdeu':' PERDEU', 'empate': 'EMPATE' , 'ganhou':'GANHOU'  ]

lista_de_erros = {        # Lista de erros possíveis
    "404": "Comando errado, verifique se foi escrito corretamente",
    "406": "Comando incompleto",
    "409": "campo vazio",
}

cmd_usr = input("Digite algum comando: ").split()
tamanho_comando = len(cmd_usr)


jogador1 = 1
jogador2 = 2
    
def processa_cliente(con, cliente): #Metodo para processar mensagem do cliente
    while True: #Enquanto for verdadeiro
        msg = con.recv(1024) #Ler o tamanho da mensagem do cliente
        if not msg or processa_mensagem(msg, con, cliente): break

    con.close() #Fecha a conexão e informa qual cliente foi desconecatado
    print("Cliente desconectado:", cliente)

def processa_mensagem(mensagem, coneccao, cliente): # Metodo que faz o processamento da mensagem
    mensagem_decodificada = mensagem.decode() #Decodifica a mensagem e coloca dentro da variável, mensagem_decodificada
    mensagem_decodificada = mensagem_decodificada.split()
 

while True :
   # jogada = conn.recv(1024)
   # jogada.decode()
  #  print(jogada)

    try:
        jogador1 = lista_comandos.get(cmd_usr[0].lower())  # Ler o comando dado pelo usuário
        assert jogador1 is not None  
        
        jogador2 = lista_comandos.get(cmd_usr[0].lower())  # Ler o comando dado pelo usuário
        assert jogador2 is not None 

        if jogador1== 'papel':
            if jogador2 == 'pedra':
                coneccao.send(str.encode("ganhou")) #ajustat os comandos no array para funcionar o send
#verificar se é para usar assim;
            elif jogador2 == 'tesoura':
                coneccao.send(str.encode('jogador2 ganhou'))
        
            else:
                coneccao.send(str.encode('Empate'))
        
        elif jogador1== 'pedra':
            if jogador2 == 'papel':
                coneccao.send(str.encode('Empate'))
        

            elif jogador2 == 'pedra':
                coneccao.send(str.encode('Empate'))
        
        
            else:
                coneccao.send(str.encode('Empate'))
        

        elif jogador1== 'tesoura':
            if jogador2 == 'papel':
                coneccao.send(str.encode('Empate'))
        

            elif jogador2 == 'pedra':
                coneccao.send(str.encode('Empate'))
        
        
            else:
                coneccao.send(str.encode('Empate'))
        
        else:
            coneccao.send(str.encode('Empate'))
        

    except IndexError:
       coneccao.send(str.encode('Empate'))
        
        


def enviar(stdscr, input_box):
    pass

