#coding:utf-8

class MessengerError:
    def Password(self,errorIdentification=None):
        if errorIdentification == 0:
            return u"A senha deve ter no minino 8 caracteres."

        elif errorIdentification == 1:
            return u"A senha deve ter numeros e letras"

        else:
            return u"Ops, Ocorreu algum erro."

    def Email(self, errorIdentification=None):
        if errorIdentification == 0:
            return u"Email já encontra-se cadastrado"

        else:
            return u"Ops, Ocorreu algum erro."

    def Usuario(self, errorIdentification=None):
        if errorIdentification == 0:
            return u"Usuario inativo."

        elif errorIdentification == 1:
            return u"Usuario ou senha incorretos"

        elif errorIdentification == 2:
            return u"Ops! Parece que não encontramos usuário!"

        elif errorIdentification == 3:
            return u"Ops! Parece este que este Ambiente não está Autorizado!"

        elif errorIdentification == 4:
            return u"Nenhum ambiente cadastrado!"

        elif errorIdentification == 5:
            return u"Erro dde conexão. Verifique a rede e tente novamente."

        elif errorIdentification == 6:
            return u'cadastro não encontrado, ou existe mais de um Cadastro com mesmo RFID'

        elif errorIdentification == 7:
            return u'Codigo RFID nao informado'

        else:
            return u"Ops, Ocorreu algum erro."

    def Cadastro(self, errorIdentification=None):
        if errorIdentification == 0:
            return u'Chave já foi utilizada!'

        elif errorIdentification == 1:
            return u'Chave não associada a nenhum Cadastro!'

        elif errorIdentification == 2:
            return u'Nenhuma chave informada!'

        elif errorIdentification == 3:
            return u'Cadastro já encontra-se Ativo!'

        elif errorIdentification == 4:
            return u'Cadastro não encontrado, informe e-mail válido!'

        else:
            return u"Ops, Ocorreu algum erro."

class MessengerSucess:

    def FaleConosco(self,sucessIdentification=None):
        if sucessIdentification == 0:
            return u'E-mail enviado para Equipe de Suporte!'

    def Cadastro(self,sucessIdentification=None):
        if sucessIdentification == 0:
            return u'Cadastro Realizado com Sucesso! Verifique seu email para ativá-lo.'

        elif sucessIdentification == 1:
            return u'Cadastro ativado!'
        else:
            return u"Algo deu certo, entretanto não identifiquei código!."

    def Email(self, sucessIdentification=None, extra=None):
        if sucessIdentification == 0:
            return u'E-mail de ativação enviado para {}.'.format(extra)


    def Usuario(self, sucessIdentification=None):
        if sucessIdentification == 0:
            return u'Informações Atualizadas!'
        elif sucessIdentification == 1:
            return u'Solicitação enviada. Aguarde, pois a porta será aberta!'

        elif sucessIdentification == 2:
            return u'Acesso autorizado!'

        elif sucessIdentification == 3:
            return u'Sessão Finalizada!'

        else:
            return u"Ops, Não seo qual mensagem Informar."