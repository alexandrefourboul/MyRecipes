# This is a sample Python script.
import tkinter as tk
import tkinter.font as tkfont
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
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
        print(e.get("1.0",'end-1c')) # ici gestion du texte

    b = tk.Button(ecran_ing, text = "OK", width = 100, command = callback)
    b.pack(side="bottom")

    tk.mainloop()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
