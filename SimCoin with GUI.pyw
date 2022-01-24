import random
from tkinter import *
from tkinter import messagebox
import os
import time
from functools import partial
import time
#----settings--------------------------------------



root = Tk()
root.minsize(width = 720, height = 1080)
root.maxsize(width = 720, height = 1080) 
Coinname = {1:"BTC", 2:"ETH", 3:"DOGE", 4:"XRP", 5:"ETC", 6:"BTT", 7:"LTC", 8:"XLM"}
#코인의 전체적인 시세를 저장하는 리스트
btclist = [52257000]
ethlist = [3527000]
doglist = [351]
riplist = [1335]
etclist = [73640]
bttlist = [5]
litlist = [196450]
lumlist = [399]

#사용자가 구매한 코인 수량
btcbuy = 0
ethbuy = 0
dogbuy = 0
ripbuy = 0
etcbuy = 0
bttbuy = 0
litbuy = 0
lumbuy = 0
wallet = 100000
a = 0
root.configure(bg = "white")
root.title("SimCoin with GUI")


#----settings--------------------------------------

def fluctuate(): #시세 변동 진행 함수
    global a
    i = 0
    upndownlist = [0, 0, 0, 0, 0, 0, 0, 0] #각 코인의 증감을 저장하는 리스트
    for i in range(0, 8): #증감을 정한 후 리스트에 저장
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
    flubutton()

def quote():#시세 변동 표시 함수
    global a
    btcquote = Label(root, text = "{:,}".format(btclist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")
    btcquote.place(x = 330, y = 59)
    ethquote = Label(root, text = "{:,}".format(ethlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    ethquote.place(x = 330, y = 59+80*1)
    dogquote = Label(root, text = "{:,}".format(doglist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    dogquote.place(x = 330, y = 59+80*2)
    ripquote = Label(root, text = "{:,}".format(riplist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    ripquote.place(x = 330, y = 59+80*3)
    etcquote = Label(root, text = "{:,}".format(etclist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    etcquote.place(x = 330, y = 59+80*4)
    bttquote = Label(root, text = "{:,}".format(bttlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    bttquote.place(x = 330, y = 59+80*5)
    litquote = Label(root, text = "{:,}".format(litlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    litquote.place(x = 330, y = 59+80*6)
    lumquote = Label(root, text = "{:,}".format(lumlist[a]), font = ('Yu Gothic UI Semilight', 20), bg = "white")        
    lumquote.place(x = 330, y = 59+80*7)
    
    btcupndown = Label(root, text = "{:.2f}%".format(((btclist[a] - btclist[a-1]) / btclist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    btcupndown.place(x = 525, y = 62)
    ethupndown = Label(root, text = "{:.2f}%".format(((ethlist[a] - ethlist[a-1]) / ethlist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    ethupndown.place(x = 525, y = 62+80*1)
    dogupndown = Label(root, text = "{:.2f}%".format(((doglist[a] - doglist[a-1]) / doglist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    dogupndown.place(x = 525, y = 62+80*2)
    ripupndown = Label(root, text = "{:.2f}%".format(((riplist[a] - riplist[a-1]) / riplist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    ripupndown.place(x = 525, y = 62+80*3)
    etcupndown = Label(root, text = "{:.2f}%".format(((etclist[a] - etclist[a-1]) / etclist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    etcupndown.place(x = 525, y = 62+80*4)
    bttupndown = Label(root, text = "{:.2f}%".format(((bttlist[a] - bttlist[a-1]) / bttlist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    bttupndown.place(x = 525, y = 62+80*5)
    litupndown = Label(root, text = "{:.2f}%".format(((litlist[a] - litlist[a-1]) / litlist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    litupndown.place(x = 525, y = 62+80*6)
    lumupndown = Label(root, text = "{:.2f}%".format(((lumlist[a] - lumlist[a-1]) / lumlist[a-1])*100), font = ('Yu Gothic UI Semilight', 15), bg = "white")
    lumupndown.place(x = 525, y = 62+80*7)
    

def buy(): #구매 진행 함수
    global a
    global wallet, btcbuy, btcnum, ethbuy, ethnum, dogbuy, dognum, ripbuy, ripnum, etcbuy, etcnum, bttbuy, bttnum, litbuy, litnum, lumbuy, lumnum
    #↑ 전역 변수 지정
    buynum = string1.get() #구매 수량값 가져오는 코드
    buyname = string2.get().lower() #구매 코인명값 가져오는 코드
    if buyname == "btc":
        try:
            if int(wallet) > int(buynum) * int(btclist[a]):
                wallet = int(wallet) - int(buynum) * int(btclist[a])
                btcbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                btcnum = Label(root, text = "{:,}".format(btcbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                btcnum.place(x = 620, y = 62)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if buyname == "eth":
        try:
            if int(wallet) > int(buynum) * int(ethlist[a]):
                wallet = int(wallet) - int(buynum) * int(ethlist[a])
                ethbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                ethnum = Label(root, text = "{:,}".format(ethbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                ethnum.place(x = 620, y = 62+80*1)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if buyname == "doge":
        try:
            if int(wallet) > int(buynum) * int(doglist[a]):
                wallet = int(wallet) - int(buynum) * int(doglist[a])
                dogbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                dognum = Label(root, text = "{:,}".format(dogbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                dognum.place(x = 620, y = 62+80*2)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if buyname == "xrp":
        try:
            if int(wallet) > int(buynum) * int(riplist[a]):
                wallet = int(wallet) - int(buynum) * int(riplist[a])
                ripbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                ripnum = Label(root, text = "{:,}".format(ripbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                ripnum.place(x = 620, y = 62+80*3)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if buyname == "etc":
        try:
            if int(wallet) > int(buynum) * int(etclist[a]):
                wallet = int(wallet) - int(buynum) * int(etclist[a])
                etcbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                etcnum = Label(root, text = "{:,}".format(etcbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                etcnum.place(x = 620, y = 62+80*4)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if buyname == "btt":
        try:
            if int(wallet) > int(buynum) * int(bttlist[a]):
                wallet = int(wallet) - int(buynum) * int(bttlist[a])
                bttbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                bttnum = Label(root, text = "{:,}".format(bttbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                bttnum.place(x = 620, y = 62+80*5)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if buyname == "ltc":
        try:
            if int(wallet) > int(buynum) * int(litlist[a]):
                wallet = int(wallet) - int(buynum) * int(litlist[a])
                litbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                litnum = Label(root, text = "{:,}".format(litbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                litnum.place(x = 620, y = 62+80*6)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if buyname == "xlm":
        try:
            if int(wallet) > int(buynum) * int(lumlist[a]):
                wallet = int(wallet) - int(buynum) * int(lumlist[a])
                lumbuy += int(buynum)
                messagebox.showinfo("System", "성공적으로 구매되었습니다.")
                lumnum = Label(root, text = "{:,}".format(lumbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                lumnum.place(x = 620, y = 62+80*7)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")

def sell(): #판매 진행 함수
    global a
    global wallet, btcbuy, btcnum, ethbuy, ethnum, dogbuy, dognum, ripbuy, ripnum, etcbuy, etcnum, bttbuy, bttnum, litbuy, litnum, lumbuy, lumnum
    #↑ 전역 변수 지정
    sellnum = string3.get() #구매 수량값 가져오는 코드
    sellname = string4.get().lower() #구매 코인명값 가져오는 코드
    if sellname == "btc":
        try:
            if btcbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(btclist[a])
                btcbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                btcnum = Label(root, text = "{:,}".format(btcbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                btcnum.place(x = 620, y = 62)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if sellname == "eth":
        try:
            if ethbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(ethlist[a])
                ethbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                ethnum = Label(root, text = "{:,}".format(ethbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                ethnum.place(x = 620, y = 62+80*1)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if sellname == "doge":
        try:
            if dogbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(doglist[a])
                dogbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                dognum = Label(root, text = "{:,}".format(dogbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                dognum.place(x = 620, y = 62+80*2)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if sellname == "xrp":
        try:
            if ripbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(riplist[a])
                ripbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                ripnum = Label(root, text = "{:,}".format(ripbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                ripnum.place(x = 620, y = 62+80*3)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if sellname == "etc":
        try:
            if etcbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(etclist[a])
                etcbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                etcnum = Label(root, text = "{:,}".format(etcbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                etcnum.place(x = 620, y = 62+80*4)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if sellname == "btt":
        try:
            if bttbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(bttlist[a])
                bttbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                bttnum = Label(root, text = "{:,}".format(bttbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                bttnum.place(x = 620, y = 62+80*5)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if sellname == "ltc":
        try:
            if ltcbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(litlist[a])
                litbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                litnum = Label(root, text = "{:,}".format(litbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                litnum.place(x = 620, y = 62+80*6)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
    if sellname == "xlm":
        try:
            if xlmbuy > 0:
                wallet = int(wallet) + int(sellnum) * int(lumlist[a])
                lumbuy -= int(sellnum)
                messagebox.showinfo("System", "성공적으로 판매되었습니다.")
                lumnum = Label(root, text = "{:,}".format(lumbuy), font = ('Yu Gothic UI Semilight', 15), bg = "white")        
                lumnum.place(x = 620, y = 62+80*7)
                userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
                userwallet.place(x = 9, y = 3)
            else:
                messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        except:
            messagebox.showinfo("System", "정확한 수량을 입력해 주십시오.")
        

string1 = StringVar()
string2 = StringVar()
string3 = StringVar()
string4 = StringVar()
#string1 ->구매 수량 입력값
#string2 ->구매 코인명 입력값
#string3 ->판매 수량 입력값
#string4 ->판매 코인명 입력값

main2 = PhotoImage(file = "img/main2.png")
main2image = Label(image = main2)
main2image.place(x = -2, y = -2)

userwallet = Label(root, text = "Wallet: {:,}".format(wallet), font = ('Yu Gothic UI Semilight', 20), bg = "white")
userwallet.place(x = 9, y = 3) #보유자산 출력

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

    BuyNum = Entry(root, width=8, textvariable = string1, font = ('Yu Gothic UI Semilight', 20), bg = "silver")
    BuyNum.place(x = 20, y = 770) #구매 수량 입력 텍스트박스

    BuyName = Entry(root, width=5, textvariable = string2, font = ('Yu Gothic UI Semilight', 20), bg = "silver")
    BuyName.place(x = 150, y = 770) #구매 코인명 입력 텍스트박스
    
    BuyButton = PhotoImage(file = "img/Buy.png") #구매 버튼
    Image = Button(root, image = BuyButton, command = partial(buy))
    Image.place(x = 235, y = 760)


    SellNum = Entry(root, width=8, textvariable = string3, font = ('Yu Gothic UI Semilight', 20), bg = "silver")
    SellNum.place(x = 20, y = 850) #판매 수량 입력 텍스트박스

    SellName = Entry(root, width=5, textvariable = string4, font = ('Yu Gothic UI Semilight', 20), bg = "silver")
    SellName.place(x = 150, y = 850) #판매 코인명 입력 텍스트박스
    
    SellButton = PhotoImage(file = "img/Sell.png") #판매 버튼
    Image = Button(root, image = SellButton, command = partial(sell))
    Image.place(x = 235, y = 840)
    
def flubutton(): #시세 변동 버튼 함수
    global a
    FluButton = PhotoImage(file = "img/Flu.png")
    Image = Button(root, image = FluButton, command = partial(fluctuate))
    Image.place(x = 20, y = 920)

    line = PhotoImage(file = "img/line.png")
    Image = Label(root, image = line)
    Image.place(x = 310, y = 50)
    Image = Label(root, image = line)
    Image.place(x = 500, y = 50)

    quote()
    root.mainloop()

flubutton()
root.mainloop()

