#include <stdio.h>

int binarySearch(int arr5[], int top, int bottom, int search)
{
    if (bottom >= top)
    {
        int mid = top + (bottom - top) / 2;
        if (arr5[mid] == search)
            return mid;
        if (arr5[mid] > search)
            return binarySearch(arr5, top, mid - 1, search);
        return binarySearch(arr5, mid + 1, bottom, search);
    }
    return -1;
}

int main(void)
{
    int arr5[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr5) / sizeof(arr5[0]);
    int search = 10;
    int result = binarySearch(arr5, 0, n - 1, search);
    (result == -1)
        ? printf("Element is not present in array")
        : printf("Element is present at index %d", result);
    return 0;
}
