import tkinter as tk
from tkinter import ttk, messagebox

# DATA CALC
def calc():
    try:
        resolution = resolution_var.get()
        duration = duration_var.get()

        bit_rates = {
            "144p":150,
            "240p":350,
            "360p":800,
            "480p":1000,
            "720p":2500,
            "1080p":5000,
            "2K":12000,
            "4K":25000,
            "8K":60000
        }

        bit_rate = bit_rates[resolution]
        file_size_mb = (bit_rate * duration * 60) / (8 / 1024)
        result_label.config(text=f"Video Boyutu: {file_size_mb:.2f} MB")
    except ValueError as v:
        messagebox.showerror("Hata", "Lütfen sayısal bir veri giriniz.")

# GUI
# Window Settings
root = tk.Tk()
root.resizable(0,0)
root.title("Video Boyutu Hesaplayıcı (beratcodes)")
root.geometry("390x300")
# Style Settings
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12))
# Button Style
style.map("TButton", foreground=[('active', 'black'),('!disabled', 'black')],
          background=[('active', 'green'),('!disabled', 'green')])
# Resolution Selector
resolution_label = ttk.Label(root, text="Çözünürlük")
resolution_label.grid(row=0,column=0 ,padx=10,pady=10)
resolution_var = tk.StringVar()
resolution_combobox = ttk.Combobox(root, textvariable=resolution_var, state='readonly')
resolution_combobox['values'] = ("144p","240p","360p","480p","720p","1080p","2K","4K","8K")
resolution_combobox.current(0)
resolution_combobox.grid(row=0,column=0, columnspan=2, padx=10,pady=10)
# Duration Settings
duration_label = tk.Label(root, text="Video Uzunluğu (Dakika)")
duration_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
duration_var = tk.StringVar()
duration_entry = ttk.Entry(root,textvariable=duration_var)
duration_entry.grid(row=2, column=0, columnspan=2, padx=10,pady=10)
# Calc Button
calc_button = tk.Button(root, text="Calculate", command=calc)
calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10,pady=10)
root.mainloop()