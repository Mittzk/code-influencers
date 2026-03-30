from pyfiglet import figlet_format
from colorama import Fore, Style, init

init(autoreset=True)

def banner_main():
    print(Fore.LIGHTMAGENTA_EX + figlet_format("I N F L U E N C E R S", font="smslant"))
    print(Fore.LIGHTMAGENTA_EX + "-" * 30)
    print(Fore.LIGHTCYAN_EX + "APP INFLUENCERS".center(30))
    print(Fore.LIGHTMAGENTA_EX + "-" * 30)

    print(Fore.LIGHTCYAN_EX + "[ 1 ] Gerenciamento de videos")
    print(Fore.LIGHTCYAN_EX + "[ 2 ] Comunidade")
    print(Fore.LIGHTCYAN_EX + "[ 0 ] Sair")

def banner_upload():
    print(Fore.LIGHTMAGENTA_EX + "\n>> GESTÃO DE UPLOADS")
    print(Fore.LIGHTCYAN_EX + "\n[ 1 ] ADICIONAR UPLOAD")
    print(Fore.LIGHTCYAN_EX + "[ 2 ] FILA DE UPLOAD")
    print(Fore.LIGHTCYAN_EX + "[ 3 ] REMOVER UPLOAD")
    print(Fore.LIGHTCYAN_EX + "[ 4 ] POSTAR UPLOAD")
    print(Fore.LIGHTCYAN_EX + "[ 5 ] VER VIDEOS POSTADOS")
    print(Fore.LIGHTCYAN_EX + "[ 0 ] VOLTAR")

def banner_community():
    print(Fore.LIGHTMAGENTA_EX + "\nGESTÃO DE COMUNIDADE")
    print(Fore.LIGHTCYAN_EX + "\n[ 1 ] ADICIONAR SEGUIDOR")
    print(Fore.LIGHTCYAN_EX + "[ 2 ] ADICIONAR VIP")
    print(Fore.LIGHTCYAN_EX + "[ 3 ] REMOVER SEGUIDOR")
    print(Fore.LIGHTCYAN_EX + "[ 4 ] VER SEGUIDORES")
    print(Fore.LIGHTCYAN_EX + "[ 0 ] VOLTAR")

# =====================================================================

error_color = Fore.LIGHTRED_EX 

header_panel = Fore.LIGHTMAGENTA_EX

text_panel = Fore.LIGHTCYAN_EX

sent_text = Fore.LIGHTGREEN_EX

post_color = Fore.LIGHTBLUE_EX

normal_follow_color = Fore.LIGHTWHITE_EX

vip_follow_color = Fore.YELLOW

follow_list_color = Fore.BLUE
    
