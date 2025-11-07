# caminho do arquivo C: -> pasta nomeada qualquer -> src -> main.py
import flet as ft
import time
def main(page: ft.Page):

    page.title = "Contador"
    t = ft.Text()
    page.add(t)

    for i in range(10):
        t.value = f"Contagem: {i}"
        page.update()
        time.sleep(1)
        
ft.app(main)

# irá abrir uma aba/página com um contador :)
