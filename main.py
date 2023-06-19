import contatos

#Digite a mensagem a ser enviadas
mensagem = str(input('Digite sua mensagem: '))
caminho = str(input('Digite o caminho para postar o arquivo: '))

#Digite o nome do contato que deseja enviar a mensagem
#O nome deve ser idêntico ao que está salvo em sua agenda
p = contatos.meusContatos().copy()
contatos.msgAuto(p, mensagem, caminho)


