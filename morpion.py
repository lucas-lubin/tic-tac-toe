from tkinter import *
 
fen= Tk()
fen.title("Morpion")
 
i=0
a1,a2,a3,a4,a5,a6,a7,a8,a9 = 0,0,0,0,0,0,0,0,0  #Creation des variables pour les ronds
b1,b2,b3,b4,b5,b6,b7,b8,b9 = 0,0,0,0,0,0,0,0,0  #Creation des variables pour les carrés
victoire=0
 
           #fonction pour dessiner une croix
def croix(x,y):
    can.create_line(x-42,y-42,x+42,y+42, width=8, fill="red")
    can.create_line(x+42,y-42,x-42,y+42, width=8, fill="red")
 
            #fonction pour dessiner un rond
def rond(x,y):
    r=43 #rayon du rond
    can.create_oval(x-r,y-r,x+r,y+r, width=8, outline="red")
 
            #fonction pour recommencer
def recommence():
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global victoire
    global i
 
    chaine.configure(text="Afficher vainqueur")
    can.delete(ALL)
    can.create_line(100,0,100,301, width=2, fill='pink')
    can.create_line(200,0,200,301, width=2, fill='pink')
    can.create_line(0,100,301,100, width=2, fill='pink')
    can.create_line(0,200,301,200, width=2, fill='pink')
    i=0
    a1,a2,a3,a4,a5,a6,a7,a8,a9 = 0,0,0,0,0,0,0,0,0
    b1,b2,b3,b4,b5,b6,b7,b8,b9 = 0,0,0,0,0,0,0,0,0
    victoire=0
 
            #fonction qui traite tout (dessin des ronds et croix + victoire du joueur)
def morpion(event):
    global i
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global victoire
 
            #placement des ronds
 
    if event.x<=100 and event.y<=100 and i%2==1:
        x=50
        y=50
        if b1!=0:
            i=i
            if b1==croix(x,y):
                i=i
        else:
            a1=rond(x,y)
            a1
            i+=1
    if event.x<=200 and event.x>100 and event.y<=100 and i%2==1:
        x=150
        y=50
        if b2!=0:
            i=i
            if b2==croix(x,y):
                i=i
        else:
            a2=rond(x,y)
            a2
            i+=1
    if event.x<=300 and event.x>200 and event.y<=100 and i%2==1:
        x=250
        y=50
        if b3!=0:
            i=i
            if b3==croix(x,y):
                i=i
        else:
            a3=rond(x,y)
            a3
            i+=1
    if event.x<=100 and event.y>100 and event.y<=200 and i%2==1:
        x=50
        y=150
        if b4!=0:
            i=i
            if b4==croix(x,y):
                i=i
        else:
            a4=rond(x,y)
            a4
            i+=1
    if event.x<=200 and event.x>100 and event.y>100 and event.y<=200 and i%2==1:
        x=150
        y=150
        if b5!=0:
            i=i
            if b5==croix(x,y):
                i=i
        else:
            a5=rond(x,y)
            a5
            i+=1
    if event.x<=300 and event.x>200 and event.y>100 and event.y<=200 and i%2==1:
        x=250
        y=150
        if b6!=0:
            i=i
            if b6==croix(x,y):
                i=i
        else:
            a6=rond(x,y)
            a6
            i+=1
    if event.x<=100 and event.y>200 and event.y<=300 and i%2==1:
        x=50
        y=250
        if b7!=0:
            i=i
            if b7==croix(x,y):
                i=i
        else:
            a7=rond(x,y)
            a7
            i+=1
    if event.x<=200 and event.x>100 and event.y>200 and event.y<=300 and i%2==1:
        x=150
        y=250
        if b8!=0:
            i=i
            if b8==croix(x,y):
                i=i
        else:
            a8=rond(x,y)
            a8
            i+=1
    if event.x<=300 and event.x>200 and event.y>200 and event.y<=300 and i%2==1:
        x=250
        y=250
        if b9!=0:
            i=i
            if b9==croix(x,y):
                i=i
        else:
            a9=rond(x,y)
            a9
            i+=1
 
                    #placement des croix
 
    if event.x<=100 and event.y<=100 and i%2==0 :
        x=50
        y=50
        if a1!=0:
            i=i
            if a1==rond(x,y):
                i=i
        else:
            b1=croix(x,y)
            b1
            i+=1
    if event.x<=200 and event.x>100 and event.y<=100 and i%2==0:
        x=150
        y=50
        if a2!=0:
            i=i
            if a2==rond(x,y):
                i=i
        else:
            b2=croix(x,y)
            b2
            i+=1
    if event.x<=300 and event.x>200 and event.y<=100 and i%2==0:
        x=250
        y=50
        if a3!=0:
            i=i
            if a3==rond(x,y):
                i=i
        else:
            b3=croix(x,y)
            b3
            i+=1
    if event.x<=100 and event.y>100 and event.y<=200 and i%2==0:
        x=50
        y=150
        if a4!=0:
            i=i
            if a4==rond(x,y):
                i=i
        else:
            b4=croix(x,y)
            b4
            i+=1
    if event.x<=200 and event.x>100 and event.y>100 and event.y<=200 and i%2==0:
        x=150
        y=150
        if a5!=0:
            i=i
            if a5==rond(x,y):
                i=i
        else:
            b5=croix(x,y)
            b5
            i+=1
    if event.x<=300 and event.x>200 and event.y>100 and event.y<=200 and i%2==0:
        x=250
        y=150
        if a6!=0:
            i=i
            if a6==rond(x,y):
                i=i
        else:
            b6=croix(x,y)
            b6
            i+=1
    if event.x<=100 and event.y>200 and event.y<=300 and i%2==0:
        x=50
        y=250
        if a7!=0:
            i=i
            if a7==rond(x,y):
                i=i
        else:
            b7=croix(x,y)
            b7
            i+=1
    if event.x<=200 and event.x>100 and event.y>200 and event.y<=300 and i%2==0:
        x=150
        y=250
        if a8!=0:
            i=i
            if a8==rond(x,y):
                i=i
        else:
            b8=croix(x,y)
            b8
            i+=1
    if event.x<=300 and event.x>200 and event.y>200 and event.y<=300 and i%2==0:
        x=250
        y=250
        if a9!=0:
            i=i
            if a9==rond(x,y):
                i=i
        else:
            b9=croix(x,y)       
            b9
            i+=1
 
                #victoire du Joueur 1
 
    if b1!=0 and b2!=0 and b3!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
    if b1!=0 and b4!=0 and b7!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
    if b1!=0 and b5!=0 and b9!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
    if b2!=0 and b5!=0 and b8!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
    if b3!=0 and b6!=0 and b9!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
    if b3!=0 and b5!=0 and b7!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
    if b4!=0 and b5!=0 and b6!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
    if b7!=0 and b8!=0 and b9!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 1")
 
                #victoire du Joueur 2
 
    if a1!=0 and a2!=0 and a3!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")
    if a1!=0 and a4!=0 and a7!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")
    if a1!=0 and a5!=0 and a9!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")
    if a2!=0 and a5!=0 and a8!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")
    if a3!=0 and a6!=0 and a9!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")
    if a3!=0 and a5!=0 and a7!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")
    if a4!=0 and a5!=0 and a6!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")
    if a7!=0 and a8!=0 and a9!=0 and victoire==0:
        victoire=1
        chaine.configure(text="Vainqueur : Joueur 2")

        #Permet de lorsque le joueur a gagné il ne peut plus


        
        #Partie interface graphique
 
chaine=Label(fen, text = "Afficher vainqueur")
chaine.grid(row=0, column=0, columnspan=2)
can= Canvas(fen, bg='black', width=300, height=300)
can.grid(row=1, column=0, columnspan=2, padx = 5, pady = 5)
can.create_line(100,0,100,300, width=4, fill='red')
can.create_line(200,0,200,300, width=4, fill='red')
can.create_line(0,100,300,100, width=4, fill='red')
can.create_line(0,200,300,200, width=4, fill='red')
Button(fen, text="Quitter", command=fen.destroy).grid(row=2, column=1, padx = 3, pady = 3, sticky = S+W+E)
Button(fen, text="Recommencer", command=recommence).grid(row=2, column=0, padx = 3, pady = 3, sticky = S+W+E)

can.bind("<Button-1>", morpion)
 
fen.mainloop()