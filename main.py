# This is a sample Python script.
import tkinter as tk
import tkinter.font as tkfont
from text_to_num import text2num
import re
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

def ingredient_decomposer(list_i):

    # on part du principe que la quantité est toujours le premier mot
    if list_i[0].isdigit():
        # TODO gestion des décimal
        q = int(list_i[0])
    else:
        # TODO gestion des langues
        q = text2num(list_i[0],"fr")
    delim = list_i.index(list(set(list_i) & set(["de", "d"]))[0])

    u = ' '.join(list_i[1:delim])
    i = ' '.join(list_i[delim+1:])
    return(q,u,i)


def text_2_ing(txt):
    # prend le txt de l'input et le parse en ingredients
    ing_l = txt.split("\n")

    # list d'objets contenants quantité unité et ingrédient
    for t in ing_l :
        q, u, i = ingredient_decomposer(re.split("\W+|'", t))
        print([q, u, i])

if __name__ == '__main__':
    ecran_ing = tk.Tk()
    ecran_ing.title("New Recipe")
    ecran_ing.geometry("800x600")

    t = "Specify the ingredient list\n (one line per ingredient, format : **quantity** **unit** **ingredient name**)"
    l = tk.Label(ecran_ing, font=tkfont.Font(weight="bold"),text=t)
    l.pack(side="top")
    e = tk.Text(ecran_ing)
    e.pack(expand=True, fill="both")

    e.focus_set()

    def callback():
        ing_text = e.get("1.0",'end-1c') # ici gestion du texte
        text_2_ing(ing_text)
    b = tk.Button(ecran_ing, text = "OK", width = 100, command = callback)
    b.pack(side="bottom")

    tk.mainloop()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
