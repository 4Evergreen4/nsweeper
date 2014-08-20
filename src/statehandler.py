import game
from mainmenu import mainmenu
from game import game

def statehandler(stdscr, screen, screen_panel, edge,
                 edge_panel, field_h, field_w, mine_num):
    done = False
    nextstate = 'menu'
    while not(done == True):
        if nextstate == 'game':
            nextstate = game(stdscr, screen, screen_panel, edge,
                             edge_panel, field_h, field_w, mine_num)
        if nextstate == 'quit':
            return
        if nextstate == 'menu':
            nextstate = mainmenu(stdscr, screen, screen_panel,
                                 edge, edge_panel)
