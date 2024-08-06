# Sorting Algorithms and SAT Score Analysis

This project implements a set of sorting algorithms and an SAT score comparison tool using Python. It demonstrates how to create and use custom comparators for sorting and comparison operations.

## Installation

Clone this repository to your local machine. No additional libraries are required beyond the Python standard library.

```bash
git clone https://github.com/vanshikadian/Hybrid_Sorting.git
```

## Usage
You can directly import and use the functions provided in this project for sorting lists and comparing SAT scores.

## Functions
do_comparison: Compares two elements with a custom comparator and order.
selection_sort: Sorts a list using the selection sort algorithm.
bubble_sort: Sorts a list using the bubble sort algorithm.
insertion_sort: Sorts a list using the insertion sort algorithm.
hybrid_merge_sort: Sorts a list using a hybrid of merge sort and insertion sort.
quicksort: Sorts a list using the quicksort algorithm.
better_than_most: Compares a student's SAT scores against the median of a given list.

## Classes
Score: Represents SAT scores for analysis.

## Example
Here's a quick example of how to use the better_than_most function:

```
from your_module import Score, better_than_most

# Create a list of scores
scores = [
    Score(english=700, math=650),
    Score(english=600, math=700),
    Score(english=650, math=600),
]

# Student's score
student_score = Score(english=680, math=670)

# Determine if the student's scores are above the median
result = better_than_most(scores, student_score)
print(result)  # Output: Both, Math, English, or None
