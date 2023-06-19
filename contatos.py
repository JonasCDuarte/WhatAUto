def meusContatos():
    con = []
    while True:
        con.append(str(input('Nome do contato: ')))
        resp = str(input(('Deseja adicionar mais um contato? [S/N]'))).upper()
        if resp[0] == 'S' or 'N':
            if resp[0] == 'S':
                print('Adicionado com sucesso!')
                print('Vamos continuar...')
            else:
                break
        else:
            print('Valor informado não é válido...')
            print('Tente novamente...')
    return con

def msgAuto(ass,mensagem,caminho):
    from time import sleep
    import pyautogui
    pyautogui.hotkey('Win')
    sleep(0.5)
    pyautogui.write('google', 0.4)
    pyautogui.hotkey('enter')
    sleep(2)
    pyautogui.write('https://web.whatsapp.com/')
    sleep(4)
    pyautogui.hotkey('enter')
    sleep(8)
    for v, c in enumerate(ass):
        sleep(5)
        pyautogui.click(x=324, y=128)
        sleep(5)
        pyautogui.write(c)
        sleep(5)
        pyautogui.hotkey('enter')
        sleep(2)
        pyautogui.write(mensagem)
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(3)
        pyautogui.hotkey('Win')
        sleep(1)
        pyautogui.write(caminho)
        sleep(2)
        pyautogui.hotkey('enter')
        sleep(3)
        pyautogui.hotkey('ctrl', 'c')
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(2)
        pyautogui.hotkey('Esc')

    sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    print('Fim de programa ')


