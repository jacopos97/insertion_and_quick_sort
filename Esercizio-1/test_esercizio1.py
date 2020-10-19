import unittest
from esercizio_1 import Array
import time
import sys

sys.setrecursionlimit(1250)


class TestArray(unittest.TestCase):

    def setUp(self):
        self.array1 = Array(10, 0)
        self.array2 = Array(100, 0)
        self.array3 = Array(1000, 0)
        self.array4 = Array(10000, 0)
        self.array5 = Array(100000, 0)
        self.array6 = Array(10, 1)
        self.array7 = Array(100, 1)
        self.array8 = Array(1000, 1)
        self.array9 = Array(10000, 1)
        self.array10 = Array(100000, 1)
        self.array11 = Array(10, 2)
        self.array12 = Array(100, 2)
        self.array13 = Array(1000, 2)
        self.array14 = Array(10000, 2)
        self.array15 = Array(100000, 2)

    def test_quick_sort(self):
        initial_time = time.time()
        if not self.array1.quick_sort(0, self.array1.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array1.get_length() - 1):
                self.assertLessEqual(self.array1.get_value(i), self.array1.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array1 ha eseguito quick sort con array random in " + str(execution_time))
        else:
            print("Array1 ha superato il limite di tempo per quick sort con array random")
        initial_time = time.time()
        if not self.array2.quick_sort(0, self.array2.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array2.get_length() - 1):
                self.assertLessEqual(self.array2.get_value(i), self.array2.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array2 ha eseguito quick sort con array random in " + str(execution_time))
        else:
            print("Array2 ha superato il limite di tempo per quick sort con array random")
        initial_time = time.time()
        if not self.array3.quick_sort(0, self.array3.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array3.get_length() - 1):
                self.assertLessEqual(self.array3.get_value(i), self.array3.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array3 ha eseguito quick sort con array random in " + str(execution_time))
        else:
            print("Array3 ha superato il limite di tempo per quick sort con array random")
        initial_time = time.time()
        if not self.array4.quick_sort(0, self.array4.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array4.get_length() - 1):
                self.assertLessEqual(self.array4.get_value(i), self.array4.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array4 ha eseguito quick sort con array random in " + str(execution_time))
        else:
            print("Array4 ha superato il limite di tempo per quick sort con array random")
        initial_time = time.time()
        if not self.array5.quick_sort(0, self.array5.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array5.get_length() - 1):
                self.assertLessEqual(self.array5.get_value(i), self.array5.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array5 ha eseguito quick sort con array random in " + str(execution_time))
        else:
            print("Array5 ha superato il limite di tempo per quick sort con array random")
        print("---")
        initial_time = time.time()
        if not self.array6.quick_sort(0, self.array6.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array6.get_length() - 1):
                self.assertLessEqual(self.array6.get_value(i), self.array6.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array6 ha eseguito quick sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array6 ha superato il limite di tempo per quick sort con array nel caso peggiore")
        initial_time = time.time()
        if not self.array7.quick_sort(0, self.array7.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array7.get_length() - 1):
                self.assertLessEqual(self.array7.get_value(i), self.array7.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array7 ha eseguito quick sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array7 ha superato il limite di tempo per quick sort con array nel caso peggiore")
        initial_time = time.time()
        if not self.array8.quick_sort(0, self.array8.get_length() - 1, time.time() + 60*2, False):
            final_time = time.time()
            for i in range(0, self.array8.get_length() - 1):
                self.assertLessEqual(self.array8.get_value(i), self.array8.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array8 ha eseguito quick sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array8 ha superato il limite di tempo per quick sort con array nel caso peggiore")
        print("---")

    def test_insertion_sort(self):
        initial_time = time.time()
        if self.array1.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array1.get_length() - 1):
                self.assertLessEqual(self.array1.get_value(i), self.array1.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array1 ha eseguito insertion sort con array random in " + str(execution_time))
        else:
            print("Array1 ha superato il limite di tempo per insertion sort con array random.")
        initial_time = time.time()
        if self.array2.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array2.get_length() - 1):
                self.assertLessEqual(self.array2.get_value(i), self.array2.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array2 ha eseguito insertion sort con array random in " + str(execution_time))
        else:
            print("Array2 ha superato il limite di tempo per insertion sort con array random.")
        initial_time = time.time()
        if self.array3.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array3.get_length() - 1):
                self.assertLessEqual(self.array3.get_value(i), self.array3.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array3 ha eseguito insertion sort con array random in " + str(execution_time))
        else:
            print("Array3 ha superato il limite di tempo per insertion sort con array random.")
        initial_time = time.time()
        if self.array4.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array4.get_length() - 1):
                self.assertLessEqual(self.array4.get_value(i), self.array4.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array4 ha eseguito insertion sort con array random in " + str(execution_time))
        else:
            print("Array4 ha superato il limite di tempo per insertion sort con array random.")
        initial_time = time.time()
        if self.array5.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array5.get_length() - 1):
                self.assertLessEqual(self.array5.get_value(i), self.array5.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array5 ha eseguito insertion sort con array random in " + str(execution_time))
        else:
            print("Array5 ha superato il limite di tempo per insertion sort con array random.")
        print("---")
        initial_time = time.time()
        if self.array6.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array6.get_length() - 1):
                self.assertLessEqual(self.array6.get_value(i), self.array6.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array6 ha eseguito insertion sort con array nel caso migliore in " + str(execution_time))
        else:
            print("Array6 ha superato il limite di tempo per insertion sort con array nel caso migliore.")
        initial_time = time.time()
        if self.array7.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array7.get_length() - 1):
                self.assertLessEqual(self.array7.get_value(i), self.array7.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array7 ha eseguito insertion sort con array nel caso migliore in " + str(execution_time))
        else:
            print("Array7 ha superato il limite di tempo per insertion sort con array nel caso migliore.")
        initial_time = time.time()
        if self.array8.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array8.get_length() - 1):
                self.assertLessEqual(self.array8.get_value(i), self.array8.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array8 ha eseguito insertion sort con array nel caso migliore in " + str(execution_time))
        else:
            print("Array8 ha superato il limite di tempo per insertion sort con array nel caso migliore.")
        initial_time = time.time()
        if self.array9.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array9.get_length() - 1):
                self.assertLessEqual(self.array9.get_value(i), self.array9.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array9 ha eseguito insertion sort con array nel caso migliore in " + str(execution_time))
        else:
            print("Array9 ha superato il limite di tempo per insertion sort con array nel caso migliore.")
        initial_time = time.time()
        if self.array10.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array10.get_length() - 1):
                self.assertLessEqual(self.array10.get_value(i), self.array10.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array10 ha eseguito insertion sort con array nel caso migliore in " + str(execution_time))
        else:
            print("Array10 ha superato il limite di tempo per insertion sort con array nel caso migliore.")
        print("---")
        initial_time = time.time()
        if self.array11.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array11.get_length() - 1):
                self.assertLessEqual(self.array11.get_value(i), self.array11.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array11 ha eseguito insertion sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array11 ha superato il limite di tempo per insertion sort con array random nel caso peggiore.")
        initial_time = time.time()
        if self.array12.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array12.get_length() - 1):
                self.assertLessEqual(self.array12.get_value(i), self.array12.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array12 ha eseguito insertion sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array12 ha superato il limite di tempo per insertion sort con array nel caso peggiore.")
        initial_time = time.time()
        if self.array13.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array13.get_length() - 1):
                self.assertLessEqual(self.array13.get_value(i), self.array13.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array13 ha eseguito insertion sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array13 ha superato il limite di tempo per insertion sort con array nel caso peggiore.")
        initial_time = time.time()
        if self.array14.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array14.get_length() - 1):
                self.assertLessEqual(self.array14.get_value(i), self.array14.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array14 ha eseguito insertion sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array14 ha superato il limite di tempo per insertion sort con array nel caso peggiore.")
        initial_time = time.time()
        if self.array15.insertion_sort():
            final_time = time.time()
            for i in range(0, self.array15.get_length() - 1):
                self.assertLessEqual(self.array15.get_value(i), self.array15.get_value(i + 1))
            execution_time = round(final_time - initial_time, 5)
            print("Array15 ha eseguito insertion sort con array nel caso peggiore in " + str(execution_time))
        else:
            print("Array15 ha superato il limite di tempo per insertion sort con array nel caso peggiore.")


if __name__ == '__main__':
    unittest.main()
