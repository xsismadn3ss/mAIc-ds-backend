import colorama
import pyfiglet


def hello():
    title = pyfiglet.figlet_format("CHARTS API")
    description = 'Microservicio de gráfica con IA'

    print(f'{colorama.Fore.GREEN}{title:}')
    print(f'{colorama.Fore.CYAN}{" ":>10}{description}{colorama.Style.RESET_ALL}\n\n')