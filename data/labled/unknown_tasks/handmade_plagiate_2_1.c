#include <math.h>
#include <stdio.h>

void insertionSort(int arr[], int n)
{
    for (int idx_0 = 1, KEY, idx_1; idx_0 < n; idx_0++)
    {
        KEY = arr[idx_0];
        idx_1 = idx_0 - 1;

        while (idx_1 >= 0 && arr[idx_1] > KEY)
        {
            arr[idx_1 + 1] = arr[idx_1];
            idx_1 = idx_1 - 1;
        }
        arr[idx_1 + 1] = KEY;
    }
}

void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);
    printArray(arr, n);

    return 0;
}
