
import webbrowser
import threading
import time

from nicegui import ui
from maquinas import MAQUINAS


@ui.page('/maquina/{nome}')
def pagina_maquina(nome: str):

    maquina = MAQUINAS.get(nome)

    if maquina is None:
        ui.label(
            'Máquina não encontrada'
        ).classes(
            'text-2xl text-red-600'
        )
        return

    with ui.column().classes(
        'w-full max-w-6xl mx-auto p-6'
     ):
          with ui.row().classes(
          'w-full items-center justify-between mb-4'
          ):
               ui.label(
                    'Orion - Machinfo'
               ).classes(
                    'text-4xl font-bold'
          )

               ui.button(
                    'ChatBot',
                    on_click=lambda: ui.navigate.to('https://orion-h600.netlify.app') #colocar URL do chatbot
               ).classes(
                    'bg-blue-600 text-white text-xl px-8 py-4 rounded-lg'
          )

          ui.label(
               nome
          ).classes(
               'text-3xl font-bold mb-6'
          )

          with ui.row().classes(
            'w-full items-start gap-6'
        ):

            with ui.card().classes(
                'flex-1 min-w-0'
            ):

                ui.label(
                    'Informações principais'
                ).classes(
                    'text-2xl font-bold mb-4'
                )

                ui.label(
                    f"Código: {maquina['codigo']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Tipo: {maquina['tipo']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Marca: {maquina['marca']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Modelo: {maquina['modelo']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Ano: {maquina['ano']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Horas trabalhadas: {maquina['horas']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Status: {maquina['status']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Tempo de garantia: {maquina['garantia']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Eficiência: {maquina['eficiencia_declarada']}"
                ).classes('text-lg mb-2')

                ui.label(
                    f"Código FINAME: {maquina['codigo_finame']}"
                ).classes('text-lg mb-2')

            with ui.card().classes(
                'flex-1 min-w-0'
            ):

                ui.label(
                    'Plantadeiras compatíveis'
                ).classes(
                    'text-2xl font-bold mb-4'
                )
                for plantadeira in maquina['plantadeiras_compativeis']:
                    ui.label(
                         f'• {plantadeira}'
                    ).classes(
                         'text-lg mb-2'
                    )
# ==========================================
# ABERTURA AUTOMÁTICA DO NAVEGADOR
# ==========================================
#retirar todo o código abaixo ou comentar para ser hospedado em servidor
def abrir_navegador():

    time.sleep(2)

    url = (
        'http://127.0.0.1:8080/'
        'maquina/Hunter%20H600'
    )

    webbrowser.open(url)


threading.Thread(
    target=abrir_navegador,
    daemon=True
).start()
#ate aqui

# ==========================================
# INICIA O SERVIDOR NICEGUI
# ==========================================
ui.run(
    host='0.0.0.0',
    port=8080,
    show=False,
    reload=False
)
