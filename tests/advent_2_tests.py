import unittest

import sys
print(sys.path)

def advent2_part1 (formatted_list: list[list[int]]):
    safe_count = 0
    for sublist in formatted_list:
        print(sublist)
        is_safe = True
        is_increasing = sublist[0] < sublist[1]
        for index, ele in enumerate(sublist):
            if index == 0: 
                continue
            prev_ele = sublist[index - 1]
            abs_diff = abs(ele - prev_ele)
            if is_increasing and ele > prev_ele and abs_diff <= 3 or not is_increasing and ele < prev_ele and abs_diff <= 3:
                continue
            else: 
                is_safe = False
                break
        if is_safe:
            safe_count += 1
    
    return { "safe_count": safe_count }


test_list = [
    [1, 2, 3, 4, 5, 6, 7, 8], 
    [8, 7, 6, 5, 4, 3, 2, 1], 
    [2, 1, 3, 4, 5, 6, 7, 8], 
    [1, 4, 3, 4, 5, 6, 7, 8], 
    [8, 2, 1, 4, 5, 6, 7, 8], 
    [7, 9, 11, 13, 16, 16, 23],
    [11, 11, 11]
    # [61, 60, 58, 56, 54],
    # [79, 81, 83, 86, 87, 89, 92],
    # [23, 20, 17, 16, 15, 14, 11, 8],
    # [39, 38, 37, 34, 33, 32],
    # [14, 13, 10, 8, 7, 6],
    # [29, 31, 34, 37, 38, 41, 43],
    # [22, 24, 26, 28, 29, 30],
    # [31, 28, 27, 25, 24],
    # [51, 50, 49, 48, 46, 44, 43],
    # [69, 70, 71, 74, 75, 77]
]

class Tests(unittest.TestCase):
    def test1(self):
        value = advent2_part1(test_list)
        print(value)
        self.assertEqual(advent2_part1(test_list)['safe_count'], 2, "Should be 2")

if __name__ == "__main__":
    unittest.main()