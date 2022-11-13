import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (800, 600))


def set_fullscreen(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    global user_name
    print(f'{user_name.get_value()}, Do the job here!')


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Concentrate or die!',
    width=400
)

# user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
menu.add.button('Jogar', start_the_game)
menu.add.button('Estatísticas', start_the_game)
menu.add.toggle_switch('Tela inteira', False, toggleswitch_id='first_switch')
# menu.add.toggle_switch('Tela inteira: ', [('Ativado', True), ('Inativado', False)], onchange=set_fullscreen)
menu.add.button('Sair', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)