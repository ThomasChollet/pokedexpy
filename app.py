from flask import Flask, url_for, redirect, render_template
from flask_assets import Environment, Bundle
from flask import request
import requests as req
import json
# import os

app = Flask(__name__, instance_relative_config=False)
app.static_folder = "static"

assets = Environment(app)

@app.route('/')
def home():
    pokemonReponse = req.request(method="GET", url="https://pokeapi.co/api/v2/pokemon/")
    pokemonReponse_json = pokemonReponse.json()
    #return pokemonReponse_json
    return render_template('index.html', Pokemons = pokemonReponse_json['results'])

@app.route('/search', methods = ['POST'])
def search():
    search = request.json['search']
    pokemonReponse = req.request(method="GET", url="https://poki-dex.herokuapp.com/pokemons/search?name=" + search + "&page=1&pageSize=20")
    pokemonReponse_json = pokemonReponse.json()
    return render_template('searchList.html', Pokemons = pokemonReponse_json['pokemons'])

@app.route('/pokemon/<name>', methods = ['GET'])
def pokemon(name):
    pokemonReponse = req.request(method="GET", url=" https://pokeapi.co/api/v2/pokemon/" + name)
    pokemonReponse_json = pokemonReponse.json()
    return render_template('pokemon.html', Pokemon = pokemonReponse_json)