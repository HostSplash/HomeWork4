import Second2
import First2

x = Second2.get_value()
y = Second2.get_value()

def sum_number():
    First2.init(x)
    Second2.init(y)
    result = x + y
    Second2.view(result)
