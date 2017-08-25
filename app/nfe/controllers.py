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
	import os
	import pynfe
	cd = "50"
	if request.method == "POST":
		uf = request.form["uf"]
		if uf == "RR":
			cd = "14"
		elif uf == "PR":
			cd = "41"
		elif uf == "CE":
			cd = "23"
		elif uf == "RS":
			cd = "43"
		elif uf == "PI":		
			cd = "22"
		elif uf == "GO":
			cd = "52"
		elif uf == "RO":
			cd = "11"
		elif uf == "PE":
			cd = "26"
		elif uf == "MT":
			cd = "51"
		elif uf == "MG":
			cd = "31"
		elif uf == "SC":
			cd = "42"
		elif uf == "BA":
			cd = "29"
		elif uf == "RJ":
			cd = "33"
		elif uf == "AP":
			cd = "16"
		elif uf == "SE":
			cd = "28"
		elif uf == "AM":
			cd = "13"
		elif uf == "MS":
			cd = "50"
		elif uf == "SP":
			cd = "35"
		elif uf == "DF":
			cd = "53"
		elif uf == "PB":
			cd = "25"
		elif uf == "AL":
			cd = "27"
		elif uf == "RN":
			cd = "24"
		elif uf == 	"MA":
			cd = "21"	
		elif uf == "PA":
			cd = "15"
		elif uf == "TO":
			cd = "17"
		elif uf ==  "AC":
			cd = "12"
		elif uf == "ES":
			cd = "32"


	print(uf)
	print(cd)
	# 'MunIBGE-UF'+dic[uf]+'.txt'

	dic = {uf:cd}
	arquivo = os.path.dirname(pynfe.__file__)+'/data/MunIBGE/MunIBGE-UF'+dic[uf]+'.txt'
	with open(arquivo, 'r') as file:
		m = file.read()
	msg = {"value": m, "status":"OK"}
	return jsonify(resposta=msg)