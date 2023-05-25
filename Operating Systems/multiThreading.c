#include <stdio.h>
#include <windows.h>

#define SIZE 7

int nums[SIZE] = {90, 81, 78, 95, 79, 72, 85};
int avg, min, max;

DWORD WINAPI minimum(LPVOID lpParam) {
    min = nums[0];
    for (int i = 1; i < SIZE; i++) {
        if (nums[i] < min) {
            min = nums[i];
        }
    }
    return 0;
}

DWORD WINAPI maximum(LPVOID lpParam) {
    max = nums[0];
    for (int i = 1; i < SIZE; i++) {
        if (nums[i] > max) {
            max = nums[i];
        }
    }
    return 0;
}

DWORD WINAPI average(LPVOID lpParam) {
    int sum = 0;
    for (int i = 0; i < SIZE; i++) {
        sum += nums[i];
    }
    avg = sum / SIZE;
    return 0;
}

int main() {
	
	# Create the threads
    HANDLE threads[3];
    DWORD threadIds[3];
    threads[0] = CreateThread(NULL, 0, average, NULL, 0, &threadIds[0]);
    threads[1] = CreateThread(NULL, 0, minimum, NULL, 0, &threadIds[1]);
    threads[2] = CreateThread(NULL, 0, maximum, NULL, 0, &threadIds[2]);
	
	# Wait for threads to complete
    WaitForMultipleObjects(3, threads, TRUE, INFINITE);

    printf("The average value is %d\n", avg);
    printf("The minimum value is %d\n", min);
    printf("The maximum value is %d\n", max);

	# Close threads
    CloseHandle(threads[0]);
    CloseHandle(threads[1]);
    CloseHandle(threads[2]);

    return 0;
}
