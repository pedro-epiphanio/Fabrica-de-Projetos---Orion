
import os
from urllib.parse import quote

from nicegui import ui
from maquinas import MAQUINAS


ui.add_head_html("""
<style>
    :root {
        --bg: #090F16;
        --surface: #121D27;
        --surface-light: #1A2933;
        --border: #263B43;
        --green: #176B4D;
        --green-light: #28A879;
        --green-soft: #A3D9BE;
        --text: #F1F5F9;
        --muted: #91A3AF;
    }

    body {
        background: var(--bg) !important;
        color: var(--text);
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
    }

    .page-shell {
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 32px 24px;
        min-height: 100vh;
    }

    .topbar {
        width: 100%;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
        padding-bottom: 22px;
        margin-bottom: 30px;
        border-bottom: 1px solid var(--border);
    }

    .brand {
        color: var(--text);
        font-size: 25px;
        font-weight: 800;
        letter-spacing: 1.5px;
    }

    .brand span {
        color: var(--green-light);
    }

    .subtitle {
        color: var(--muted);
        font-size: 14px;
        line-height: 1.6;
    }

    .hero {
        width: 100%;
        padding: 30px;
        border-radius: 16px;
        background: linear-gradient(
            120deg,
            #142B28 0%,
            #121D27 65%,
            #14232D 100%
        );
        border: 1px solid #285044;
        margin-bottom: 24px;
    }

    .hero-title {
        color: var(--text);
        font-size: clamp(25px, 4vw, 34px);
        font-weight: 800;
        letter-spacing: -0.8px;
    }

    .hero-description {
        color: #A3B8B0;
        font-size: 15px;
        margin-top: 8px;
        line-height: 1.6;
    }

    .panel {
        width: 100%;
        padding: 26px;
        border-radius: 15px;
        background: var(--surface) !important;
        border: 1px solid var(--border);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        color: var(--text);
    }

    .section-title {
        color: var(--text);
        font-size: 21px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .machine-btn {
        width: 100%;
        min-height: 58px;
        padding: 12px 18px;
        border-radius: 11px;
        background: var(--surface-light) !important;
        border: 1px solid var(--border);
        color: var(--text) !important;
        font-size: 15px;
        font-weight: 600;
        justify-content: flex-start;
        transition: all 0.2s ease;
    }

    .machine-btn:hover {
        background: #1B3A31 !important;
        border-color: var(--green-light);
        transform: translateY(-2px);
    }

    .machine-btn .q-icon {
        color: var(--green-light);
    }

    .primary-btn {
        background: var(--green) !important;
        color: white !important;
        border: 1px solid #27835F;
        border-radius: 10px;
        padding: 10px 22px;
        min-height: 44px;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    .primary-btn:hover {
        background: #20835E !important;
        transform: translateY(-2px);
    }

    .secondary-btn {
        background: var(--surface-light) !important;
        color: var(--green-soft) !important;
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 9px 18px;
        min-height: 44px;
    }

    .secondary-btn:hover {
        background: #1B3A31 !important;
        border-color: var(--green);
    }

    .info-grid {
        width: 100%;
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 13px;
    }

    .info-item {
        width: 100%;
        padding: 16px;
        border-radius: 11px;
        background: var(--surface-light) !important;
        border: 1px solid var(--border);
        box-shadow: none;
    }

    .info-label {
        color: var(--muted);
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin-bottom: 7px;
    }

    .info-value {
        color: var(--text);
        font-size: 16px;
        font-weight: 650;
        overflow-wrap: anywhere;
    }

    .plantadeira-item {
        width: 100%;
        padding: 14px;
        margin-bottom: 10px;
        border-radius: 10px;
        background: #142B25 !important;
        border: 1px solid #285044;
        color: var(--green-soft) !important;
        font-size: 14px;
        font-weight: 600;
    }

    .q-card {
        color: var(--text);
    }

    .footer {
        width: 100%;
        padding-top: 24px;
        margin-top: 30px;
        border-top: 1px solid var(--border);
        text-align: center;
        color: #647985;
        font-size: 12px;
    }

    @media (max-width: 700px) {
        .page-shell {
            padding: 18px 14px;
        }

        .topbar {
            margin-bottom: 20px;
            padding-bottom: 17px;
        }

        .brand {
            font-size: 21px;
        }

        .hero {
            padding: 22px 18px;
        }

        .panel {
            padding: 18px;
        }

        .section-title {
            font-size: 19px;
        }

        .info-grid {
            grid-template-columns: 1fr !important;
        }

        .primary-btn {
            width: 100%;
        }
    }
</style>
""", shared=True)


def criar_info(titulo, valor):
    with ui.card().classes('info-item'):
        ui.label(titulo).classes('info-label')
        ui.label(str(valor)).classes('info-value')


def criar_cabecalho():
    with ui.row().classes('topbar'):
        ui.html(
            '<div class="brand">ORION <span>| MACHINFO</span></div>'
        )

        ui.label(
            'INTELLIGENT MACHINERY INFORMATION'
        ).classes('subtitle')


def criar_rodape():
    ui.label(
        'ORION MACHINFO  |  Tecnologia e informação para o agronegócio'
    ).classes('footer')


@ui.page('/')
def pagina_inicial():

    with ui.column().classes('page-shell'):

        criar_cabecalho()

        with ui.column().classes('hero'):
            ui.label(
                'Conheça seus equipamentos.'
            ).classes('hero-title')

            ui.label(
                'Acesse informações técnicas, especificações e compatibilidade '
                'de máquinas em um só lugar.'
            ).classes('hero-description')

        with ui.card().classes('panel'):

            ui.label(
                'Equipamentos disponíveis'
            ).classes('section-title')

            ui.label(
                'Selecione uma máquina para visualizar seus dados técnicos.'
            ).classes('subtitle mb-6')

            for nome in MAQUINAS:

                ui.button(
                    nome,
                    icon='precision_manufacturing',
                    on_click=lambda n=nome: ui.navigate.to(
                        f'/maquina/{quote(n, safe="")}'
                    )
                ).classes('machine-btn')

        criar_rodape()


@ui.page('/maquina/{nome}')
def pagina_maquina(nome: str):

    maquina = MAQUINAS.get(nome)

    if maquina is None:

        with ui.column().classes('page-shell'):

            criar_cabecalho()

            ui.label(
                'Máquina não encontrada'
            ).classes('hero-title')

            ui.button(
                'Voltar ao início',
                icon='arrow_back',
                on_click=lambda: ui.navigate.to('/')
            ).classes('secondary-btn')

        return

    with ui.column().classes('page-shell'):

        criar_cabecalho()

        with ui.row().classes('w-full items-center justify-between gap-3 flex-wrap mb-6'):

            ui.label(nome).classes('hero-title')

            with ui.row().classes('gap-2 flex-wrap'):

                ui.button(
                    'Voltar',
                    icon='arrow_back',
                    on_click=lambda: ui.navigate.to('/')
                ).classes('secondary-btn')

                ui.button(
                    'ChatBot',
                    icon='smart_toy',
                    on_click=lambda: ui.navigate.to(
                        'https://orionchatbot.netlify.app/'
                    )
                ).classes('primary-btn')

        with ui.row().classes('w-full items-start gap-4 flex-wrap'):

            with ui.card().classes('panel flex-1 min-w-0'):

                ui.label(
                    'Informações principais'
                ).classes('section-title')

                ui.label(
                    'Dados técnicos do equipamento'
                ).classes('subtitle mb-4')

                with ui.grid(columns=2).classes('info-grid'):

                    criar_info('Código', maquina['codigo'])
                    criar_info('Tipo', maquina['tipo'])
                    criar_info('Marca', maquina['marca'])
                    criar_info('Modelo', maquina['modelo'])
                    criar_info('Ano', maquina['ano'])
                    criar_info('Horas trabalhadas', maquina['horas'])
                    criar_info('Status', maquina['status'])
                    criar_info('Tempo de garantia', maquina['garantia'])
                    criar_info('Eficiência', maquina['eficiencia_declarada'])
                    criar_info('Código FINAME', maquina['codigo_finame'])

            with ui.card().classes('panel flex-1 min-w-0'):

                ui.label(
                    'Plantadeiras compatíveis'
                ).classes('section-title')

                ui.label(
                    'Equipamentos compatíveis com este modelo'
                ).classes('subtitle mb-4')

                for plantadeira in maquina['plantadeiras_compativeis']:

                    ui.label(
                        f'✓  {plantadeira}'
                    ).classes('plantadeira-item')

        criar_rodape()


port = int(os.environ.get('PORT', 8080))

ui.run(
    host='0.0.0.0',
    port=port,
    show=False,
    reload=False
)
