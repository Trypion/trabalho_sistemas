import PySimpleGUI as sg
import hashlib
from database import connection

db = connection.DatabaseConnection()  # criando uma conexao com a database


def main():    
    def HashGeneratorGUI():
        '''
          Janela de hash generator
          ma janela para criar um hash de um password para fins de desenvolvimento
        '''
        layout = [
            [sg.Text('Password Hash Generator', size=(30, 1), font='Any 15')],
            [sg.Text('Password'), sg.Input(key='-password-')],
            [sg.Text('SHA Hash'), sg.Input('', size=(40, 1), key='hash')],
        ]

        window = sg.Window('SHA Generator', layout,
                           auto_size_text=False,
                           default_element_size=(10, 1),
                           text_justification='r',
                           return_keyboard_events=True,
                           grab_anywhere=False)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            password = values['-password-']
            try:
                password_utf = password.encode('utf-8')
                sha1hash = hashlib.sha1()
                sha1hash.update(password_utf)
                password_hash = sha1hash.hexdigest()
                window['hash'].update(password_hash)
            except:
                pass
        window.close()

    def PasswordMatches(password, login):
        '''
          Faz a procura do usuario pelo login no banco de dados,
          depois verifica se a hash do password no banco de dados 
          bate com a hash do password fornecido pelo usuario
        '''
        # PROCRA O USUARIO NA DATABASE VIA LOGIN
        user = db.findUserByLogin(login)

        if user is None:
            return False

        password_utf = password.encode('utf-8')
        sha1hash = hashlib.sha1()
        sha1hash.update(password_utf)
        password_hash = sha1hash.hexdigest()
        return password_hash == user['password']

    def LoginGUI():
        '''
        Janela de login
        recupera o login e senha digitados pelo usuario
        verifica em database se o login existe e se a senha esta correta

        se o login for 'gui' abre uma janela para gerar hash para facilitar
        a criação de registros falsos na database
        '''
        layout = [
            [sg.Text('Login'), sg.Input('', size=(40, 1), key='login')],
            [sg.Text('Password'), sg.Input('', size=(40, 1), key='password')],
            [sg.Button('Ok'), sg.Button('Cancel')],
        ]

        window = sg.Window('LoginGUI', layout,
                           auto_size_text=False,
                           default_element_size=(10, 1),
                           text_justification='r',
                           return_keyboard_events=True,
                           grab_anywhere=False)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            if event == 'Ok':
                login = values['login']
                password = values['password']
                if login == "gui":
                    HashGeneratorGUI()
                    return

                if PasswordMatches(password, login):
                    # TODO
                    # ADICIONE O CODIGO DA PROXIMA JANELA AQUI
                    sg.popup('Login Successful')
                    window.close()
                    break
                else:
                    sg.popup('Login Failed')

        window.close()

    LoginGUI()


if __name__ == '__main__':
    sg.theme('DarkAmber')
    main()
