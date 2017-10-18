from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def PrimeiraParte(canvas,doc):
    # auto generated elements
    texto = canvas.setFont('Helvetica',8,leading = None)
    texto = canvas.drawString(0.2*cm,29.5*cm,"_____________________________")
    texto = canvas.drawString(0.17*cm,29.25*cm,"|")
    #0.2571
    texto = canvas.drawString(0.17*cm,28.9929*cm,"|")
    texto = canvas.drawString(0.17*cm,28.7358*cm,"|")
    texto = canvas.drawString(0.17*cm,28.4787*cm,"|")
    texto = canvas.drawString(0.17*cm,28.2216*cm,"|")
    texto = canvas.drawString(0.17*cm,27.9645*cm,"|")
    texto = canvas.drawString(0.17*cm,27.7074*cm,"|")
    texto = canvas.drawString(0.17*cm,27.4503*cm,"|")
    texto = canvas.drawString(0.17*cm,27.1932*cm,"|")
    texto = canvas.drawString(0.17*cm,26.9361*cm,"|")
    texto = canvas.drawString(0.17*cm,26.6791*cm,"|")
    texto = canvas.drawString(0.2*cm,26.65*cm,"_____________________________")

    texto = canvas.drawString(4.73*cm,29.25*cm,"|")
    #0.2571
    texto = canvas.drawString(4.73*cm,28.9929*cm,"|")
    texto = canvas.drawString(4.73*cm,28.7358*cm,"|")
    texto = canvas.drawString(4.73*cm,28.4787*cm,"|")
    texto = canvas.drawString(4.73*cm,28.2216*cm,"|")
    texto = canvas.drawString(4.73*cm,27.9645*cm,"|")
    texto = canvas.drawString(4.73*cm,27.7074*cm,"|")
    texto = canvas.drawString(4.73*cm,27.4503*cm,"|")
    texto = canvas.drawString(4.73*cm,27.1932*cm,"|")
    texto = canvas.drawString(4.73*cm,26.9361*cm,"|")
    texto = canvas.drawString(4.73*cm,26.6791*cm,"|")

    numero_selo ="00000.00000.00000"
    controle_selo = "00000.00000"
    texto = canvas.setFont('Helvetica-Bold',10,leading = None)
    #trocar a fonte do texto
    texto = canvas.drawCentredString(2.45*cm,29.10*cm,"FUNARPEN")
    texto = canvas.setFont('Helvetica',10,leading = None)
    texto = canvas.drawCentredString(2.45*cm,28.70*cm,"SELO DIGITAL Nº")
    texto = canvas.setFont('Helvetica-Bold',10,leading = None)
    texto = canvas.drawCentredString(2.45*cm,28.30*cm,numero_selo)
    texto = canvas.setFont('Helvetica',10,leading = None)
    texto = canvas.drawCentredString(2.45*cm,27.90*cm,"Controle:")
    texto = canvas.setFont('Helvetica-Bold',10,leading = None)
    texto = canvas.drawCentredString(2.45*cm,27.50*cm,controle_selo)
    texto = canvas.setFont('Helvetica',10,leading = None)
    texto = canvas.drawCentredString(2.45*cm,27.10*cm,"Consulte esse selo em:")
    texto = canvas.setFont('Helvetica',10,leading = None)
    texto = canvas.drawCentredString(2.45*cm,26.685*cm,"http://funarpen.com.br")
    #link = c.linkURL("http://funarpen.com.br",(cm, cm, 2.45*cm, 26.685*cm), relative=1)

    #Segundo Relatorio
    nomeDoCartorio="Cartório Distrital do Taboão"
    endereco ="Rua Mateus Leme,Fone (xx) xxxx-xxxx - yyyy-yyyy / FAX: (zz) zzzz-zzzz, Cep: wwwww-www - Curitiba / PR"
    nomePessoaJuridica = "José Marcelo Lucas de Oliveira - Tabelião"
    cpfPessoaJuridica ="CPF Nº xxx.xxx.xxx-xx"



    #Bordas do Relatorio
    texto = canvas.setFont('Helvetica',20,leading = None)
    texto = canvas.drawString(0.5*cm,25.5*cm,"___________________________________________")
    #texto = c.setFont('Helvetica',16,leading = None)
    #texto = c.drawString(0.34*cm,25.0*cm,"(")
    texto = canvas.drawString(0.37*cm,24.88*cm,"|")
    texto = canvas.drawString(17.3*cm,24.88*cm,"|")
    #0.65
    texto = canvas.drawString(0.37*cm,24.23*cm,"|")
    texto = canvas.drawString(17.3*cm,24.23*cm,"|")
    texto = canvas.drawString(0.37*cm,23.58*cm,"|")
    texto = canvas.drawString(17.3*cm,23.58*cm,"|")
    texto = canvas.drawString(0.37*cm,22.93*cm,"|")
    texto = canvas.drawString(17.3*cm,22.93*cm,"|")
    texto = canvas.drawString(0.37*cm,22.28*cm,"|")
    texto = canvas.drawString(17.3*cm,22.28*cm,"|")
    texto = canvas.drawString(0.37*cm,21.63*cm,"|")
    texto = canvas.drawString(17.3*cm,21.63*cm,"|")
    texto = canvas.drawString(0.37*cm,20.98*cm,"|")
    texto = canvas.drawString(17.3*cm,20.98*cm,"|")


    texto = canvas.setFont('Helvetica-Bold',12,leading = None)
    texto = canvas.drawCentredString(8.8*cm,24.985*cm,nomeDoCartorio)
    texto = canvas.setFont('Helvetica',7,leading = None)
    texto = canvas.drawCentredString(8.8*cm,24.60*cm,endereco)
    texto = canvas.setFont('Helvetica-Bold',10,leading = None)
    texto = canvas.drawCentredString(8.8*cm,24.10*cm,nomePessoaJuridica)
    texto = canvas.setFont('Helvetica',7,leading = None)
    texto = canvas.drawCentredString(8.8*cm,23.80*cm,cpfPessoaJuridica)
    texto = canvas.setFont('Helvetica',10,leading = None)
    texto = canvas.drawString(0.5*cm,23.67*cm,"______________________________________________________________________________________")
    texto = canvas.setFont('Helvetica',5,leading = None)
    texto = canvas.drawString(0.5*cm,23.47*cm,"############################################################################################################################################################################")
    texto = canvas.drawString(0.5*cm,23.37*cm,"############################################################################################################################################################################")
    texto = canvas.setFont('Helvetica',10,leading = None)
    texto = canvas.drawString(0.5*cm,23.39*cm,"______________________________________________________________________________________")
    # Save
    canvas.showPage()
    canvas.save()

def Paragrafo():
    doc = SimpleDocTemplate("Relatorio Mensal.pdf",pagesize=A4)
    nomeFuncionario ="Paulo de Thomas Augusto Soares Machado da Silva de Oliveira Tavares São Fracisco"
    numeroRegistro="9884-1523"
    dataregistro ="20 de outubro de 2011"
    Story = []
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    paragracoTestamento = ("Reconheço por semelhança a assinatura de ") + (nomeFuncionario) + (" (")+ (numeroRegistro) + ("). Dou Fé. 74075F*.")
    paragracoTestamento = Paragraph(paragracoTestamento,style)
    Story.append(paragracoTestamento)
    doc.build(Story, PrimeiraParte)

if __name__ == "__main__":
    Paragrafo()
