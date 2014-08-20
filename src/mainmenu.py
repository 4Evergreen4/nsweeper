import interface.window
import curses
import curses.panel
import game
import config

def mainmenu(stdscr, screen, screen_panel):
    play_button = interface.window.newbutton(40, 16, 'play', 0)
    quit_button = interface.window.newbutton(40, 10, 'quit', 1)
    button_handler = interface.window.newbuttonhandler(0, play_button, quit_button)
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
        play_button.display(screen, 20, 5)
        quit_button.display(screen, 20, 8)
        screen_panel.top()
        screen.border()
        screen.refresh()
        key = stdscr.getch()
