import tkinter.font as font
from tkinter.filedialog import askopenfilename
import os
from tkinter import ttk,filedialog
from tkinter import *
from tkinter import Tk,Frame,Label
import tkinter as tk
import pandas as pd
import csv
from pytsmp import STAMP
import mass_ts  as  mts
from pandas import read_csv
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np

fen = tk.Tk()
fen.title("My application")
fen.geometry("1000x620")
fen.config(background='#001a33')
fen.minsize(400,400)
fen.resizable(width=False,height=False)

wrapper1 = LabelFrame(fen)
wrapper1.config(background='#001a33')
wrapper2 = LabelFrame(fen)
wrapper2.config(background='#001a33')
wrapper3 = LabelFrame(fen,height='2')
wrapper3.config(background='#001a33')

wrapper1.pack(fill="both",expand="yes",padx=5,pady=5,ipadx=5,ipady=5)
wrapper2.pack(fill="both",expand="yes",padx=10,pady=10,ipadx=10,ipady=10)
wrapper3.pack(fill="both",expand="yes",padx=5,pady=5,ipadx=2,ipady=2)

tv1 = ttk.Treeview(wrapper2,columns=(1))
tv1.place(relx=0,rely=0)

treescrolly = ttk.Scrollbar(wrapper2,orient="vertical",
                            command=tv1.yview)  # command means update the yaxis view of the widget
treescrollx = ttk.Scrollbar(wrapper2,orient="horizontal",
                            command=tv1.xview)  # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set,
              yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
# treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
# treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

tv = ttk.Treeview(wrapper2)
tv.place(relx=0.75,rely=0)

tv['columns'] = ('Class_A')
tv.column('#0',width=0,stretch=NO)
tv.column('Class_A',anchor=CENTER)
tv.heading('#0',text='',anchor=CENTER)
tv.heading('Class_A',text='Class_A',anchor=CENTER)

treescrolly = tk.Scrollbar(wrapper2,orient="vertical",
                           command=tv.yview)  # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(wrapper2,orient="horizontal",
                           command=tv.xview)  # command means update the xaxis view of the widget
tv.configure(xscrollcommand=treescrollx.set,
             yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
'''
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
'''


def open(self):
    file_path = listbox.get(listbox.curselection())
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information "," Le fichier que vous avez choisi n'est pas valide")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information ",f" Aucun fichier tel que {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column,text=column)  # let the column heading = column name

    df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("","end",
                   values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


def open1(self):
    file_path = listbox1.get(listbox1.curselection())
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information "," Le fichier que vous avez choisi n'est pas valide")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information ",f" Aucun fichier tel que {file_path}")
        return None

    clear_data1()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column,text=column)  # let the column heading = column name

    df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("","end",
                   values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data1():
    tv1.delete(*tv1.get_children())
    return None


def traitement1():
    chemin = filedialog.askopenfilename(initialdir="/",filetypes=[('CSV','*.csv')])
    if chemin == '':
        return None
    else:
        listbox1.insert(0,chemin)
    return None


def traitement():
    chemin = filedialog.askopenfilename(initialdir="/",filetypes=[('CSV','*.csv')])
    if chemin == '':
        return None
    else:
        listbox.insert(0,chemin)
    return None


def vis1():
    if listbox.curselection():
        file = listbox.get(listbox.curselection())
        series = read_csv(file,header=0,index_col=0,parse_dates=True,squeeze=True)
        series.plot()
    else:
        file = listbox1.get(listbox1.curselection())
        series = read_csv(file,header=0,index_col=0,parse_dates=True,squeeze=True)
        series.plot()
    pyplot.show()


def vis2():
    file = listbox.get(listbox.curselection())
    file2 = listbox1.get(listbox1.curselection())
    fig,axs = plt.subplots(2)
    x = read_csv(file,header=0,index_col=0,parse_dates=True,squeeze=True)
    y = read_csv(file2,header=0,index_col=0,parse_dates=True,squeeze=True)
    axs[0].plot(x)
    axs[1].plot(y)
    plt.show()


def mass():
    ts = []
    m = int(name1.get())
    for i in range(0,listbox.size(),1):
        file = listbox.get(i)
        df = pd.read_csv(file)
        ts.append(df)
    concatDf = pd.concat(ts,axis=0)
    # mass

    distances = mts.mass2(np.array(concatDf["Value"]),np.array(concatDf["Value"][0:m]))
    print(distances)

    ts1 = []
    for i in range(0,listbox1.size(),1):
        file1 = listbox1.get(i)
        df1 = pd.read_csv(file1)
        ts1.append(df1)
    concatDf1 = pd.concat(ts1,axis=0)
    # mass
    distances1 = mts.mass2(np.array(concatDf1["Value"]),np.array(concatDf1["Value"][0:m]))
    print(distances1)


def classi():
    chemin1 = filedialog.askopenfilename(initialdir="/",filetypes=[('CSV','*.csv')])

    ts = []
    m = int(name1.get())
    for i in range(0,listbox.size(),1):
        file = listbox.get(i)
        df = pd.read_csv(file)
        ts.append(df)
    concatDf = pd.concat(ts,axis=0)
    currentItem = tv.focus()
    b = tv.item(currentItem)['values']
    z = int(b[0])
    s = pd.read_csv(chemin1)
    s3 = np.array(s["Value"])
    query = np.array(concatDf["Value"][(z):(z + m)])

    mp = STAMP(s3,query,window_size=m)
    mat_profile3,ind_profile = mp.get_profiles()

    lab = Label(wrapper2,foreground="white",background="#001a33")
    lab['font'] = f_label
    lab.place(relx=0.47,rely=0.35)




    r = 0
    for i in range(0,len(mat_profile3),1):
        if ((float(mat_profile3[i])) < 0.1):
            r = 1

    if (r == 1):
        lab['text'] = str("Les deux séries sont " + "\n" + " dans la même classe")
    else:
        lab['text'] = str("Les deux séries ne sont pas " + "\n" + " dans la même classe")

    return None

def stamp():
    ts = []
    for i in range(0,listbox.size(),1):
        file = listbox.get(i)
        df = pd.read_csv(file)
        ts.append(df)
    concatDf = pd.concat(ts,axis=0)
    ts1 = []
    for i in range(0,listbox1.size(),1):
        file1 = listbox1.get(i)
        df1 = pd.read_csv(file1)
        ts1.append(df1)
    concatDf1 = pd.concat(ts1,axis=0)

    s1 = np.array(concatDf["Value"])
    query = np.array(concatDf["Value"])
    query1 = np.array(concatDf1["Value"])
    m = int(name1.get())
    mp = STAMP(s1,query,window_size=m)
    mat_profile,ind_profile = mp.get_profiles()
    print(mat_profile)

    mp1 = STAMP(s1,query1,window_size=m)
    mat_profile1,ind_profile1 = mp1.get_profiles()
    print(mat_profile1)

    mat3 = (mat_profile1 - mat_profile)

    plt.subplot(3,1,1)
    plt.plot(mat_profile)
    plt.title('P_AA')

    plt.subplot(3,1,2)
    plt.plot(mat_profile1)
    plt.title('P_AB')

    plt.subplot(3,1,3)
    plt.plot(mat3)
    plt.title('P_AB - P_AA')
    seuil = float(name2.get())
    plt.axhline(seuil,color='r',linestyle='dashed')
    plt.show()

    for i in range(0,len(mat3),1):
        if ((float(mat3[i])) > seuil):
            tv.insert("","end",values=i)
    return None


def ploSh(self):
    ts = []

    m = int(name1.get())
    for i in range(0,listbox.size(),1):
        file = listbox.get(i)
        df = pd.read_csv(file)
        ts.append(df)
    concatDf = pd.concat(ts,axis=0)
    currentItem = tv.focus()
    b = tv.item(currentItem)['values']
    z = int(b[0])
    v = np.array(concatDf["Value"][z:(z + m)])
    plt.plot(v)
    plt.show()


tv.bind('<Double-1>',ploSh)

f_label = font.Font(family='Times New Roman',size=14)
f_bouton = font.Font(family='Times New Roman',size=12,weight="bold")
label = Label(wrapper1,
              text="\n" + "Bonjour! Bienvenue dans notre application." + "\n" + "\n" + "Veuillez sélectionner un fichier Excel ou CSV :" + "\n",
              foreground="white",background="#001a33")
label['font'] = f_label
label.pack()

name = tk.IntVar()
label1 = Label(wrapper1,text="Entrer la valeur du m:",foreground="white",background="#001a33")
label1['font'] = f_label
label1.pack()
name1 = Entry(wrapper1,textvariable=name,width='7')
name1.pack()

name2 = DoubleVar()
label2 = Label(wrapper1,text="\n" + "Entrer la valeur du seuil:",foreground="white",background="#001a33")
label2['font'] = f_label
label2.pack()
name3 = Entry(wrapper1,textvariable=name2,width='7')
val2 = name3.get()
name3.pack()

f_bouton1 = font.Font(family='Times New Roman',size=12,weight="bold")

bouton = Button(wrapper1,text='Charger S2',command=lambda: traitement())
bouton.place(relx=0.75,rely=0.25,height=40,width=85)
bouton.configure(foreground="#2B00FA")
bouton['font'] = f_bouton

boutonn = Button(wrapper1,text='Charger S1',command=lambda: traitement1())
boutonn.place(relx=0.15,rely=0.25,height=40,width=85)
boutonn.configure(foreground="#2B00FA")
boutonn['font'] = f_bouton

listbox = Listbox(wrapper1,selectmode=MULTIPLE,exportselection=0,height='8',width='55')
listbox.place(relx=0.63,rely=0.45)

listbox1 = Listbox(wrapper1,selectmode=MULTIPLE,exportselection=0,height='8',width='55')
listbox1.place(relx=0.03,rely=0.45)

listbox.bind('<Double-Button>',open)
listbox1.bind('<Double-Button>',open1)

bouton1 = Button(wrapper3,text='Visualiser1',command=lambda: vis1())
bouton1.place(relx=0.04,rely=0.35,height=40,width=85)
bouton1.configure(foreground="#2B00FA")
bouton1['font'] = f_bouton

bouton2 = Button(wrapper3,text='Visualiser2',command=lambda: vis2())
bouton2.place(relx=0.18,rely=0.35,height=40,width=85)
bouton2.configure(foreground="#2B00FA")
bouton2['font'] = f_bouton

bouton3 = Button(wrapper3,text='Algorithme de MASS',command=lambda: mass())
bouton3.place(relx=0.32,rely=0.35,height=40,width=170)
bouton3.configure(foreground="#2B00FA")
bouton3['font'] = f_bouton

bouton4 = Button(wrapper3,text='Algorithme de STAMP',command=lambda: stamp())
bouton4.place(relx=0.55,rely=0.35,height=40,width=170)
bouton4.configure(foreground="#2B00FA")
bouton4['font'] = f_bouton

bouton5 = Button(wrapper3,text='Classification',command=lambda: classi())
bouton5.place(relx=0.78,rely=0.35,height=40,width=170)
bouton5.configure(foreground="#2B00FA")
bouton5['font'] = f_bouton

fen.mainloop()