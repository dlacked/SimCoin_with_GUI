import random
from tkinter import *
import os
import time
from functools import partial
#----settings--------------------------------------

root = Tk()
root.minsize(width = 720, height = 1080)
root.maxsize(width = 720, height = 1080) 
Coinname = {1:"Bitcoin", 2:"Etherium", 3:"Dogecoin", 4:"Ripple", 5:"Etherium Classic", 6:"BitTorent", 7:"Litecoin", 8:"Lumen"}
#코인의 시세를 저장하는 리스트
btclist = [52257000]
ethlist = [3527000]
doglist = [351]
riplist = [1335]
etclist = [73640]
bttlist = [5]
litlist = [196450]
lumlist = [399]
wallet = 100000
a = 0
root.configure(bg = "white")
root.title("SimCoin with GUI")
#----settings--------------------------------------

def fluctuate(a):
    i = 0
    upndownlist = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        upndown = random.randrange(0, 2)
        upndownlist[i] = upndown
    if upndownlist[0] == 0:
        btclist.append(int(btclist[a]+random.randrange(0, btclist[a])/8))
    else:
        btclist.append(int(btclist[a]-random.randrange(0, btclist[a])/8))
    if upndownlist[1] == 0:
        ethlist.append(int(ethlist[a]+random.randrange(0, ethlist[a])/8))
    else:
        ethlist.append(int(ethlist[a]-random.randrange(0, ethlist[a])/8))
    if upndownlist[2] == 0:
        doglist.append(int(doglist[a]+random.randrange(0, doglist[a])/8))
    else:
        doglist.append(int(doglist[a]-random.randrange(0, doglist[a])/8))
    if upndownlist[3] == 0:
        riplist.append(int(riplist[a]+random.randrange(0, riplist[a])/8))
    else:
        riplist.append(int(riplist[a]-random.randrange(0, riplist[a])/8))
    if upndownlist[4] == 0:
        etclist.append(int(etclist[a]+random.randrange(0, etclist[a])/8))
    else:
        etclist.append(int(etclist[a]-random.randrange(0, etclist[a])/8))
    if upndownlist[5] == 0:
        bttlist.append(int(bttlist[a]+random.randrange(0, bttlist[a])/8))
    else:
        bttlist.append(int(bttlist[a]-random.randrange(0, bttlist[a])/8))
    if upndownlist[6] == 0:
        litlist.append(int(litlist[a]+random.randrange(0, litlist[a])/8))
    else:
        litlist.append(int(litlist[a]-random.randrange(0, litlist[a])/8))
    if upndownlist[7] == 0:
        lumlist.append(int(lumlist[a]+random.randrange(0, lumlist[a])/8))
    else:
        lumlist.append(int(lumlist[a]-random.randrange(0, lumlist[a])/8))
    a += 1
    flubutton(a)

def quote(a):
    btcquote = Label(root, text = "{:,}₩".format(btclist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")
    btcquote.place(x = 330, y = 59)
    ethquote = Label(root, text = "{:,}₩".format(ethlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    ethquote.place(x = 330, y = 59+80*1)
    dogquote = Label(root, text = "{:,}₩".format(doglist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    dogquote.place(x = 330, y = 59+80*2)
    ripquote = Label(root, text = "{:,}₩".format(riplist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    ripquote.place(x = 330, y = 59+80*3)
    etcquote = Label(root, text = "{:,}₩".format(etclist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    etcquote.place(x = 330, y = 59+80*4)
    bttquote = Label(root, text = "{:,}₩".format(bttlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    bttquote.place(x = 330, y = 59+80*5)
    litquote = Label(root, text = "{:,}₩".format(litlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    litquote.place(x = 330, y = 59+80*6)
    lumquote = Label(root, text = "{:,}₩".format(lumlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    lumquote.place(x = 330, y = 59+80*7)
        

#보유자산 출력
userwallet = Label(root, text = "Wallet: {:,}₩".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
userwallet.place(x = 9, y = 3)

#이미지, 코인명 출력
for i in range(0, 8):
    if i == 0:
        Coinname[i] = PhotoImage(file = f"img/{i+1}.png")
        Image = Label(image = Coinname[i])
        Image.place(x = 20, y = 50)
        name = Label(root, text=f"{Coinname[i+1]}", font = ('Yu Gothic UI Semilight', 20), bg = "white")
        name.place(x = 100, y = 59)
    else:
        Coinname[i] = PhotoImage(file = f"img/{i+1}.png")
        Image = Label(image = Coinname[i])
        Image.place(x = 20, y = 50+80*i)
        name = Label(root, text=f"{Coinname[i+1]}", font = ('Yu Gothic UI Semilight', 20), bg = "white")
        name.place(x = 100, y = 59+80*i)
        
    BuyButton = PhotoImage(file = "img/Buy.png")
    Image = Button(root, image = BuyButton)
    Image.place(x = 20, y = 760)

    SellButton = PhotoImage(file = "img/Sell.png")
    Image = Button(root, image = SellButton)
    Image.place(x = 20, y = 840)
    
def flubutton(a):
    FluButton = PhotoImage(file = "img/Flu.png")
    Image = Button(root, image = FluButton, command = partial(fluctuate, a))
    Image.place(x = 20, y = 920)

    line = PhotoImage(file = "img/line.png")
    Image = Label(root, image = line)
    Image.place(x = 310, y = 50)
    Image = Label(root, image = line)
    Image.place(x = 500, y = 50)

    quote(a)
    root.mainloop()
flubutton(a)
root.mainloop()

