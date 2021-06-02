import requests
import json
import os

class TelegramBot:
    def __init__(self):
        token = '1825758163:AAG3EcPA2fqReedUsOdUyuzB11l8wr_nUMc'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    print(dado)
                    try:
                      update_id = dado['update_id']
                      mensagem = str(dado["message"]["text"])
                      usuario = dado["message"]["from"]["first_name"]
                      chat_id = dado["message"]["from"]["id"]
                      eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                      resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem, usuario)
                      self.responder(resposta, chat_id)
                    except Exception:
                      self.responder("Encontrei um problema", 1825361005)
    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    def criar_resposta(self, mensagem, eh_primeira_mensagem, usuario):
        if eh_primeira_mensagem == True or mensagem in ('OI', 'OLÁ', 'OLA', 'oi', 'Oi', 'ola', 'olá', 'Ola', 'Olá', 'Bom dia', 'bom dia', 'boa tarde', 'boa noite', 'Boa noite', 'Boa tarde', '/start'):
          return f'''Olá {usuario}, seja bem vindo(a)! :){os.linesep}Selecione uma das opções para que eu possa te ajudar:{os.linesep}1 - Agendar{os.linesep}2 - Remarcar{os.linesep}3 - Cancelar'''

        elif mensagem == '1' or mensagem in ('AGENDAR', 'Agendar', 'agendar'):
          return f'''Qual o tipo de agendamento deseja fazer?{os.linesep}4 - Retorno{os.linesep}5 - Acompanhamento{os.linesep}6 - Exame{os.linesep}7 - Cirurgia'''
          
        elif mensagem == '2' or mensagem in ('REMARCAR', 'Remarcar', 'remarcar', 'Sim', 'sim'):
          return f'''Tudo bem, vamos lá, me passe o código da sua consulta para eu busca-lá aqui e te dar os horários disponíveis para remarcarmos...{os.linesep}'''

        elif mensagem == '3' or mensagem in ('CANCELAR', 'Cancelar', 'cancelar'):
          return f'''Que pena, certeza que invés de cancelar não conseguimos remarcar?{os.linesep}Vamos remarcar? Sim ou não?'''
        
        elif mensagem == '4' or mensagem in ('RETORNO', 'Retorno', 'retorno'):
          return f'''Temos esses horários disponíveis, qual fica melhor para você?{os.linesep}8 - 01/07/21 às 14:00 horas{os.linesep}9 - 01/07/21 às 15:00 horas{os.linesep}10 - 04/07/21 às 09:00 horas{os.linesep}11 - 05/07/21 às 16:00 horas'''

        elif mensagem == '5' or mensagem in ('ACOMPANHAMENTO', 'Acompanhamento', 'acompanhamento'):
          return f'''Temos esses horários disponíveis, qual fica melhor para você?{os.linesep}8 - 01/07/21 às 14:00 horas{os.linesep}9 - 01/07/21 às 15:00 horas{os.linesep}10 - 04/07/21 às 09:00 horas{os.linesep}11 - 05/07/21 às 16:00 horas'''

        elif mensagem == '6' or mensagem in ('EXAME', 'Exame', 'exame'):
          return f'''Temos esses horários disponíveis, qual fica melhor para você?{os.linesep}8 - 01/07/21 às 14:00 horas{os.linesep}9 - 01/07/21 às 15:00 horas{os.linesep}10 - 04/07/21 às 09:00 horas{os.linesep}11 - 05/07/21 às 16:00 horas'''

        elif mensagem == '7' or mensagem in ('CIRURGIA', 'Cirurgia', 'cirurgia'):
          return f'''Temos esses horários disponíveis, qual fica melhor para você?{os.linesep}8 - 01/07/21 às 14:00 horas{os.linesep}9 - 01/07/21 às 15:00 horas{os.linesep}10 - 04/07/21 às 09:00 horas{os.linesep}11 - 05/07/21 às 16:00 horas'''

        elif mensagem in ('ACO', 'RET', 'EXA', 'CIR'):
          return f'''Temos esses horários disponíveis, qual fica melhor para você?{os.linesep}8 - 01/07/21 às 14:00 horas{os.linesep}9 - 01/07/21 às 15:00 horas{os.linesep}10 - 04/07/21 às 09:00 horas{os.linesep}11 - 05/07/21 às 16:00 horas{os.linesep}Digite o número do horário que deseja...'''

        elif mensagem == '8':
          return f'''Certo, deseja confirmar sua vinda no dia 01/07/21 às 14:00 horas?'''

        elif mensagem == '9':
          return f'''Certo, deseja confirmar sua vinda no dia 01/07/21 às 15:00 horas?'''

        elif mensagem == '10':
          return f'''Certo, deseja confirmar sua vinda no dia 04/07/21 às 09:00 horas?'''

        elif mensagem == '11':
          return f'''Certo, deseja confirmar sua vinda no dia 05/07/21 às 16:00 horas?'''

        elif mensagem in ('CONFIRMAR', 'Confirmar', 'confirmar'):
          return f'''Horário confirmado {usuario}, obrigado(a) pela preferência, estamos te aguardando no dia e horário escolhidos.{os.linesep}Qualquer coisa estou sempre aqui, é só me chamar.'''

        elif mensagem in ('CANCELAR', 'cancelar', 'Não', 'não', 'nao'):
          return f'''Que pena que vamos mesmo cancelar {usuario}, mas tudo bem, se precisar de outra coisa, estou sempre aqui, é só me chamar.{os.linesep}Até mais e obrigado pelo contato.'''

        elif mensagem in ('Obrigado', 'obrigado', 'Obrigada', 'obrigada'):
          return f'''Obrigado(a) você {usuario}, espero ter ajudado, sempre que precisar estou a posição. Até mais.'''
        
        else:
          return f'''Desculpa {usuario}, não entendi oque você disse, se já estavámos conversando, verifique se não errou nada na última mensagem em relação a nossa conversa, se foi isso, sem problemas é só responder de novo.{os.linesep}Caso seja a primeira mensagem me diga um Oi ou Olá que tudo fica mais fácil...'''
          
    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)

bot = TelegramBot()
bot.Iniciar()