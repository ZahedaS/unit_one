# File: lib/high_value.py

class HighValue:
    def __init__(self, value_first, value_second):
        if not isinstance(value_first, int) and not isinstance(value_second, int):
            raise TypeError("Incorrect datatype")
        
        self.value_first = value_first
        self.value_second = value_second
        
    def get_highest(self):
        if self.value_first > self.value_second:
            return "First value is higher"
        elif self.value_first < self.value_second:
            return "Second value is higher"
        else:
            return "Values are equal"
        
    def add(self, increase_by, selection):
         if selection == "first":
            self.value_first += increase_by
         elif selection == "second":
            self.value_second += increase_by
         else:
             return "Select first or second"

    


hv = HighValue(3,4)
hv.add(3, "third")
print(hv.get_highest())