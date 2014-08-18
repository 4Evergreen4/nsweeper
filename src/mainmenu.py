import interface.window
import curses
import curses.panel
import game
import config

def mainmenu(stdscr, screen, screen_panel, edge, edge_panel):
    play = interface.window.newbutton(40, 16, 'play', 0)
    quit = interface.window.newbutton(40, 10, 'quit', 1)
    button_handler = interface.window.newbuttonhandler(0, play, quit)
    try:
        key_select = ord(config.getval('Keybindings', 'select'))
    except:
        key_select = 32
    key = 0

    done = False
    while not(done):
        stdscr.refresh()
        edge.border()
        edge_panel.bottom()
        edge.refresh()
        screen_panel.top()
        button_handler.update(key)
        play.display(screen, 20, 5)
        quit.display(screen, 20, 8)
        screen.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            done = True

        if quit.getstate() == True and key == key_select:
            return 'quit'
        if play.getstate() == True and key == key_select:
            return 'game'
