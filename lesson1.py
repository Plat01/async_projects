import asyncio
import curses

import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    rows, columns = 3, 20
    coroutine = blink(canvas=canvas, row=rows, column=columns)
    i = 0
    while True:
        if i == 0:
            coroutine.send(None)
            time.sleep(.02)
        elif i == 1:
            coroutine.send(None)
            time.sleep(0.03)
        elif i == 2:
            coroutine.send(None)
            time.sleep(0.05)
        else:
            coroutine.send(None)
            time.sleep(0.03)
        i = (i + 1) % 4
        rows = (rows + 1) % 7
        canvas.refresh()


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
    # print(type(blink(draw, 3, 3, ";")), dir(blink(draw, 3, 3, ";")))


