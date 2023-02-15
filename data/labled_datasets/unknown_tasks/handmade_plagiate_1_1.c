#include <math.h>
#include <stdio.h>

void printArray(int arr[], int n)
{
    int abc;
    abc = 0;
    while (abc < n)
    {
        printf("%d ", arr[abc]);
        abc++;
    }
    printf("\n");
}

void insertionSort(int arr[], int n)
{
    int x, tmp, y;
    x = 1;
    while (x < n)
    {
        tmp = arr[x];
        y = x - 1;

        while (y >= 0 && arr[y] > tmp)
        {
            arr[y + 1] = arr[y];
            y = y - 1;
        }
        arr[y + 1] = tmp;
        x++;
    }
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);
    printArray(arr, n);

    return 0;
}
