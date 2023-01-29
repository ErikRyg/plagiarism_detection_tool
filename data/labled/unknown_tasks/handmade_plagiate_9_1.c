#include <stdio.h>

int binarySearch(int list[], unsigned int lef, unsigned int rig, unsigned int find)
{
    if (rig >= lef)
    {
        int mid = lef + (rig - lef) / 2;
        if (list[mid] == find)
            return mid;
        if (list[mid] > find)
            return binarySearch(list, lef, mid - 1, find);
        return binarySearch(list, mid + 1, rig, find);
    }
    return -1;
}

int main(void)
{
    int list[] = {2, 3, 4, 10, 40};
    int n = sizeof(list) / sizeof(list[0]);
    int find = 10;
    int result = binarySearch(list, 0, n - 1, find);
    (result == -1)
        ? printf("Element is not present in array")
        : printf("Element is present at index %d", result);
    return 0;
}
