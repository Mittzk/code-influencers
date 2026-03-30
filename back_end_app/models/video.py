from models.utils import *

class Video:
    def __init__(self, title, description):
        self.title = title 
        self.description = description

    def __str__(self):
        return text_panel + f"Título: {self.title} | Descrição: {self.description}"
        
class ManagerVideo:

    def __init__(self):
        self.uploads = []
        self.description = []
        self.posts = []

    def view_uploads(self):
        print(header_panel + "\nFILA DE UPLOAD:")

        for i, upload in enumerate(self.uploads, start=1):
            print(text_panel + f"\nUPLOADS: " )
            print(text_panel + f"{i} - {upload}")

    def view_posts(self):
        print(header_panel + "\nLISTA DE VIDEOS:")

        for i, video in enumerate(self.posts, start=1):
            print(text_panel + f"\n{i} - VIDEOS: ")
            print(text_panel + f"- {video}")
        
    def upload_video(self):
        print(header_panel + "\nGESTÃO DE UPLOAD")

        while True:

            while True:

                name_up = str(input(text_panel + "\n-> Título upload: ")).strip()
                if name_up:
                    pass
                else:
                    print(error_color + "\nERRO. Título vazio.\n")

                dsc_up = str(input(text_panel + "-> Descrição: "))
                if dsc_up:
                    break
                else:
                    print(error_color + "\nERRO. Descrição vazia")

            self.description.append(dsc_up)

            remove_description = input(sent_text + "\nDeseja < enviar > essa descrição? [Sim/Não]: ").lower().strip()

            if remove_description in ["não","nao","n"]:
                self.description.pop()
                dsc_up = str(input(text_panel + "-> Descrição: "))
                self.description.append(dsc_up)

            elif remove_description in ["sim","s"]:
                pass
            else:
                print(error_color + "\nERRO. Digite uma resposta valida")
            
            finish_up = str(input(sent_text + "\nDeseja < encerrar > os uploads? [Sim/Não]: ")).lower()

            if finish_up in ["sim","s"]:
                self.uploads.append(Video(name_up, self.description[-1]))
                break

            elif finish_up in ["não","nao","n"]:
                self.uploads.append(Video(name_up, self.description[-1]))
            
            else:
                print(error_color + "\n > ERRO. Digite uma resposta valida. <")
                return finish_up
            
    def remove_upload(self):
        print(header_panel + "\nREMOVER UPLOAD:")
        print(text_panel + "\nEscolha o upload que deseja remover:")
        self.view_uploads()

        try:
            op_remove = int(input(sent_text + "\n:"))

            if 1 <= op_remove <= len(self.uploads):

                confirme = input(sent_text + "\nTem certeza que deseja excluir?  [Sim/Não]: ").lower()

                if confirme in ["sim","s"]:
                    self.uploads.pop(op_remove -1)
                    self.view_uploads()
                elif confirme in ["não","nao","n"]:
                    print(sent_text + "\nVoltando...")
                else:
                    print(error_color + "DIGITE UMA OPÇÃO VALIDA.")
            else:
                print(error_color + "\n > ERRO. NÚMERO INVALIDO. <")
        except ValueError as e:
            print(error_color + f"ERRO: {e}")

    def post_video(self):
        print(header_panel + "\n POSTAR VIDEOS:")

        print(text_panel + "\nEscolha um da fila para postar:")
        self.view_uploads()

        try:
            op_video = int(input(sent_text + "\n->:"))

            if 1 <= op_video <= len(self.uploads):
 
                enviar = self.uploads.pop(op_video -1)
                self.posts.append(enviar)
                print(sent_text + "\nVIDEO ENVIADO COM SUCESSO!")
            else:
                print(error_color + "\nERRO. Número invalido")

        except ValueError as e:
            print(error_color + f"ERRO: {e}")

mvd = ManagerVideo()

def upload_manager():
    while True:
        banner_upload()

        try:
            op = int(input(Fore.LIGHTMAGENTA_EX+ "\nOPÇÃO >> "))

            match(op):
                case 1:
                    mvd.upload_video()
                case 2:
                    mvd.view_uploads()
                case 3:
                    mvd.remove_upload()
                case 4:
                    mvd.post_video()
                case 5:
                    mvd.view_posts()
                case 0:
                    break
                case _:
                    print(error_color + "\nNÚMERO INVALIDO.")
        except ValueError as e:
            print(error_color + f"\nERRO: {e}")


