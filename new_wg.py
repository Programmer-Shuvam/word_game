import requests
# from bs4 import BeautifulSoup
import sqlite3 as sql

con=sql.connect('words.db')
c=con.cursor()

name=input("enter your name : ")
dct=[]        
user=pc=''

def wrd_srch(wrd):
    # URL = "https://www.dictionary.com/browse/"+wrd+"?s=t"
    # r = requests.get(URL)
    # soup = BeautifulSoup(r.content, 'html5lib')
    # data = soup.select('.e1q3nk1v4')
    c.execute('select word from words where word="'+wrd+'";')
    data=c.fetchone()
    if data:
        return True
    else:
        return False

def usr_wrd(pc):
    global user
    pc=pc.lower()
    n,k=' ',' '
    m=0-(len(pc)+1)
    for i in range(-1,m,-1):
        if (pc[i]>='A' and pc[i]<='Z') or (pc[i]>='a' and pc[i]<='z'):
            k=pc[i]
            # n=input('whether yo want to continue the game(y/n):')
            # n=n.lower()
            break
    # if n=='y' or n=='yes':
    user=input('enter a word starting with "'+k+'" : ')
    user=user.lower()
    # if user[0]==k:
        # print('this might take a while to check whether the word here, is appropriate or not...')

    while user[0]!=k or wrd_srch(user)==False or user in dct:
        user=input('Inappropriate word given by you\nplease enter again : ')
        if user=='':
            print(name,', you lose the game\nbetter luck next time...')
            break
        # if user[0]==k:
            # print('this might take a while to check whether the word here, is appropriate or not...')

    else:
        dct.append(user)
        wrd=user[-1]
        pc_wrd(wrd)

    if k==' ':
        print('computer loses the game, you won',name,'\nCongrats !!!')

    # else:
    #     print(name,', you lose the game\nbetter luck next time...')

def pc_wrd(user):
    global pc
    c.execute('select word from words where word like "'+user+'%";')
    word=c.fetchall()
    for i in word:
        if i[0] not in dct:
            print('word by computer starting with '+user+' : '+i[0])
            pc=i[0]
            break
    dct.append(pc)
    usr_wrd(pc)

pc='army'
print('word by computer starting with a : '+pc)
dct.append(pc)
usr_wrd(pc)
con.commit()