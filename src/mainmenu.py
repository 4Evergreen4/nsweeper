import interface
import curses
import curses.panel
import game
import config

logo = [
" __    _  _______  _     _  _______  _______  _______  _______  ______",
"|  |  | ||       || | _ | ||       ||       ||       ||       ||    _ |",
"|   |_| ||  _____|| || || ||    ___||    ___||    _  ||    ___||   | ||",
"|       || |_____ |       ||   |___ |   |___ |   |_| ||   |___ |   |_||_",
"|  _    ||_____  ||       ||    ___||    ___||    ___||    ___||    __  |",
"| | |   | _____| ||   _   ||   |___ |   |___ |   |    |   |___ |   |  | |",
"|_|  |__||_______||__| |__||_______||_______||___|    |_______||___|  |_|"
]

def mainmenu(stdscr, screen, screen_panel):
    play_button = interface.newbutton(40, 16, 'play', 0)
    quit_button = interface.newbutton(40, 10, 'quit', 1)
    button_handler = interface.newbuttonhandler(0, play_button, quit_button)
    try:
        key_select = ord(config.getval('select', 'Keybindings'))
    except:
        key_select = ord(' ')

    key = 0
    play_button.setstate(True)
    quit_button.setstate(False)
    button_handler.update(key)

    done = False
    while not(done):
        if key == ord('q'):
            return 'quit'

        if quit_button.getstate() == True and key == key_select:
            return 'quit'
        if play_button.getstate() == True and key == key_select:
            return 'game'

        stdscr.refresh()
        button_handler.update(key)
        play_button.display(screen, 35, 9)
        quit_button.display(screen, 35, 12)
        drawlogo(screen, 1, 3)
        screen_panel.top()
        screen.border()
        screen.refresh()
        key = stdscr.getch()

def drawlogo(screen, y, x):
    for i in range(0, len(logo)):
        screen.addstr(y + i, x, str(logo[i]))
