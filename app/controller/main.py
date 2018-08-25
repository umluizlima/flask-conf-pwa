from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


atividades = [
    {
        'title': 'Credenciamento',
        'time': '09:00 - 10:00'
    },
    {
        'title': 'Abertura',
        'time': '10:00 - 10:10'
    },
    {
        'title': 'Usando o Flask Admin com segurança e flexibilidade',
        'time': '10:20 - 11:00',
        'speaker': 'Bruno Rocha'
    },
    {
        'title': 'Aplicações web com Flask e Docker',
        'time': '11:10 - 11:50',
        'speaker': 'Felipe Alcantara'
    },
    {
        'title': 'Almoço / Networking',
        'time': '12:00 - 13:40'
    },
    {
        'title': 'Escrevendo Testes com Flask e #JustPython',
        'time': '14:35 - 15:15',
        'speaker': 'Eduardo Mendes'
    },
    {
        'title': 'Inteligência Artificial, Flask e Raspberry Pi',
        'time': '17:50 - 18:30',
        'speaker': 'Eduardo Pereira'
    },
    {
        'title': 'API REST o começo: Introdução a REST para iniciantes',
        'time': '13:45 - 14:05',
        'speaker': 'Talita Rossari'
    },
    {
        'title': 'Flask Profiling: Técnicas para identificação de \
pontos críticos de performance',
        'time': '17:00 - 17:40',
        'speaker': 'Iuri de Silvio'
    },
    {
        'title': 'API REST em Flask + Vue.js: Aplicações modernas \
com separação entre frontend e backend',
        'time': '14:10 - 14:30',
        'speaker': 'João Lugão'
    },
    {
        'title': 'Lightning Talks',
        'time': '15:25 - 15:55'
    },
    {
        'title': 'Coffee Break / Networking',
        'time': '16:00 - 16:30'
    },
    {
        'title': 'Introdução ao Sanic - O clone assíncrono do Flask',
        'time': '16:35 - 16:55',
        'speaker': 'Danilo Bellini'
    },
    {
        'title': 'Flask + PWA - Mobile Applications',
        'time': '18:40 - 19:00',
        'speaker': 'Luiz Lima'
    },
    {
        'title': 'Encerramento / Sorteios',
        'time': '19:05 - 19:35'
    },
]


@bp.route('/')
def index():
    return render_template(
        'main/index.html',
        title='Flask Conf 2018'
    )


@bp.route('/agenda')
def agenda():
    return render_template(
        'main/agenda.html',
        title='Palestras',
        agenda=sorted(atividades, key=lambda k: k['time'])
    )


@bp.route('/cdc')
def cdc():
    return render_template(
        'main/cdc.html',
        title='Código de conduta'
    )


@bp.route('/local')
def local():
    return render_template(
        'main/local.html',
        title='Local'
    )
