

#PROJEKT - račun v restavraciji

from tkinter import *

class Jedilnik():
    def __init__(self, master):
        
        Label(master, text="Testenine").grid(row=1, column=0)
        
        Label(master, text="10 €").grid(row=1, column=1)
        
        self.testenine = IntVar(master, value=None)
        polje_testenine= Entry(master, textvariable=self.testenine)
        polje_testenine.grid(row=1, column=2)
   
        Label(master, text="Rizota").grid(row=2, column=0)
        
        Label(master, text="10 €").grid(row=2, column=1)
        
        self.rizota = IntVar(master, value=None)
        polje_rizota= Entry(master, textvariable=self.rizota)
        polje_rizota.grid(row=2, column=2)

        Label(master, text="Solata").grid(row=3, column=0)
        
        Label(master, text="5 €").grid(row=3, column=1)
        
        self.solata = IntVar(master, value=None)
        polje_solata= Entry(master, textvariable=self.solata)
        polje_solata.grid(row=3, column=2)

        gumb_izračun = Button(master, text="Izračun", command=self.izračun)
        gumb_izračun.grid(row=4, column=0)

        self.a = DoubleVar(master, value=None)
        polje_a = Entry(master, textvariable=self.a)
        polje_a.grid(row=4, column=1)

        Label(master, text="€").grid(row=4, column=2)

        self.b = DoubleVar(master, value=None)
        polje_b = Entry(master, textvariable=self.b)
        polje_b.grid(row=5, column=1)

        Label(master, text="€ zaželjena napitnina").grid(row=5, column=2)

        gumb_shrani = Button(master, text="Shrani", command=self.shrani)
        gumb_shrani.grid(row=6, column=2)

        
    def izračun(self):
        x = self.testenine.get()
        y = self.rizota.get()
        z = self.solata.get()
        f = []
        with open("meni.txt") as dat:
            for vrstica in dat:
                f.append(vrstica)
            self.a.set(int(f[0].split(',')[1])*x + int(f[1].split(',')[1])*y + int(f[2].split(',')[1])*z )
            self.b.set(0.15*self.a.get())

    def shrani(self):
        with open("racun.txt", 'at', encoding="utf-8") as f:
            print("Plačal sem {0} evrov in {1} evrov napitnine.".format(self.a.get(), self.b.get()), file = f)

    

root = Tk()
aplikacija = Jedilnik(root)

root.mainloop()
