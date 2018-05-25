import os
import random
import time
from IPython.display import clear_output

os.system('clear')
board=[""," "," "," "," "," "," "," "," "," "]
def print_board():
    os.system('clear')
    print("TIC TAC TOE")
    print ("")
    print (board[1] + '|' +board[2]+ '|' +board[3])
    print ("-|-|-")
    print (board[4] + '|' +board[5] + '|' +board[6])
    print ("-|-|-")
    print (board[7] + "|" +board[8] + "|" +board[9])

print_board()
while True:
    choice=input("Enter your choice(P1): ")
    choice=int(choice)
    board[choice]="X"
    if((board[1]==board[2]==board[3]=="X") or
        (board[4]==board[5]==board[6]=="X") or
        (board[7]==board[8]==board[9]=="X") or
        (board[1]==board[4]==board[7]=="X") or
        (board[2]==board[5]==board[8]=="X") or
        (board[3]==board[6]==board[9]=="X") or
        (board[1]==board[5]==board[9]=="X") or
        (board[3]==board[5]==board[7]=="X")):
        print_board()
        print("Player 1 wins")
        break
    else:
        print_board()
    choice=input("Enter your choice(P2): ")
    choice=int(choice)
    board[choice]="O"
    if((board[1]==board[2]==board[3]=="O") or
        (board[4]==board[5]==board[6]=="O") or
        (board[7]==board[8]==board[9]=="O") or
        (board[1]==board[4]==board[7]=="O") or
        (board[2]==board[5]==board[8]=="O") or
        (board[3]==board[6]==board[9]=="O") or
        (board[1]==board[5]==board[9]=="O") or
        (board[3]==board[5]==board[7]=="O")):
        print_board()
        print("Player 2 wins")
        break
    else:
        print_board()
