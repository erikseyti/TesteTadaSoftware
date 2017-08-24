# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
# Define the blueprint: 'nfe', set its url prefix: app.url/auth
nfe = Blueprint('nfe', __name__)

@nfe.route('/teste/', methods=['GET', 'POST'])
def teste():
	#return render_template('nfe/teste.html')
	return 'teste blueprint nfe'

@nfe.route('/cidade/',methods=['GET','POST'])
def cidade():
	if request.method == 'POST':
		cidade = request.form["cidade"].strip()
		uf = request.form["uf"]
		return render_template("/nfe/cidade.html", resposta=cidade)
	return render_template("/nfe/cidade.html")

@nfe.route('/status/',methods=['GET', 'POST'])
def status():
	if request.method == 'POST':
		from pynfe.processamento.comunicacao import ComunicacaoSefaz
		certificado = request.form["certificado"]
		senha = request.form["senha"]
		uf = request.form["uf"]
		homologacao = bool(request.form["homologacao"])
		tipo = request.form["tipo"]

		# import pdb
		# pdb.set_trace()

		con = ComunicacaoSefaz(uf, certificado, senha, homologacao)
		xml = con.status_servico(tipo)     # nfe ou nfce
		print (xml.text)
		
		return render_template("/nfe/status.html", resposta = xml.text)
	return render_template("/nfe/status.html")
# list codcidade
# os.listdir(os.path.dirname(pynfe.__file__)+'/data/MunIBGE')

@nfe.route('/_cod_ibge/', methods=['POST'])
def _cod_ibge():
	m = 'teste'
	msg = {"value": m, "status":"OK"}
	return jsonify(resposta=msg)