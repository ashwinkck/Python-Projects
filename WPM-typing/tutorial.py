import curses #helping with styling of the terminal
from curses import wrapper

def main(stdscr):
    stdscr.clear() # Clearing the screen
    stdscr.addstr("Hello World!") # adding text in to the scrreen
    stdscr.refresh()# Refreshing the screen
    stdscr.getkey() # The covering in which of the o/p when we are putting the values

wrapper(main)