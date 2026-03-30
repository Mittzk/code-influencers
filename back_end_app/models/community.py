from models.utils import *


class Followers:
    def __init__(self):
        self.followers = []

    def view_followers(self):
        print(header_panel + "\nSEGUIDORES:")

        for i, follow in enumerate(self.followers, start=1):
            print(text_panel + f"\n{i} - {follow}")

    def add_follow(self):
        print(header_panel + "\n-> Adicione seguidor")

        while True:

            new_follow = input(sent_text + "@Usuario: ").strip()
            if new_follow:
                break
            else:
                print(error_color + "\nERRO. Usuario vazio.\n")

        self.followers.append(f"@{new_follow}")

        print(follow_list_color + f"\nLista atualizada: {self.followers}")

    def add_vip(self):
        print(header_panel + "\n-> Área vip")

        while True:
            vip_follow = input(vip_follow_color + "@usuario vip: ").strip()
            if vip_follow:
                break
            else:
                print(error_color + "\nERRO. Usuario vazio.\n")

        self.followers.insert(0, f"@{vip_follow}")

        print(follow_list_color + f"\nLista atualizada: {self.followers}")

    def remove_follow(self):
        print(header_panel + "\n-> Remover seguidor")

        while True:
            print(text_panel + f"\n[ 1 ] REMOVER SEGUIDOR")
            print(text_panel + f"[ 0 ] VOLTAR")

            
            op = int(input(sent_text + "\nOPÇÃO >> "))

            try:
                match (op):

                    case 1:
                        remove = (input(sent_text + "\nDigite o user que deseja remover : ")).strip()
                        if not remove:
                            print(error_color + "\nERRO. Usuario vazio.\n")
                            continue

                        if f"@{remove}" in self.followers:
                            self.followers.remove(f"@{remove}")
                            print(post_color + f"\nSeguidor Removido com sucesso!")
                        else:
                            print(error_color + "\nERRO. Usuário não encontrado.\n")

                        print(follow_list_color + f"\nLista atualizada: {self.followers}")
                    case 0:
                        break
                    case _:
                        print(error_color + "\nNUMERO INVALIDO.")
            except ValueError as e:
                print(error_color + f"\nERRO: {e}")


fl = Followers()


def community_manager():
    while True:
        banner_community()

        try:
            op = int(input(Fore.LIGHTMAGENTA_EX + "\nOPÇÃO >> "))

            match(op):
                case 1:
                    fl.add_follow()
                case 2:
                    fl.add_vip()
                case 3:
                    fl.remove_follow()
                case 4:
                    fl.view_followers()
                case 0:
                    break
                case _:
                    print(error_color + "\nNÚMERO INVALIDO.")
        except ValueError as e:
            print(error_color + f"\nERRO: {e}")
