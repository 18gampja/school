/****************************************************************************
 *                                                                          *
 * File    : Loopin.c                                                       *
 *                                                                          *
 * Purpose : Lab 3 we are loopin through time.                              *
 *                                                                          *
 * History : 2/5/2023, Jacob Gampa                                          *
 *                                                                          *
 *                                                                          *
 ****************************************************************************/


#include <stdio.h>
#include <conio.h>
#include <windows.h>

#define MIN_SLEEP_TIME 100
#define MAX_SLEEP_TIME 2000

int main()
{
	// Creating some variables

    int hour, minute, second = 0;
    int sleepTime = MIN_SLEEP_TIME;

    printf("Press any key to start the clock...\n");
    _getch();

	// While loops for hours, minutes, and seconds
    while (hour < 24)
    {
        while (minute < 60)
        {
            while (second < 60)
            {
				// Prints the current time

                _gotoxy(20, 3);
                printf("[%2d:%2d:%2d]", hour, minute, second);

				// Checks for an input, then goes into a switch statement
				// Chooses the correct outcome for the detected input.

				if(_kbhit())
				{
	                int key = _getch();
	                switch (key)
	                {
						// Adds time to sleep timer
		                case '+':
		                    sleepTime += 100;
		                    if (sleepTime > MAX_SLEEP_TIME)
		                    {
		                        sleepTime = MAX_SLEEP_TIME;
								_gotoxy(20, 4);
								char c = (char) sleepTime;
								printf("%2d", c);
		                    }
		                    break;

						// Removes time from sleep timer
		                case '-':
		                    sleepTime -= 100;
		                    if (sleepTime < MIN_SLEEP_TIME)
		                    {
		                        sleepTime = MIN_SLEEP_TIME;
		                    }
		                    break;

						// Escape exits the program
		                case 27:
		                    _gotoxy(0, 24);
		                    return 0;

						// Checks for F5 key to reset timer, any other function key is wrong
		                case 0:
							if (_getch() == 63)
							{
			                    hour = minute = second = 0;
								system("cls");
			                    break;
							}

							else
							{
								_gotoxy(50, 1);
			                    printf("Invalid keystroke: %d", key);
								break;
							}

						// If anything else, wrong key
		                default:
		                    _gotoxy(50, 1);
		                    printf("Invalid keystroke: %d", key);
		                    break;
	                }
				}

				// Sleeps before looping again, then adds a second to the second timer
				Sleep(sleepTime);
				second++;
            }

			// Once out of "seconds" while loop, adds a minute and resets second to 0
			minute++;
			second = 0;
        }

		// Once out of "minutes" while loop, adds an hour then resets minute and second to 0
		hour++;
		minute = 0;
		second = 0;
    }

    return 0;
}
