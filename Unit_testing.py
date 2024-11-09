import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):

    # Test case to check basic sorting
    def test_postive(self):
        
        array = [3, 1, 4, 1, 5]
        sorted_array = quick_sort(array)
        self.assertEqual(sorted_array, [1, 1, 3, 4, 5])
    
    # Test case for handling an empty array
    def test_empty_array(self):

        array = []
        sorted_array = quick_sort(array)
        self.assertEqual(sorted_array, [])

    # Test case for handling an array with one element
    def test_single_element_array(self):
        array = [42]
        sorted_array = quick_sort(array)
        self.assertEqual(sorted_array, [42])

    # Test case to handle an array with duplicate elements
    def test_array_with_duplicates(self):
        array = [5, 3, 5, 3, 1]
        sorted_array = quick_sort(array)
        self.assertEqual(sorted_array, [1, 3, 3, 5, 5])

    # Test a reverse-sorted array
    def test_reverse_sorted_array(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # Test case for checking idempotency
    def test_already_sorted_array(self):
        array = [1, 2, 3, 4, 5]
        sorted_array = quick_sort(array)
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        
        # Running quick_sort again to check idempotency
        sorted_again = quick_sort(sorted_array)
        self.assertEqual(sorted_array, sorted_again)

# Run the tests
if __name__ == '__main__':
    unittest.main()
