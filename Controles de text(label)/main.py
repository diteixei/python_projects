import flet as ft

def main(page: ft.Page):
    #t = ft.Text(value="Olá Mundo!", color="green")
    
    a = ft.Text("A")
    b = ft.Text("B")
    c = ft.Text("C")
            
    page.add(ft.Row( controls=[a,b,c]))

    #t.value = "Olá Mesma!"
    #t.color = "red"

    #page.update()
    
    #page.controls.append(t)
    #age.update()

ft.app(target=main)