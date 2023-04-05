import time
import curses


def draw(canvas):
    rows, columns = 3, 20
    canvas.addstr(rows, columns, "Hello world!", curses.A_REVERSE)
    canvas.border()
    canvas.refresh()
    time.sleep(1)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)


