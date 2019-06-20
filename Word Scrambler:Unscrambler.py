#Word Scrambler/Unscrambler
import sys
import random
import threading
def shuffle(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
garbage = False
solved = []

print('----------Word Scrambler/Unscrambler----------')
option = input('''
1) Scramble a word
2) Unscramble a word
3) Exit
Option: ''')
def solve():
    attempt_no = 0
    while garbage == False:
        attempt_no += 1
        rs1 = shuffle(scram)
        rs = '\n' + rs1 + '\n'
        if rs in dct:
            if rs1 not in solved:
               print('Unscrambled word: ' + rs1.upper() + ' after ' + str(attempt_no) + ' attempts')
               solved.append(rs1)

    while garbage == True:
        attempt_no += 1
        rs1 = shuffle(scram)[0:len(scram) - garb_num]
        rs = '\n' + rs1 + '\n'
        if rs in dct:
            if rs1 not in solved:
                print('Unscrambled word: ' + rs1.upper() + ' after ' + str(attempt_no) + ' attempts')
                solved.append(rs1)

if option == '1':
    word = input('Word to scramble: ').upper()
    method = input('Include garbage letters? (y/n) [n] ')
    if method == 'y':
        garb = input('Specify garbage letters [leave blank for random]: ').upper()
        if garb == '':
            garb_no = int(input('Number of garbage letters: '))
            for i in range(garb_no):
                word += alphabet[random.randint(0,25)]
        word += garb
    print(shuffle(word))
                
elif option == '2':
    option = input('''
1) Unscramble with no garbage letters
2) Unscramble with garbage letters
Option: ''')
    scram = input('Word to unscramble: ')
    thread = int(input('Number of threads to use: '))
    f = open('words.txt', 'r')
    dct = f.read()
    if option == '1':
        for i in range(0,thread):
            threading.Thread(target=solve).start()
    elif option == '2':
        garb_num = int(input('Number of garbage letters: '))
        print('WARNING: THIS PROCEDURE CAN TAKE AN EXTREMELY LONG TIME')
        garbage = True
        for i in range(0,thread):
            threading.Thread(target=solve).start()
elif option == '3':
    sys.exit()
