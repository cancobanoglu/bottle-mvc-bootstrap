# -*- coding: utf-8 -*-
from project import app
from bottle import view


@app.route('/', method='GET')
@view('index')
def index():
    return {}
