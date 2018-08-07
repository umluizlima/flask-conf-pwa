from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


atividades = [
    {
        'title': 'Credenciamento',
        'time': '08:00'
    },
    {
        'title': 'Usando o Flask Admin com segurança e flexibilidade',
        'time': '09:10',
        'speaker': 'Thaíssa Falbo'
    },
    {
        'title': 'Escrevendo Testes com Flask e #JustPython',
        'time': '08:30',
        'speaker': 'Eduardo Mendes'
    },
    {
        'title': 'Inteligência Artificial, Flask e Raspberry Pi',
        'time': '11:00',
        'speaker': 'Eduardo Pereira'
    },
    {
        'title': 'API REST o começo: Introdução a REST para iniciantes',
        'time': '15:20',
        'speaker': 'Talita Rossari'
    },
    {
        'title': 'Flask Profiling: Técnicas para identificação de \
pontos críticos de performance',
        'time': '13:00',
        'speaker': 'Iuri de Silvio'
    },
    {
        'title': 'API REST em Flask + Vue.js: Aplicações modernas \
com separação entre frontend e backend',
        'time': '14:00',
        'speaker': 'João Lugão'
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
        title='Agenda',
        agenda=sorted(atividades, key=lambda k: k['time'])
    )


@bp.route('/cdc')
def cdc():
    return render_template(
        'main/cdc.html',
        title='Código de conduta'
    )
