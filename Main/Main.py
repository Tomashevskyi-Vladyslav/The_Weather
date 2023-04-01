from tkinter import *
import requests
import json

# ------------------------------

api = '28435134d848dceb376a9791fcf97829'
city = 'Херсон'
url = 'https://api.openweathermap.org/data/2.5/weather?appid='

# ------------------------------


def change_city(event):
    global city

    city = en.get()
    lb.config(text=city)
    en.delete(0, END)


def update():
    complete_url = url + api + '&q=' + city
    response = requests.get(complete_url)
    x = response.json()

    if x['cod'] == 200:
        main = x['main']
        temp = main['temp'] - 273.15

        press = main['pressure']
        hum = main['humidity']

        temp = round(temp, 2)
        tmp.config(text=f'{temp} C')
        description = x['weather'][0]['description']

        pressure = Label(text=f'''{press} p''', font=('Consolas', 20))
        pressure.place(relx=0.25, rely=0.65, anchor=CENTER)

        humidity = Label(text=f'''{hum} φ''', font=('Consolas', 20))
        humidity.place(relx=0.75, rely=0.65, anchor=CENTER)

        if 'cloud' in description: img.config(image=cloudy)
        elif 'clear' in description: img.config(image=clear)
        elif 'rain' in description: img.config(image=rain)
        elif 'snow' in description: img.config(image=snow)
        elif 'storm' in description: img.config(image=storm)
        else: img.config(image=mist)

    tmp.after(2000, update)


# ------------------------------

root = Tk()
root.title('WEATHER')
root.geometry('350x350')

lb = Label(text=city, font=('Consolas', 30))
lb.place(relx=0.5, rely=0.1, anchor=CENTER)

# ------------------------------

clear = PhotoImage(file='clear.png')
cloudy = PhotoImage(file='cloudy.png')
mist = PhotoImage(file='mist.png')
rain = PhotoImage(file='rain.png')
snow = PhotoImage(file='snow.png')
storm = PhotoImage(file='storm.png')

img = Label(image=clear)
img.place(relx=0.5, rely=0.35, anchor=CENTER)

# ------------------------------

tmp = Label(text='0 C', font=('Consolas', 20))
tmp.place(relx=0.5, rely=0.5, anchor=CENTER)


en = Entry(font=('Consolas', 25), justify=CENTER)
en.place(relx=0.5, rely=0.85, anchor=CENTER)
en.focus()

update()
root.bind('<Return>', change_city)
root.mainloop()

