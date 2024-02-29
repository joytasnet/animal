import tkinter as tk

animal=None
index=0
correct=0
root=tk.Tk()
root.geometry('400x500')
class Animal:
    def __init__(self,ja,en,img):
        self.ja=ja
        self.en=en
        self.img=img

animals=[
	Animal('ぞう','elephant',tk.PhotoImage(file='elephant.png').subsample(2)),
	Animal('しろくま','polarbear',tk.PhotoImage(file='polarbear.png').subsample(2)),
	Animal('くじら','whale',tk.PhotoImage(file='whale.png').subsample(2)),
	Animal('ペンギン','penguin',tk.PhotoImage(file='penguin.png').subsample(2)),
	Animal('ライオン','lion',tk.PhotoImage(file='lion.png').subsample(2)),
	Animal('カンガルー','kangaroo',tk.PhotoImage(file='kangaroo.png').subsample(2)),
	Animal('ひと','human',tk.PhotoImage(file='human.png').subsample(2)),
	Animal('いぬ','dog',tk.PhotoImage(file='dog.png').subsample(2)),
	Animal('ねこ','cat',tk.PhotoImage(file='cat.png').subsample(2)),
	Animal('あり','ant',tk.PhotoImage(file='ant.png').subsample(2)),
]

def clear_result():
    l_result['text']=''

def btn_click():
    global animal,correct,index
    user_ans=entry.get()
    if user_ans.lower()==animal.en:
        correct+=1
        msg='正解!'
    else:
        msg=f'不正解{animal.ja}の答えは{animal.en}'
    if index==len(animals)-1:
        msg+=f'\n{len(animals)}中{correct}問正解でした!'
        index = -1
        correct=0
    l_result['text']=msg
    root.after(1500,clear_result)
    index+=1
    animal=animals[index]
    l_ja['text']=animal.ja
    cvs.delete('ANI')
    cvs.create_image(100,100,image=animal.img,tag="ANI")
    entry.delete(0,tk.END)

fnt=('Arial',30)
animal=animals[index]
l_ja=tk.Label(text=animal.ja,font=fnt)
l_ja.pack(pady=(20,10))
entry=tk.Entry(font=('Arial',20))
entry.pack()
cvs=tk.Canvas(width=200,height=200)
cvs.pack(pady=20)
cvs.create_image(100,100,image=animal.img,tag="ANI")
btn=tk.Button(text='答える',font=fnt,command=btn_click)
btn.pack()
l_result=tk.Label(text='',font=('Arial',16))
l_result.pack(pady=(10,0))
root.mainloop()
