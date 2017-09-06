# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
# Define the blueprint: 'nfe', set its url prefix: app.url/auth
nfe = Blueprint('nfe', __name__)

@nfe.route('/teste/', methods=['GET', 'POST'])
def teste():
	#return render_template('nfe/teste.html')
	return 'teste blueprint nfe'

@nfe.route('/senha/', methods=['GET', 'POST'])
def senha():
	#return render_template('nfe/teste.html')
	return render_template("/nfe/senha.html")



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
	if request.method == "POST":
		uf = request.form["uf"]
	# 'MunIBGE-UF'+dic[uf]+'.txt'

	dic = {'PR':'41','RR':'14','CE':'23','RS':'43','PI':'22','GO':'52','RO':'11','PE':'26','MT':'51','MG':'31','SC':'42','BA':'29','RJ':'33','AP':'16','SE':'28','AM':'13','MS':'50','SP':'35','DF':'53','PB':'25','AL':'27','RN':'24','MA':'21','PA':'15','TO':'17','AC':'12','ES':'32'}
	print(dic[uf])
	arquivo = os.path.dirname(pynfe.__file__)+'/data/MunIBGE/MunIBGE-UF'+dic[uf]+'.txt'
	with open(arquivo, 'r') as file:
		m = file.read()
	msg = {"value": m, "status":"OK"}
	return jsonify(resposta=msg)
