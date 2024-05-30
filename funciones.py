import tkinter as tk

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def main():
    root = tk.Tk()
    root.iconbitmap("icono/lapiz.ico")
    
    fr_ingreso = tk.Frame(root)
    fr_ingreso.pack()
    fr_btns = tk.Frame(root)
    fr_btns.pack()
    fr_rta = tk.Frame(root)
    fr_rta.pack()
    
    num1 = tk.Entry(fr_ingreso)
    num1.grid(row=0, column=0, padx=20, pady=10)
    num2 = tk.Entry(fr_ingreso)
    num2.grid(row=1, column=0, padx=20, pady=10)
    
    btn_suma = tk.Button(fr_btns, text="Sumar", width="10")
    btn_suma.grid(row=0, column=0, padx=10, pady=10)
    btn_resta = tk.Button(fr_btns, text="Restar", width="10")
    btn_resta.grid(row=0, column=1, padx=10, pady=10)
    btn_multiplicar = tk.Button(fr_btns, text="Multiplicar", width="10")
    btn_multiplicar.grid(row=1, column=0, padx=10, pady=10)
    btn_dividir = tk.Button(fr_btns, text="Dividir", width="10")
    btn_dividir.grid(row=1, column=1, padx=10, pady=10)
    
    lb_resultado = tk.Label(fr_rta, text="Resultado:")
    lb_resultado.grid(row=0, column=0)
    rta = tk.Entry(fr_rta)
    rta.grid(row=1, column=0, padx=20, pady=10)
    
    
    root.mainloop()
    
main()