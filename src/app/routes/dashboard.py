from os import getenv

from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def index():
    menus = {
        "Calc - Area de Plantio": '/fase1'
    }

    return render_template("pages/dashboard.html", menus=menus)

@dashboard_bp.route('/fase-1')
def phase_one():
    cultures = ['milho', 'laranja']
    products = {'milho': 'Fosfato Monoamônico', 'laranja': 'Diclorofenoxiacético'}
    productsQtd = {'Fosfato Monoamônico': 5, 'Diclorofenoxiacético': 0.15}
    formats = {'milho': 'retangulo', 'laranja': 'triangulo'}
    streets = {'milho': 1, 'laranja': 2}
    spaceBetweenStreets = 1

    return render_template(
        "pages/calc-area.html",
        sub_title="Cálculo de area de plantio",
        cultures=cultures,
        products=products,
        productsQtd=productsQtd,
        formats=formats,
        streets=streets,
        spaceBetweenStreets=spaceBetweenStreets,
    )