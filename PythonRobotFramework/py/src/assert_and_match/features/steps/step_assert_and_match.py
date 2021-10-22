from hamcrest import *

def add_up(a, b):
    return a+b

ans1 = assert_that(add_up(3, 4), equal_to(7), 'test one / must = 7')
ans2 = assert_that(add_up(3.4, 4.4), close_to(8, 0.25), 'test two / approximately 8')

print(ans1, ans2)
