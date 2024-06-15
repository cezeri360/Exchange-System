import requests
import tkinter as tk
r= tk.Tk()
r.title("المعاملات المالية")
r.geometry("700x500+300+100")
r.configure(background="black")
yazi=tk.Label(
    text="financial transactions",
    fg="orange",
    bg="black",
    width=30,
    height=3,
    font="Impact"
)
yazi.pack()
def get_exchange_rate(currency_code):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency_code}"
    response = requests.get(url)
    data = response.json()
    return data['rates']['TRY']
mısır_lirasi = 50
mısır_lirası_değeri = get_exchange_rate("EGP")
türk_lirasi = mısır_lirasi * mısır_lirası_değeri
pak_lirasi = 50
pak_lirası_değeri = get_exchange_rate("PKR")
türkiyye_lirasi = pak_lirasi * pak_lirası_değeri
az_lirasi = 50
az_lirası_değeri = get_exchange_rate("AZN")
türkiyyeci_lirasi = az_lirasi * az_lirası_değeri
print(f"{pak_lirasi} Pakistan Rupisi, {türkiyye_lirasi} Türk Lirasına eşittir.")
print(f"{mısır_lirasi} Mısır Lirası, {türk_lirasi} Türk Lirasına eşittir.")
print(f"{az_lirasi} Azerbaycan Manatı, {türkiyyeci_lirasi} Türk Lirasına eşittir.")
def listeye_tikla(event):
    secilen = liste.get(liste.curselection())
    if secilen == "Pakistan Rupisi":
        sonuc_label.config(text=f"{pak_lirasi} Pakistan Rupisi, {türkiyye_lirasi} Türk Lirasına eşittir.",fg="green",bg="black",font="Tahoma")
    elif secilen == "Mısır Lirası":
        sonuc_label.config(text=f"{mısır_lirasi} Mısır Lirası, {türk_lirasi} Türk Lirasına eşittir.",fg="red",bg="black",font="Tahoma")
    elif secilen == "Azerbaycan Manatı":
        sonuc_label.config(text=f"{az_lirasi} Azerbaycan Manatı, {türkiyyeci_lirasi} Türk Lirasına eşittir.",fg="blue",bg="black",font="Tahoma")
liste=tk.Listbox(r)
liste.pack()
liste.insert(tk.END,"Pakistan Rupisi")
liste.insert(tk.END,"Mısır Lirası")
liste.insert(tk.END,"Azerbaycan Manatı")
sonuc_label = tk.Label(r, text="",fg="green",bg="orange",font="Impact")
sonuc_label.pack()
liste.bind("<ButtonRelease-1>", listeye_tikla)
r.mainloop()
###financial transactions###
############
#I'm from Turkey
#Thanks for reviewing this program.
#################################################3




















