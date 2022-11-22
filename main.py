import tkinter as tk


def f():
    fahr = ent_temperature.get()
    cels = (5/9) * (float(fahr) - 32)
    kelv = cels + 273.15
    lbl_result_C["text"] = f"{round(cels, 2)} \N{DEGREE CELSIUS}"
    lbl_result_F["text"] = f"{fahr} \N{DEGREE FAHRENHEIT}"
    lbl_result_K["text"] = f"{round(kelv, 2)} \N{KELVIN SIGN}"
    btn_f.config(font=("Courier New", 16), bg="red")
    btn_c.config(font=("Courier New", 16), bg="lightsteelblue3")
    btn_k.config(font=("Courier New", 16), bg="lightsteelblue3")

def c():
    cels = ent_temperature.get()
    fahr = float(cels) * (9/5) + 32
    kelv = float(cels) + 273.15
    lbl_result_C["text"] = f"{cels} \N{DEGREE CELSIUS}"
    lbl_result_F["text"] = f"{round(fahr, 2)} \N{DEGREE FAHRENHEIT} "
    lbl_result_K["text"] = f"{round(kelv, 2)} \N{KELVIN SIGN}"
    btn_f.config(font=("Courier New", 16), bg="lightsteelblue3")
    btn_c.config(font=("Courier New", 16), bg="red")
    btn_k.config(font=("Courier New", 16), bg="lightsteelblue3")

def k():
    kelv = ent_temperature.get()
    cels = float(kelv) - 273.15
    fahr = cels * (9/5) + 32
    lbl_result_C["text"] = f"{round(cels, 2)} \N{DEGREE CELSIUS}"
    lbl_result_F["text"] = f"{round(fahr, 2)} \N{DEGREE FAHRENHEIT} "
    lbl_result_K["text"] = f"{kelv} \N{KELVIN SIGN}"
    btn_f.config(font=("Courier New", 16), bg="lightsteelblue3")
    btn_c.config(font=("Courier New", 16), bg="lightsteelblue3")
    btn_k.config(font=("Courier New", 16), bg="red")

window = tk.Tk()
window.title("Конвертер температуры")
window.geometry("400x350")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=25, fg="dodgerblue2", justify="center")
ent_temperature.config(font=("Courier New", 18))


ent_temperature.grid(row=0, column=0, sticky="e")

btn_f = tk.Button(
    master=window,
    bg="lightsteelblue3",
    text=f"Фаренгейт [↓]",
    command=f
)

btn_c = tk.Button(
    master=window,
    bg="lightsteelblue3",
    text=" Цельсий  [←]",
    command=c
)

btn_k = tk.Button(
    master=window,
    bg="lightsteelblue3",
    text=" Кельвин  [→]",
    command=k
)

window.bind("<Left>", lambda event: c())
window.bind("<Down>", lambda event: f())
window.bind("<Right>", lambda event: k())

btn_f.config(font=("Courier New", 16))
btn_c.config(font=("Courier New", 16))
btn_k.config(font=("Courier New", 16))
lbl_result_C = tk.Label(master=window, fg="firebrick2")
lbl_result_C.config(font=("Courier New", 26))
lbl_result_F = tk.Label(master=window, fg="firebrick2")
lbl_result_F.config(font=("Courier New", 26))
lbl_result_K = tk.Label(master=window, fg="firebrick2")
lbl_result_K.config(font=("Courier New", 26))

frm_entry.grid(row=0, column=0, padx=20)
btn_f.grid(row=2, column=0, pady=10)
btn_c.grid(row=1, column=0, pady=5)
btn_k.grid(row=3, column=0, pady=5)
lbl_result_C.grid(row=4, column=0, padx=10)
lbl_result_F.grid(row=5, column=0, padx=10)
lbl_result_K.grid(row=6, column=0, padx=10)

window.mainloop()