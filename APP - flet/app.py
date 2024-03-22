import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.page):
    page.title = "Cadastro App"

    lista_produtos = ft.ListView()

    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(ft.Container(
                ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                ))
            txt_erro.visible = False
            txt_acerto.visible = True
        except:
            txt_erro.visible = True
            txt_acerto.visible = False

        page.update()
        print('Produto salvo com sucesso.')

    txt_erro = ft.Container(ft.Text("Erro ao salvar produto!"), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text("Produto salvo com sucesso!"), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)


    txt_titulo = ft.Text('Título do produto:')
    produto = ft.TextField(label="Digite o título do produto...", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto')
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_acerto,
        txt_erro,
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )

    page.add(
        lista_produtos,
    )

ft.app(target=main)