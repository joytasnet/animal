import tkinter as tk

#今着目しているAnimalインスタンス
animal=None
#animalsリストのindex
index=0
#正解数
correct=0

root=tk.Tk()
root.geometry('400x500')

#Animalクラス
class Animal:
    def __init__(self,ja,en,img):
        self.ja=ja
        self.en=en
        self.img=img

#animalsリスト(subsample(整数)は画像を1/整数に縮小zoomは拡大)
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

#結果表示を消す関数
def clear_result():
    l_result['text']=''

#ボタンを押したときの処理
def btn_click():
    global animal,correct,index
    #入力欄に入っている値を取得
    user_ans=entry.get()
    #答えが正しかったら
    if user_ans.lower()==animal.en:
        correct+=1
        msg='正解!'
    else:
        msg=f'不正解{animal.ja}の答えは{animal.en}'
    #最後の問題だったら
    if index==len(animals)-1:
        #結果表示
        msg+=f'\n{len(animals)}中{correct}問正解でした!'
        index = -1
        correct=0

    #ラベルにメッセージを表示
    l_result['text']=msg
    #1500m秒後にclear_resultを実行
    root.after(1500,clear_result)

    index+=1
    #リストから次のanimalインスタンスを取り出す
    animal=animals[index]
    #問題文表示
    l_ja['text']=animal.ja
    #古い画像を削除
    cvs.delete('ANI')
    #新しい画像を表示
    cvs.create_image(100,100,image=animal.img,tag="ANI")
    #入力欄を空にする
    entry.delete(0,tk.END)

fnt=('Arial',30)
#リストから動物を取り出す
animal=animals[index]
#問題表示
l_ja=tk.Label(text=animal.ja,font=fnt)
#ラベルを画面に配置(上が20下が10のpadding)
l_ja.pack(pady=(20,10))
#入力フォームの作成
entry=tk.Entry(font=('Arial',20))
#入力フォームを配置
entry.pack()
#キャンバスの作成
cvs=tk.Canvas(width=200,height=200)
#キャンバスの配置
cvs.pack(pady=20)
#画像の作成
cvs.create_image(100,100,image=animal.img,tag="ANI")
#ボタンの作成
btn=tk.Button(text='答える',font=fnt,command=btn_click)
#ボタンの配置
btn.pack()
#結果表示ラベルの作成
l_result=tk.Label(text='',font=('Arial',16))
#結果表示ラベルの配置
l_result.pack(pady=(10,0))
#tkinterアプリを動かすときのおきまり
root.mainloop()
