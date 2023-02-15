#include <math.h>
#include <stdio.h>

void printArray(int arr[], int n)
{
    int k;
    for (k = 0; k < n; k++)
        printf("%d ", arr[k]);
    printf("\n");
}

void insertionSort(int arr[], int n)
{
    int i_1, schluessel, i_2;
    i_1 = 1;
    while (i_1 < n)
    {
        schluessel = arr[i_1];
        i_2 = i_1 - 1;

        while (i_2 >= 0 && arr[i_2] > schluessel)
        {
            arr[i_2 + 1] = arr[i_2];
            i_2 = i_2 - 1;
        }
        arr[i_2 + 1] = schluessel;
        i_1++;
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
