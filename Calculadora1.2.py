from tkinter import *
windows=Tk()
windows.title("Calculadora 1.2 ")

#Frame
ventana=Frame(windows)
ventana.grid(row=0, column=0,padx=(10,10), pady=(10,10))
ventana.pack()

#Elementos
en_pantalla=Entry(ventana,font="Roboto 20")
en_pantalla.grid(row=0, column=0,columnspan=4)
i=0
def Click_boton(valor):
    global i
    en_pantalla.insert(i,valor)
    i+=1
def Borrar():
    en_pantalla.delete(0,END)
    i=0
def Igual():
    
        ecuacion=en_pantalla.get()
        resultado=eval(ecuacion)
        en_pantalla.delete(0, END)
        en_pantalla.insert(0,resultado)
        i=0
  
#primera fila
btn_borrar=Button(ventana,text="AC",width=5,height=2,command=lambda: Borrar())
btn_paren1=Button(ventana,text="(",width=5,height=2,command=lambda: Click_boton("("))
btn_paren2=Button(ventana,text=")",width=5,height=2,command=lambda: Click_boton(")"))
btn_division=Button(ventana,text="/",width=5,height=2,command=lambda: Click_boton("/"))

btn_borrar.grid(row=1,column=0,pady=3)
btn_paren1.grid(row=1,column=1,pady=3)
btn_paren2.grid(row=1,column=2,padx=3)
btn_division.grid(row=1,column=3,padx=3)

#segunda fila
btn_7=Button(ventana,text="7",width=5,height=2,command=lambda: Click_boton(7))
btn_8=Button(ventana,text="8",width=5,height=2,command=lambda: Click_boton(8))
btn_9=Button(ventana,text="9",width=5,height=2,command=lambda: Click_boton(9))
btn_producto=Button(ventana,text="*",width=5,height=2,command=lambda: Click_boton("*"))

btn_7.grid(row=2,column=0,pady=3)
btn_8.grid(row=2,column=1,pady=3)
btn_9.grid(row=2,column=2,pady=3)
btn_producto.grid(row=2,column=3,pady=3)

#tercera fila
btn_4=Button(ventana,text="4",width=5,height=2,command=lambda: Click_boton(4))
btn_5=Button(ventana,text="5",width=5,height=2,command=lambda: Click_boton(5))
btn_6=Button(ventana,text="6",width=5,height=2,command=lambda: Click_boton(6))
btn_suma=Button(ventana,text="+",width=5,height=2,command=lambda: Click_boton("+"))

btn_4.grid(row=3,column=0,pady=3)
btn_5.grid(row=3,column=1,pady=3)
btn_6.grid(row=3,column=2,pady=3)
btn_suma.grid(row=3,column=3,pady=3)

#cuarta fila
btn_1=Button(ventana,text="1",width=5,height=2,command=lambda: Click_boton(1))
btn_2=Button(ventana,text="2",width=5,height=2,command=lambda: Click_boton(2))
btn_3=Button(ventana,text="3",width=5,height=2,command=lambda: Click_boton(3))
btn_resta=Button(ventana,text="-",width=5,height=2,command=lambda: Click_boton("-"))

btn_1.grid(row=4,column=0,pady=3)
btn_2.grid(row=4,column=1,pady=3)
btn_3.grid(row=4,column=2,pady=3)
btn_resta.grid(row=4,column=3,pady=3)

#quinta fila
btn_0=Button(ventana,text="0",width=15,height=2,command=lambda: Click_boton(0))
btn_punto=Button(ventana,text=".",width=5,height=2,command=lambda: Click_boton("."))
btn_igual=Button(ventana,text="=",width=5,height=2,command=lambda: Igual())

btn_0.grid(row=5,column=0,columnspan=2,pady=3)
btn_punto.grid(row=5,column=2,pady=3)
btn_igual.grid(row=5,column=3,pady=3)

windows.mainloop()
