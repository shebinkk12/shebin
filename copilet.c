#include "stdio.h"

void findLargestSmallest(int arr[], int size, int *largest, int *smallest) {
    *largest = arr[0];
    *smallest = arr[0];

    for(int i = 1; i < size; i++) {
        if(arr[i] > *largest) {
            *largest = arr[i];
        }
        if(arr[i] < *smallest) {
            *smallest = arr[i];
        }
    }
}

int main() {
    int array[] = {3, 5, 1, 9, 7, 2};
    int size = sizeof(array) / sizeof(array[0]);
    int largest, smallest;

    findLargestSmallest(array, size, &largest, &smallest);

    printf("Largest number: %d\n", largest);
    printf("Smallest number: %d\n", smallest);

    return 0;
    
}
