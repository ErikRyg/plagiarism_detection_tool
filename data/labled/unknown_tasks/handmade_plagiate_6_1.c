#include <stdio.h>

int binarySearch(int array[], int left, int right, int tmp)
{
    if (left <= right)
    {
        int mid = ((right - left) / 2) + left;
        if (tmp == array[mid])
            return mid;
        if (tmp > array[mid])
            return binarySearch(array, left, mid - 1, tmp);
        return binarySearch(array, mid + 1, right, tmp);
    }
    return -1;
}

int main()
{
    int array[] = {2, 3, 4, 10, 40};
    int n = sizeof(array) / sizeof(array[0]);
    int tmp = 10;
    int result = binarySearch(array, 0, n - 1, tmp);
    (result == -1)
        ? printf("Element is not present in array")
        : printf("Element is present at index %d", result);
    return 0;
}
