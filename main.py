import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro de Usuários"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20

    usuarios = []

    nome_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="E-mail", width=300)
    lista_cadastros = ft.Column()

    def cadastrar_usuario(e):
        nome = nome_input.value.strip()
        email = email_input.value.strip()
        if nome and email:
            usuarios.append({"nome": nome, "email": email})
            lista_cadastros.controls.append(
                ft.Text(f"• {nome} - {email}")
            )
            nome_input.value = ""
            email_input.value = ""
            page.update()
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Preencha todos os campos!"))
            page.dialog.open = True
            page.update()

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        on_click=cadastrar_usuario
    )

    page.add(
        ft.Text("Cadastro de Usuários", size=24, weight="bold"),
        nome_input,
        email_input,
        botao_cadastrar,
        ft.Divider(),
        ft.Text("Usuários Cadastrados:", size=18, weight="w500"),
        lista_cadastros
    )

ft.app(target=main)
