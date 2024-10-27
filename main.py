import curses
def main(stdscr):
    # Clears the screen 
    stdscr.clear();

    ## Adding Hello, world to the screen
    stdscr.addstr(5, 10, "Hello, World");

    stdscr.refresh();
    ## Waits for the user input
    stdscr.getch();

curses.wrapper(main)
