#coding:utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#server = smtplib.SMTP_SSL('localhost', 25)
#server.login('giorgyismael@gmail.com', 'vai220607')

def emailAtivacaoCadastro(nomeUsuario, emailUsuario, assunto, chaveAtivacao, dominio):
        server = smtplib.SMTP()
        server.connect('localhost')
        me = "no-reply@sisca.fabricadesoftware.ifc.edu.br"
        you = "{}".format(emailUsuario)
        subject = assunto

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = you

        html = """
                    <h2><b>Ola  {}.</b></h2>
                    <h3>Seja Bem Vindo ao <strong>SisCA</strong> - Sistema de Controle de Acesso</h3>
                    <p>Para Confirmar Seu cadastro, Clique no Link Abaixo<br>
                        <a href="http://{}/automaticport/ativacadastro/{}">Ativar Cadastro</a>
                    </p>

                    <p>Atenciosamente,
                    <br>
                    Equipe de Suporte<br>
                    giorgyismael@gmail.com<br>
                    +55 (47)84390048 | (47) 84390048</p>
                    """.format(nomeUsuario.split(" ")[0], dominio, chaveAtivacao)

        txt = MIMEText(html, 'html')
        msg.attach(txt)
        server.sendmail(me, you, msg.as_string())
        server.quit()

def emailRecuperarSenha(nomeUsuario, emailUsuario, assunto, chaveAtivacao, dominio):
        server = smtplib.SMTP()
        server.connect('localhost')
        me = "no-reply@sisca.fabricadesoftware.ifc.edu.br"
        you = "{}".format(emailUsuario)
        subject = assunto

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = you

        html = """
                    <h2><b>Ola  {}.</b></h2>
                    <p>Para redefinir sua senha, clique no link abaixo<br>
                        <a href="http://{}/automaticport/recuperarsenhachave/{}">Redefinir Senha</a>
                    </p>

                    <p>Atenciosamente,
                    <br>
                    Equipe de Suporte<br>
                    giorgyismael@gmail.com<br>
                    +55 (47)84390048 | (47) 84390048</p>
                    """.format(nomeUsuario.split(" ")[0], dominio,chaveAtivacao)

        txt = MIMEText(html, 'html')
        msg.attach(txt)
        #server = smtplib.SMTP('localhost')
        server.sendmail(me, you, msg.as_string())
        server.quit()


def emailFaleConosco(nomeUsuario, emailUsuario, assunto, descricao):
        server = smtplib.SMTP()
        server.connect('localhost')
        me = "no-reply@sisca.fabricadesoftware.ifc.edu.br"
        you = "{}".format(emailUsuario)
        subject = assunto

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = you

        html = """
                    <h2><b>Olá. </b></h2>
                    <p>Comunicamos o recebimento do fale conosco abaixo, pedimos a gentileza que aguarde contato.</p>
                    <p>Nome:{}<br>
                    Email:{}<br>
                    Descrição:{}</p>

                    <p>Atenciosamente,
                    <br>
                    Equipe de Suporte<br>
                    giorgyismael@gmail.com<br>
                    +55 (47)84390048 | (47) 84390048</p>
                    """.format(nomeUsuario,emailUsuario,descricao)

        txt = MIMEText(html, 'html')
        msg.attach(txt)
        #s = smtplib.SMTP('localhost','587')
        #s.starttls()
        server.sendmail(me, you, msg.as_string())
        server.quit()

#print('enviando')
#emailFaleConosco('gaf', 'giorgyismael@gmail.com', 'qweqwe', 'qweqe')
#print('foi')
