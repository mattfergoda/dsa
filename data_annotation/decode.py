from collections import OrderedDict

def get_nums_on_right_of_pyramid(n):
    i = 1
    nums = []
    counter = 2
    while i <= n:
        nums.append(i)
        i = i + counter
        counter += 1

    return nums


# def decode(message_file):
#     with open(message_file) as f:
#         lines = f.readlines()

#     right_pyramid_nums = get_nums_on_right_of_pyramid(len(lines))

#     words = OrderedDict()

#     for num in right_pyramid_nums:
#         words[num] = ''
    
#     result = ''
#     for line in lines:
#         num, word = line.rstrip().split(' ')
#         num = int(num)
#         if num in words.keys():
#             words[num] = word

#     for word in words.values():
#         result += word + ' '

#     return result.strip()


def decode(message_file):
    with open(message_file) as f:
        lines = f.readlines()

    words = {}
    for line in lines:
        num, word = line.rstrip().split(' ')
        words[int(num)] = word

    right_pyramid_nums = get_nums_on_right_of_pyramid(len(lines))

    result = ''
    for num in right_pyramid_nums:
        result += words[num] + ' '

    return result.strip()