import curses #helping with styling of the terminal
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear() # Clearing the screen
    stdscr.addstr("Welcome to the speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!") # adding text in to the scrreen
    stdscr.refresh()
    stdscr.getkey()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # adding styling with foreground green and background white with an id 1
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)# Same shi with a second id
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    

wrapper(main)