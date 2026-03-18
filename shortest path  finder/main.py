import curses# a module where there are libararies where you can do many things like bold the text and give a blank screeen and colors to the background tooo

from curses import wrapper 
import queue
import time#time module




maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze,stdscr,path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)








def main(stdcr):
    curses.init_pair(1, curses.COLOR_CYAN,curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_CYAN,curses.COLOR_RED)

    # cyan_and_red = curses.color_pair(1)
    # stdcr.clear()
    # stdcr.addstr(0,0,"hello world",cyan_and_red  )
    # stdcr.refresh
    # stdcr.getch()
    
wrapper(main)

