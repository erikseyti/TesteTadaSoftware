# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
# Define the blueprint: 'nfe', set its url prefix: app.url/auth
nfe = Blueprint('nfe', __name__)

@nfe.route('/teste/', methods=['GET', 'POST'])
def teste():
	#return render_template('nfe/teste.html')
	return 'teste blueprint nfe'

@nfe.route('/status/',methods=['GET', 'POST'])
def status():
	if request.method == 'POST':
		import pdb
		pdb.set_trace()
		print(request.form)
		return redirect(url_for('nfe.teste'))
	return render_template("/nfe/status.html")

# list codcidade
# os.listdir(os.path.dirname(pynfe.__file__)+'/data/MunIBGE')