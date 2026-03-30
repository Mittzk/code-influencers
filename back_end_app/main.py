import models.community 
import models.video 
from models.utils import *

while True:
    banner_main()

    try:

        option = int(input(Fore.LIGHTMAGENTA_EX+ "\nOpção >> "))

        match(option):

            case 1:
                models.video.upload_manager()
            case 2:
                models.community.community_manager()
            case 0:
                break
            case _:
                print("\nNÚMERO INVALIDO.")

    except ValueError as e:
        print(f"ERRO. {e}")
