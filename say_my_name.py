# escreve o nome, aperta no botão adiciona na tela :)
import flet as ft
import time
def main(page: ft.Page):
    
    page.title = "Sistema de name"
    t = ft.TextField(label="Digite seu nome", width=300)
    t_coluna = ft.Column()
    def clicked(e): #função chamada quando o botão é clicado, e = evento/event
        time.sleep(1)
        nome = t.value
        t_coluna.controls.append(ft.Text(f"Olá, {nome}!"))
        page.update()
        nome = ""
    # button com largura de 150
    button = ft.Button("Say my name", on_click= clicked, width=150)
    page.add(t, button, t_coluna) #adicionar o texto à página

ft.app(main)

