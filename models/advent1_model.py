from collections import Counter

def advent1_part1 (input_list1: list[int], input_list2: list[int]):
    sorted_list1 = sorted(input_list1)
    sorted_list2 = sorted(input_list2)
    total_distance = 0
    for index, key in enumerate(sorted_list1):
        total_distance += abs(sorted_list1[index] - sorted_list2[index])
    return { "total_distance": total_distance }

def advent1_part2 (input_list1: list[int], input_list2: list[int]):
    similarity_score = 0
    list2_map = Counter(input_list2)
    for num in input_list1:
        print(list2_map[num])
        if list2_map[num] != 0:
            similarity_score += num * list2_map[num]
    return { "similarity_score": similarity_score }