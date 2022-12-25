import tkinter as tk     
import vlc 
import random
my_media = vlc.MediaPlayer("mus.mp3")

def musica():
    my_media.play()
def stop_musica():
    my_media.stop()



def Change_state_radio_button():
    
    if var.get() == 0:
        file = open('Words.txt',encoding='utf-8',mode="r")
        return file
    elif var.get() == 1:
        file = open('words1.txt',encoding='utf-8',mode="r") 
        return file

def Rand():
    n = random.randint(1,9)
    return n

def ChooseWord(file,n):
    for i in range(n):
        file.readline()
    txt=file.readline()
    return txt,n

def MixWord(txt):
    txt = txt.replace('\n','')
    Word=txt.split()
    for i, word in enumerate(map(list,Word)):
        random.shuffle(word)
        Word[i]=''.join(word)
        global str2
        str2 = txt
    return Word

def selectWord():
    MixedWord['text'] = MixWord(ChooseWord(Change_state_radio_button(),Rand())[0])
    MixedWord['bg'] = "#5cbb73"
    

def Chek(str2):
    if(input_word.get() ==str2):
            print(True)
            MixedWord['bg'] = 'green'
            MixedWord['text'] = str2
    else:
            print(False)
            MixedWord['bg'] = 'red'


def CheckCheck():
        Chek(str2)
        

                                                        #библеотека tkinter из которой 
                                                        #берутся все методы ниже
window = tk.Tk()                                        #создание обьекта window (окно)
window.title("wordMix")                                 #заголовок window (окна)
window.geometry("500x700")                              #размер окна в пикселях относительно монитора
icon = tk.PhotoImage(file='icon.png')                   #добавление в переменную icon картинки icon.png 
window.iconphoto(False,icon)                            #размещение icon в window
window.config(bg="#49c8ff")                             #цвет фона окна
# window.минимизация окна
window.resizable(False,False)                            #возможность изменять размер по ширине заблокирована
ButPic = tk.PhotoImage(file="enterbutton.png") 
MutePic = tk.PhotoImage(file="mutepng.png") 
SigPic = tk.PhotoImage(file="sig.png") 
HintPic = tk.PhotoImage(file="hint.png") 
logoPic = tk.PhotoImage(file="logo1.png")

var = tk.IntVar()
textVar=tk.StringVar()
var.set(0)



"""__________________________________________________________________________________________________________"""
"""Описание места для вывода загаданного слова"""
MixedWord = tk.Label(window,                             # рабочее окно window
               text= "Добро пожаорвать",                     # текст Lable
               height=4,                                    # высота Lable в количестве символов
               width=5,                                    # ширина Lable в количестве символов
               bg="#5cbb73",                                # цвет фона Lable
               fg="white",                                  # цвет текста Lable
               padx=5,                                      # отступ по лево/право в пикселях
               pady=5,                                      # отступ по верх/низ в пикселях
               relief=tk.RAISED,
               font=('Arial','12','bold')                            #граница Lable
               )
MixedWord.grid(row=0,column=0,columnspan=5,rowspan=1,stick='snwe') #вывод оформленного выше Lable в окно window

"""Описание места для вывода подсказки"""
Hint = tk.Label(window,                             # рабочее окно window
            text= "Место для подсказки",                     # текст Lable
            height=4,                                    # высота Lable в количестве символов
            width=5,                                    # ширина Lable в количестве символов
            bg="#5cbb73",                                # цвет фона Lable 
            fg="white",                                  # цвет текста Lable
            padx=0,                                      # отступ по лево/право в пикселях
            pady=0,                                      # отступ по верх/низ в пикселях
            relief=tk.RAISED, 
            font=('Arial','12','bold')                           #граница Lable
            )
Hint.grid(row=4,column=0,columnspan=4,rowspan=3,stick='snwe') #вывод оформленного выше Lable в окно window

Health = tk.Label(window,                             # рабочее окно window
            text= "5 жизней",                     # текст Lable
            height=4,                                    # высота Lable в количестве символов
            width=5,                                    # ширина Lable в количестве символов
            bg="#5cbb73",                                # цвет фона Lable
            fg="white",                                  # цвет текста Lable
            padx=0,                                      # отступ по лево/право в пикселях
            pady=0,                                      # отступ по верх/низ в пикселях
            relief=tk.RAISED, 
            font=('Arial','10','bold')                           #граница Lable
            )
Health.grid(row=8,column=0,columnspan=5,stick='ew') #вывод оформленного выше Lable в окно window

logo=tk.Label(window,image=logoPic)
logo.grid(row=11,column=0,columnspan=5)

"""__________________________________________________________________________________________________________"""
#Поле ввода
input_word = tk.Entry(
                       window,
                       bg="#5cbb73",
                       fg="white",
                       relief=tk.RAISED,
                       font=('Arial','12','bold'),
                       )                
input_word.grid(row=1,column=0,rowspan=3, columnspan=4,stick = 'snwe')
"""Кнопка проверки слова"""
ChekButton = tk.Button(
    window,
    text="Ввод",
    height=90,
    width=90,
    image= ButPic,
    relief=tk.RAISED,
    padx=2,
    pady=2,
    bg="#5cbb73",
    activebackground="#5cbb73",
    command=CheckCheck
    
    
)
ChekButton.grid(row=1,column=4,rowspan=3,stick='ew')
"""Кнопка подсказки"""
Hint_Button = tk.Button(
    window,
    text="Ввод",
    height=90,
    width=90,
    image= HintPic,
    relief=tk.RAISED,
    padx=2,
    pady=2,
    bg="#5cbb73",
    command=selectWord,
    activebackground="#5cbb73",
    
)
Hint_Button.grid(row=4,column=4,rowspan=3, stick='we')
#кнопка воспроизведения музыки
Music_Button = tk.Button(
    window,
    text="Playe",
    height=50,
    width=50,
    image= SigPic,
    relief=tk.RAISED,
    padx=2,
    pady=2,
    bg="#594D5E",
    command=musica
)
Music_Button.grid(row=9,column=0,stick='w')
# кнопка останова музыки 
Mute_Button = tk.Button(
    window,
    text="Ввод",
    height=40,
    width=50,
    image= MutePic,
    relief=tk.RAISED,
    padx=2,
    pady=2,
    bg="#594D5E",
    command=stop_musica
)
Mute_Button.grid(row=10,column=0,stick='w')
"""__________________________________________________________________________________________________________"""

"""__________________________________________________________________________________________________________"""
#Сложность
frame1 = tk.LabelFrame(window, text='Сложность',bg="#49c8ff")
frame1.grid(row=7, column=0,columnspan=5, padx=5 )
#легко
Lite = tk.Radiobutton(
                        frame1,
                        text="легко",
                        fg="black",
                        bg="#49c8ff",
                        font=("Arial","12","bold"),
                        activebackground="#49c8ff",
                        value=0,variable=var
                        
)
Lite.grid(row =9, column=0,stick='w' )
#не просто
Medium = tk.Radiobutton(
                           frame1,
                           text="не просто",
                           fg="black",
                           bg="#49c8ff",
                           font=("Arial","12","bold"),
                           activebackground="#49c8ff",
                           value=1,variable=var
)
Medium.grid(row =9, column=1,stick='w' )
#Сложно
Hard = tk.Radiobutton(
                        frame1,
                        text="сложно",
                        fg="black",
                        bg="#49c8ff",
                        font=("Arial","12","bold"),
                        activebackground="#49c8ff",
                        value=2,variable=var
)
Hard.grid(row =9, column=2, stick='w' )
#Ты не пройдешь
YSNP = tk.Radiobutton(
                        frame1,
                        text="ты не пройдешь",
                        fg="black",
                        bg="#49c8ff",
                        font=("Arial","12","bold"),
                        activebackground="#49c8ff",
                        value=3, variable=var
)
YSNP.grid(row =9, column=3 )



window.mainloop()