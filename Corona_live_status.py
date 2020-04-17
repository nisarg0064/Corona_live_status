import tkinter as tk
import requests


def method(country):
    res = requests.get("https://api.covid19api.com/summary")
    resp = res.json()

    for i in resp["Countries"]:
        if i["Country"].lower() == country.lower():
            country = i["Country"]
            print(i["TotalConfirmed"], i["TotalDeaths"], i["TotalRecovered"])
            Confirmed = i["TotalConfirmed"]
            deaths = i["TotalDeaths"]
            recovered = i["TotalRecovered"]


    death_to_recovery = deaths / recovered
    resulted = (recovered + deaths) / Confirmed
    remainingCases = (1 - resulted) * 100
    f = f'''Confirmed_Cases:{Confirmed},Deaths:{deaths},Recovered:{recovered}
          Almost {int(death_to_recovery * 100)} people die in compare to 100 recovered
          Cases_resulted are:{resulted * Confirmed},Cases_remaining_results:{int(remainingCases * Confirmed / 100)}
         '''
    label['text']=f



HEIGHT = 500

WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

canvas.pack()

background_image = tk.PhotoImage(file='landscape[1].png')

background_label = tk.Label(root,image=background_image)

background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)

frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=40)

entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Set Country", font=40, command=lambda: method(entry.get()))

button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)

lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)

label.place(relwidth=1, relheight=1)

root.mainloop()
