import numpy as np
import time


class Array:
    def __init__(self, length, array_type):
        self.__array_type = array_type
        self.__length = length
        self.__array = []
        if self.__array_type == 0:
            self.__array = np.array(np.random.randint(0, 1000, size=length), dtype=int)
        elif self.__array_type == 1:
            for i in range(0, self.__length):
                self.__array.append(i)
        elif self.__array_type == 2:
            for i in range(length - 1, -1, -1):
                self.__array.append(i)

    def get_length(self):
        return self.__length

    def get_array(self):
        return self.__array

    def get_value(self, pos):
        return self.__array[pos]

    def switch(self, i, j):
        temp = self.__array[i]
        self.__array[i] = self.__array[j]
        self.__array[j] = temp

    def partition(self, p, r):
        pivot = int(self.__array[r])
        i = p - 1
        for j in range(p, r):
            if self.__array[j] <= pivot:
                i = i + 1
                self.switch(i, j)
        i = i + 1
        self.switch(i, r)
        return i

    def quick_sort(self, p, r, timeout, failure):
        if p < r and not failure:
            q = self.partition(p, r)
            #print("Array dopo partition in ", p, "-", r, ":\n", self.__array, "\n\n")
            if time.time() <= timeout and not failure:
                failure = self.quick_sort(p, q - 1, timeout, failure)
            else:
                return True
            if time.time() <= timeout and not failure:
                failure = self.quick_sort(q + 1, r, timeout, failure)
            else:
                return True
            if time.time() <= timeout and not failure:
                return failure
            else:
                return True
        else:
            return failure

    def insertion_sort(self):
        timeout = time.time() + 60*2
        for j in range(1, self.__length):
            if time.time() > timeout:
                return False
            key = self.__array[j]
            i = j - 1
            while i >= 0 and self.__array[i] > key:
                self.__array[i + 1] = self.__array[i]
                i = i - 1
            self.__array[i + 1] = key
            #print("Array al passo ", j, ":\n", self.__array, "\n\n")
        return True


'''
sort_type = int(input("Digitare 0 se si desidera un quick sort o 1 se si desidera un insertion sort:"))
if sort_type == 0:
    length = int(input('Inserisci grandezza array: '))
    array = Array(length, 0)
    print("QUICKSORT:\n", array.get_array(), "\n\n")
    array.quick_sort(0, array.get_length() - 1, time.time() + 60*2, False)
    print("Array ordinato tramite quicksort :\n", array.get_array())
elif sort_type == 1:
    length = int(input('Inserisci grandezza array: '))
    array = Array(length, 0)
    print("INSERTIONSORT:\n", array.get_array(), "\n\n")
    array.insertion_sort()
    print("Array ordinato tramite insertionsort :\n", array.get_array())
else:
    print("Il carattere digitato deve essere 0 o 1!!!")
'''