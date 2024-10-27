# Intro to PyCurses

```
import curses

stdscr = curses.initscr()
                        
## Usually curses applications turn off automatic echoing of keys to the screen, in order to be able to read keys
## and only display them under certain circumstances. This requires calling the noecho() function.
curses.noecho()


## Applications will also commonly need to react to keys instantly, without requiring the Enter key to be pressed;
## this is called cbreak mode, as opposed to the usual buffered input mode
curses.cbreak()

## Terminals usually return special keys, such as the cursor keys or navigation keys such as Page Up and Home, as a multibyte escape sequence.
curses.keypad(True)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

## to reverse the curses-friendly terminal settings. Then call the endwin() function to restore the terminal to its original operating mode.
curses.endwin()
```

# Windows and Pads
\\\\\\\\\\\\\\\\\\\\\\\\
Windows are the basic abstraction in curses. A window object represents a rectangular area of the 
screen, and supports methods to display text, erase it, allow the user to input strings, and so forth.
----------------------------------------------------------------------------------------------------
The stdscr object returned by the initscr() function is a window object that covers the entire screen. 
Many programs may need only this single window, but you might wish to divide the screen into smaller windows, in order to redraw or clear them separately.
The newwin() function creates a new window of a given size, returning the new window object.

```
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
```
--------------------------------------------------------------------------------------
Note that the coordinate system used in curses is unusual. 
Coordinates are always passed in the order y,x, and the top-left corner of a window is coordinate (0,0). 
This breaks the normal convention for handling coordinates where the x coordinate comes first. 
This is an unfortunate difference from most other computer applications, but it’s been part of curses 
since it was first written, and it’s too late to change things now.
Your application can determine the size of the screen by using the `curses.LINES and curses.COLS` variables to obtain the `y` and `x` sizes. 
Legal coordinates will then extend from `(0,0)` to `(curses.LINES - 1, curses.COLS - 1)`.
--------------------------------------------------------------------------------------------------
When you call a method to display or erase text, the effect doesn’t immediately show up on the display. 
Instead you must call the `refresh()` method of window objects to update the screen.
This is because curses was originally written with slow 300-baud terminal connections in mind; with these terminals, minimizing the time required to redraw the screen was very important. 
Instead curses accumulates changes to the screen and displays them in the most efficient manner when you call refresh(). For example, 
if your program displays some text in a window and then clears the window, there’s no need to send the original text because they’re never visible.
--------------------------------------------------------------------------------------------------------------------------

In practice, explicitly telling curses to redraw a window doesn’t really complicate programming with curses much. 
Most programs go into a flurry of activity, and then pause waiting for a keypress or some other action on the part of the user. 
All you have to do is to be sure that the screen has been redrawn before pausing to wait for user input, by first calling stdscr.refresh() or the refresh() method of some other relevant window.




