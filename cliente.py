#!/usr/bin/env python3
import socket 
import sys 
import time

HOST = '127.0.0.1' # IP do Servidor 
PORT = 40000 # Porta que o Servidor escuta 


print('Servidor: ', (HOST, PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
sock.connect(dest)


tipoDaJogada = input('escolha pedra, papel ou tesoura: ')
sock.send(tipoDaJogada.encode())


jogador1 = 1
jogador2 = 2

while True:    # Menu de escolhas do usuário
    print()
    print("*=" * 40, "\n")
    print('Escolha um comando PEDRA/PAPEL/TESOURA', "\n")
    print("-" * 40, "\n")

   