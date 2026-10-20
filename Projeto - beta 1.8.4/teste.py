# Importa o módulo responsável por abrir páginas
# no navegador padrão do computador.
import webbrowser

# Importa o módulo threading para podermos executar
# uma tarefa separada enquanto o servidor inicia.
import threading

# Importa o módulo time para podermos esperar
# alguns segundos antes de abrir o navegador.
import time

# Importa o NiceGUI, que será utilizado
# para criar o nosso site.
from nicegui import ui

# Importa o dicionário MAQUINAS do arquivo maquinas.py.
from maquinas import MAQUINAS


# ============================================================
# PÁGINA DA MÁQUINA
# ============================================================

# Define a URL da página.
# O valor {nome} será recebido através da URL.
#
# Exemplo:
# http://127.0.0.1:8080/maquina/Hunter%20H600
#
@ui.page('/maquina/{nome}')
def pagina_maquina(nome: str):

    # Procura a máquina dentro do dicionário MAQUINAS.
    maquina = MAQUINAS.get(nome)

    # Verifica se a máquina não existe.
    if maquina is None:

        # Mostra uma mensagem de erro.
        ui.label(
            'Máquina não encontrada'
        ).classes(
            'text-2xl text-red-600'
        )

        # Para a execução da função.
        return

    # Cria uma coluna principal.
    # w-full = utiliza toda a largura disponível.
    # max-w-4xl = limita a largura máxima.
    # mx-auto = centraliza a coluna.
    # p-6 = adiciona espaçamento interno.
    with ui.column().classes(
        'w-full max-w-4xl mx-auto p-6'
    ):

        # Título do sistema.
        ui.label(
            'Orion - Machinfo'
        ).classes(
            'text-4xl font-bold mb-8'
        )

        # Nome da máquina.
        ui.label(
            nome
        ).classes(
            'text-3xl font-bold mb-6'
        )

        # Cria um cartão para organizar
        # as informações da máquina.
        with ui.card().classes(
            'w-full'
        ):

            # Código da máquina.
            ui.label(
                f"Código: {maquina['codigo']}"
            ).classes(
                'text-xl mb-2'
            )

            # Tipo da máquina.
            ui.label(
                f"Tipo: {maquina['tipo']}"
            ).classes(
                'text-xl mb-2'
            )

            # Marca da máquina.
            ui.label(
                f"Marca: {maquina['marca']}"
            ).classes(
                'text-xl mb-2'
            )

            # Modelo da máquina.
            ui.label(
                f"Modelo: {maquina['modelo']}"
            ).classes(
                'text-xl mb-2'
            )

            # Ano da máquina.
            ui.label(
                f"Ano: {maquina['ano']}"
            ).classes(
                'text-xl mb-2'
            )

            # Horas trabalhadas.
            ui.label(
                f"Horas Trabalhadas: {maquina['horas']}"
            ).classes(
                'text-xl mb-2'
            )

            # Status da máquina.
            ui.label(
                f"Status: {maquina['status']}"
            ).classes(
                'text-xl mb-2'
            )

            # Tempo de garantia.
            ui.label(
                f"Tempo de garantia: {maquina['garantia']}"
            ).classes(
                'text-xl mb-2'
            )

            # Eficiência declarada.
            ui.label(
                f"Eficiência: {maquina['eficiencia_declarada']}"
            ).classes(
                'text-xl mb-2'
            )

            # Código FINAME.
            ui.label(
                f"Código Finame: {maquina['codigo_finame']}"
            ).classes(
                'text-xl mb-4'
            )

            # Linha separadora.
            ui.separator()

            # Título da seção de plantadeiras.
            ui.label(
                'Plantadeiras compatíveis'
            ).classes(
                'text-2xl font-bold mt-4 mb-2'
            )

            # Percorre todas as plantadeiras compatíveis.
            for plantadeira in maquina[
                'plantadeiras_compativeis'
            ]:

                # Mostra cada plantadeira.
                ui.label(
                    f'• {plantadeira}'
                ).classes(
                    'text-lg'
                )


# ============================================================
# ABERTURA AUTOMÁTICA DO NAVEGADOR
# ============================================================

# Cria uma função responsável por abrir
# a página correta no navegador.
def abrir_navegador():

    # Espera 2 segundos para garantir que
    # o servidor NiceGUI já esteja funcionando.
    time.sleep(2)

    # Define a URL que queremos abrir.
    url = (
        'http://127.0.0.1:8080/'
        'maquina/Hunter%20H600'
    )

    # Abre somente essa URL no navegador padrão.
    webbrowser.open(url)


# Cria uma thread separada para abrir o navegador.
#
# Isso permite que o NiceGUI continue iniciando
# o servidor normalmente.
threading.Thread(
    target=abrir_navegador,
    daemon=True
).start()


# ============================================================
# INICIA O SERVIDOR NICEGUI
# ============================================================

# Inicia o servidor web.
ui.run(

    # Permite acesso pelo computador local
    # e também por outros dispositivos da rede.
    host='0.0.0.0',

    # Define a porta do servidor.
    port=8080,

    # MUITO IMPORTANTE:
    # impede o NiceGUI de abrir automaticamente
    # outra aba do navegador.
    show=False,

    # Desativa o modo de recarregamento automático.
    reload=False
)
