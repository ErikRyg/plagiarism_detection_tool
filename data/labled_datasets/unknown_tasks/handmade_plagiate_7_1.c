#include <stdio.h>

int binarySearch(int integers[], unsigned int start, unsigned int end, unsigned int result)
{
    if (!(end < start))
    {
        int mid = start + (end - start) / 2;
        if (!(integers[mid] != result))
            return mid;
        if (!(integers[mid] <= result))
            return binarySearch(integers, start, mid - 1, result);
        return binarySearch(integers, mid + 1, end, result);
    }
    return -1;
}

int main(void)
{
    int integers[] = {2, 3, 4, 10, 40};
    int n = sizeof(integers) / sizeof(integers[0]);
    int result = 10;
    int result = binarySearch(integers, 0, n - 1, result);
    (result == -1)
        ? printf("Element is not present in array")
        : printf("Element is present at index %d", result);
    return 0;
}
