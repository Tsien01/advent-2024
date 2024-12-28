

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

## Located bug - Ascending -> Descending is flagged as safe
### FIXED - added not is_increasing to right side of boolean statement