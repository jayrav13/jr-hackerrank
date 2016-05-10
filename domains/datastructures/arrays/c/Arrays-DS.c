// HackerRank provided libraries
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

// Main function
int main() {

	// Store number of values in n
	int n; 
	scanf("%d",&n);

	// Memory allocation for array of values
	int *arr = malloc(sizeof(int) * n);

	// Scan values
	for(int i = 0; i < n; i++) {
		scanf("%d",&arr[i]);
	}

	// Print reverse values
	for(int i = n - 1; i >= 0; i--) {
		printf("%d ", arr[i]);
	}

	// Return
	return 0;

}

