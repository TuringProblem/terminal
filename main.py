from curses import wrapper

def main(stdscr):
    ## Clear the Screen
    stdscr.clear()

    ## This raises ZeroDivisionError when i == 10.
    for i in range (0, 11):
        v = i - 10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()
wrapper(main)

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)


