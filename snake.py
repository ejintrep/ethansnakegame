import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
#Width=120 Height=40


def menu(men):
    men.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    men.nodelay(1)
    selection = -1
    option = 0

    snk1 = "   ,-,--.  .-._         ,---.      ,--.-.,-.      ,----.  "
    snk2 = " ,-.'-  _\/==/ \  .-._.--.'  \    /==/- |\  \  ,-.--` , \ "
    snk3 = "/==/_ ,_.'|==|, \/ /, |==\-/\ \   |==|_ `/_ / |==|-  _.-` "
    snk4 = "\==\  \   |==|-  \|  |/==/-|_\ |  |==| ,   /  |==|   `.-. "
    snk5 = " \==\ -\  |==| ,  | -|\==\,   - \ |==|-  .|  /==/_ ,    / "
    snk6 = " _\==\ ,\ |==| -   _ |/==/ -   ,| |==| _ , \ |==|    .-'  "
    snk7 = "/==/\/ _ ||==|  /\ , /==/-  /\ - \/==/  '\  ||==|_  ,`-._ "
    snk8 = "\==\ - , //==/, | |- \==\ _.\=\.-'\==\ /\=\.'/==/ ,     / "
    snk9 = " `--`---' `--`./  `--``--`         `--`      `--`-----``  "
    hghscr = "High Scores"


    while selection < 0:

        key = men.getch()
        height, width = men.getmaxyx()
        graphics = [0]*5
        graphics[option] = curses.A_REVERSE
        with open('scores.txt','r') as f:
            men.addstr(1, 1, snk1 + " "*4 + hghscr)
            f_contents = f.readline()
            f_contents = f.readline()
            men.addstr(2, 1, snk2 + " "*4 + f_contents)
            f_contents = f.readline()
            men.addstr(3, 1, snk3 + " "*4 + f_contents)
            f_contents = f.readline()
            men.addstr(4, 1, snk4 + " "*4 + f_contents)
            f_contents = f.readline()
            men.addstr(5, 1, snk5 + " "*4 + f_contents)
            f_contents = f.readline()
            men.addstr(6, 1, snk6 + " "*4 + f_contents)
            f_contents = f.readline()
            men.addstr(7, 1, snk7 + " "*4 + f_contents)
            f_contents = f.readline()
            men.addstr(8, 1, snk8 + " "*4 + f_contents)
            f_contents = f.readline()
            men.addstr(9, 1, snk9 + " "*4 + f_contents)

        men.addstr(15, int(width/4-2), "Play", graphics[0])
        men.addstr(16, int(width/4-2), "Exit", graphics[1])
        men.addstr(17, int(width/4-3), "Credits", graphics[2])
        men.addstr(18, int(width/4-2), "Instructions", graphics[3])

        men.refresh()
        if key == curses.KEY_UP:
            option = (option - 1) % 5
        elif key == curses.KEY_DOWN:
            option = (option + 1) % 5
        elif key == ord('\n'):
            selection = option

        if selection == 0:
            men.clear()
            curses.wrapper(game)
        elif selection == 1:
            men.clear()
            quit()
        elif selection == 2:
            men.clear()
            t=1
def game(win):
    height, width = win.getmaxyx()
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = KEY_RIGHT                                                    # Initializing values
    score = 0

    snake = [[4,10], [4,9], [4,8]]                                     # Initial snake co-ordinates
    food = [10,20]                                                     # First food co-ordinates

    win.addch(food[0], food[1], '*')                                   # Prints the food

    while key != 27:                                                   # While Esc key is not pressed

        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
        win.timeout(150 - int(len(snake)/5 + len(snake)/10)%120)          # Increases the speed of Snake as its length increases
        height, width = win.getmaxyx()
        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event


        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # If snake crosses the boundaries, make it enter from the other side
        if snake[0][0] == 0:
            snake[0][0] = height - 1
        if snake[0][1] == 0:
            snake[0][1] = width - 1
        if snake[0][0] == height:
            snake[0][0] = 1
        if snake[0][1] == width:
            snake[0][1] = 1


        # If snake runs over itself
        if snake[0] in snake[1:]: break


        if snake[0] == food:                                            # When snake eats the food
            food = []
            score += 1
            while food == []:
                food = [randint(2, height-2), randint(2, width-2)]                 # Calculating next food's coordinates
                if food in snake: food = []
            win.addch(food[0], food[1], '*')
        else:
            last = snake.pop()                                          # [1] If it does not eat the food, length decreases
            win.addch(last[0], last[1], ' ')
        win.addch(snake[0][0], snake[0][1], '#')

    curses.endwin()
    input("Initials please")
    print("\nScore - " + str(score))

def main():
    curses.wrapper(menu)


if __name__ == "__main__":
    main()
