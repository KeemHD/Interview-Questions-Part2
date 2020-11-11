#8/21/21

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a string that may represent a number, determine if it is a number.
# Here's some of examples of how the number may be presented:
#"123" # Integer
#"12.3" # Floating point
#"-123" # Negative numbers
#"-.3" # Negative floating point
#"1.5e5" # Scientific notation
#Here's some examples of what isn't a proper number:
#"12a" # No letters
#"1 2" # No space between numbers
#"1e1.2" # Exponent can only be an integer (positive or negative or 0)
#Scientific notation requires the first number to be less than 10,
# however to simplify the solution assume the first number can be greater than 10.
# Do not parse the string with int() or any other python functions.


def parse_number(s):
    # Fill this in.
    print(s)

    neg_count = 0
    e_count = 0
    dot_count = 0

    for n in s:
        if neg_count <= 1 and e_count <= 1 and dot_count <= 1:
            if n == "-":
                neg_count+=1
            elif n == ".":
                dot_count+=1
            elif n == "e":
                e_count+=1
                dot_count = 1

            elif not n.isnumeric():
                return False

        else:
            return False

    return True

print("Determine if Number 8-21")
print("<-----------------START--------------<DONE")
print(parse_number("12.3"))
# True

print(parse_number("12a"))
# False
print("<-----------------END--------------<")


#8/22/20

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a 2d n x m matrix where each cell
# has a certain amount of change on the floor,
# your goal is to start from the top left corner
# mat[0][0] and end in the bottom right corner mat[n - 1][m - 1]
# with the most amount of change. You can only move either left or down.


def max_change(mat):
    # Fill this in.
    for i in range(len(mat)):
        print(mat[i])

mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]
print("Picking up Change 8-22")
print("<-----------------START--------------<")
print(max_change(mat))
# 13
print("<-----------------END--------------<")

#8/23/20

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a list of sorted numbers (can be both negative or positive),
# return the list of numbers squared in sorted order.

#Solve this problem in O(n) time.

def square_numbers(nums):
    # Fill this in.
    print(nums)
    flag = False
    positive = []
    negative = []
    output = []


    for n in nums:

        if n >= 0:
            positive.append(n*n)
            flag = True

        else:
            negative.insert(0,n*n)

        '''    
        if flag:
            if len(negative) == 0:
                output.extend(positive)
                positive.clear()

            elif positive[0] == negative[0]:
                output.append(negative[0])
                negative.pop(0)

            elif positive[0] < negative[0]:
                output.append(positive[0])
                positive.pop(0)
                
            else:
                output.append(negative[0])
                negative.pop(0)
        '''

    while len(negative) > 0:
        if len(negative) == 0:
            output.extend(positive)
            positive.clear()

        elif positive[0] == negative[0]:
            output.append(negative[0])
            negative.pop(0)

        elif positive[0] < negative[0]:
            output.append(positive[0])
            positive.pop(0)

        else:
            output.append(negative[0])
            negative.pop(0)

    return output


print("Sorted Square Numbers 8-23")
print("<-----------------START--------------<DONE")
print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
print("<-----------------END--------------<")


#8/24/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a binary tree, find the level in
# the tree where the sum of all nodes on that level is the greatest.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    # Fill this in.
    print()

n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

print("Level of tree with Maximum Sum 8-24")
print("<-----------------START--------------<")
print(tree_level_max_sum(n1))
# Should print 1 as level 1 has the highest level sum
print("<-----------------END--------------<")

#8/25/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given 2 binary trees t and s, find if s
# has an equal subtree in t, where the structure
# and the values are the same. Return True if it exists,
# otherwise return False.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def find_subtree(s, t):
    # Fill this in.
    print()

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print("Find Subtree Sum 8-25")
print("<-----------------START--------------<")
print(find_subtree(s, t))
# True
print("<-----------------END--------------<")

#8/26/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a list of words in a string,
# reverse the words in-place
# (ie don't create a new string and reverse the words).
# Since python strings are not mutable,
# you can assume the input will be a mutable sequence (like list).

def reverse_words(words):
    # Fill this in.
    print(words)


print("Reverse Words 8-26")
print("<-----------------START--------------<")
s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can
print("<-----------------END--------------<")

#8/27/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given 2 strings s and t, find and return all
# indexes in string s where t is an anagram.


def find_anagrams(s, t):
    # Fill this in.
    print()

print("Anagrams in a String 8-27")
print("<-----------------START--------------<")
print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
print("<-----------------END--------------<")

#8/28/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a 32-bit integer, swap the 1st and 2nd bit,
# 3rd and 4th bit, up til the 31st and 32nd bit.

def swap_bits(num):
    # Fill this in.
    print(num)
    return 0

print("Swap Bits 8-28")
print("<-----------------START--------------<")
print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101
print("<-----------------END--------------<")

#8/29/20
#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a string, convert it to an integer
# without using the builtin str function.
# You are allowed to use ord to convert a
# character to ASCII code.

#Consider all possible cases of an integer.
# In the case where the string is not a valid integer,
# return None.


def convert_to_int(s):
    # Fill this in.
    print(s)
    return int(s)

print("String to Integer 8-29")
print("<-----------------START--------------<")
print(convert_to_int('-105') + 1)
# -104
print("<-----------------END--------------<")

#8/30/20
#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Given a square 2D matrix (n x n),
# rotate the matrix by 90 degrees clockwise.


def rotate(mat):
    # Fill this in.
    print(mat)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
print("Rotate Matrix 8-30")
print("<-----------------START--------------<")
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print("<-----------------END--------------<")

#8/31/20
#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#The power function calculates x raised to the
# nth power. If implemented in O(n) it would
# simply be a for loop over n and multiply x n
# times. Instead implement this power function
# in O(log n) time. You can assume that n will
# be a non-negative integer.

def pow(x, n):
    # Fill this in.
    print()

print("Power Function 8-31")
print("<-----------------START--------------<")
print(pow(5, 3))
# 125
print("<-----------------END--------------<")

#9/1/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a positive integer, find the square
# root of the integer without using any
# built in square root or power functions
# (math.sqrt or the ** operator). Give accuracy
# up to 3 decimal points.


def sqrt(x):
    # Fill this in.
    print(x)


print("Squareroot 9-1")
print("<-----------------START--------------<")
print(sqrt(5))
# 2.236
print("<-----------------END--------------<")

#9/2/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a sorted list of numbers,
# and two integers low and high representing
# the lower and upper bound of a range,
# return a list of (inclusive) ranges where the
# numbers are missing. A range should be represented
# by a tuple in the format of (lower, upper).


def missing_ranges(nums, low, high):
    # Fill this in.
    print()


print("Missing Ranges 9-2")
print("<-----------------START--------------<")
print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
print("<-----------------END--------------<")

#9/3/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#A Sudoku board is a 9x9 grid, where each row,
# column and each 3x3 subbox contains the number
# from 1-9. Here's an example of a Sudoku board.
#-------------
#|534|678|912|
#|672|195|348|
#|198|342|567|
#|------------
#|859|761|423|
#|426|853|791|
#|713|924|856|
#|------------
#|961|537|284|
#|287|419|635|
#|345|286|179|
#|------------

#Given a 9x9 board, determine if it is a valid Sudoku
#board. The board may be partially filled,
# where an empty cell will be represented by
# the space character ' '.

def validate_sudoku(board):
    # Fill this in.
    print(board)

board = [
    [5, ' ', 4, 6, 7, 8, 9, 1, 2],
    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
    [1,   9, 8, 3, 4, 2, 5, 6, 7],
    [8,   5, 9, 7, 6, 1, 4, 2, 3],
    [4,   2, 6, 8, 5, 3, 7, 9, 1],
    [7,   1, 3, 9, 2, 4, 8, 5, 6],
    [9,   6, 1, 5, 3, 7, 2, 8, 4],
    [2,   8, 7, 4, 1, 9, 6, 3, 5],
    [3,   4, 5, 2, 8, 6, 1, 7, 9],
]

print("Sudoku Check 9-3")
print("<-----------------START--------------<")
print(validate_sudoku(board))
# True
print("<-----------------END--------------<")

#9/4/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a number n, find the least number of
# squares needed to sum up to the number.

def square_sum(n):
    # Fill this in.
    print(n)
    i = 1
    solution_list = []
    remainder = n

    while remainder > 0:
        while (i*i) <= remainder:
            i+=1
        i = i - 1
        remainder = remainder % (i*i)
        solution_list.append(i)
        i =1

    #print(solution_list)
    return len(solution_list)

print("Sum of Squares 9-4")
print("<-----------------START--------------<Done")
print(square_sum(13))
# Min sum is 3^2 + 2^2
# 2
print("<-----------------END--------------<")

#9/5/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#A task is a some work to be done which can
# be assumed takes 1 unit of time. Between the
# same type of tasks you must take at least n
# units of time before running the same tasks again.

#Given a list of tasks (each task will be represented by a string),
# and a positive integer n representing the time it takes to
# run the same task again, find the minimum amount of time needed
# to run all tasks.


def schedule_tasks(tasks, n):
    # Fill this in.
    print(tasks,n)

print("Schedule Tasks 9-5")
print("<-----------------START--------------<")
print(schedule_tasks(['q', 'q', 's', 'q', 'w', 'w'], 4))
# print 6
# one of the possible orders to run the task would be
# 'q', 'w', idle, idle, 'q', 'w'
print("<-----------------END--------------<")

#9/6/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a sorted linked list of integers,
# remove all the duplicate elements in the
# linked list so that all elements in the linked list are unique.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(lst):
    # Fill this in.
    print()

lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

print("Remove Duplicate from Linked List 9-6")
print("<-----------------START--------------<")
remove_dup(lst)
print(lst)
# (1, (2, (3, None)))
print("<-----------------END--------------<")


#9/7/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#N-Queens is the problem where you
# find a way to put n queens on a nxn
# chess board without them being able
# to attack each other. Given an integer
# n, return 1 possible solution by returning
# all the queen's position.

def n_queens(n):
    # Fill this in.
    print(n)

print("Queens on a chessboard 9-7")
print("<-----------------START--------------<")
print(n_queens(5))
# There can be many answers
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
print("<-----------------END--------------<")

#9/8/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a valid parenthesis string
# (with only '(' and ')', an
# open parenthesis will always end
# with a close parenthesis, and a close
# parenthesis will never start first),
# remove the outermost layers of the
# parenthesis string and return the new
# parenthesis string.

#If the string has multiple outer layer parenthesis
# (ie (())()), remove all outer layers and
# construct the new string. So in the example,
# the string can be broken down into (()) + ().
# By removing both components outer layer we are
# left with () + '' which is simply (),
# thus the answer for that input would be ().


def remove_outermost_parenthesis(s):
    # Fill this in.
    print(s)

print("Remove One Layer of Parenthesis 9-8")
print("<-----------------START--------------<")
print(remove_outermost_parenthesis('(())()'))
# ()

print(remove_outermost_parenthesis('(()())'))
# ()()

print(remove_outermost_parenthesis('()()()'))
# ' '
print("<-----------------END--------------<")

#9/9/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a list of undirected edges which represents a graph,
# find out the number of connected components.

#In the above example, vertices 1, 2, 3, 4 are all connected,
# and 5, 6 are connected, and thus there are 2 connected components
# in the graph above.

def num_connected_components(edges):
    # Fill this in.
    print(edges)

print("Number of Connected Componets 9-9")
print("<-----------------START--------------<")
print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
# 2
print("<-----------------END--------------<")

#9/10/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a non-negative integer n, convert n to
# base 2 in string form. Do not use any built in
# base 2 conversion functions like bin.

#In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123.

def base_2(n):
    # Fill this in.
    print(n)
    binary_num = ""

    while  n != 0:
        binary_num += str(n%2)
        n = int(n/2)

    return binary_num[::-1]

print("Convert to Base Two 9-10")
print("<-----------------START--------------<DONE")
print(base_2(123))
# 1111011
print("<-----------------END--------------<")

#9/11/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a binary search tree (BST) and a value s,
# split the BST into 2 trees, where one tree
# has all values less than or equal to s,
# and the other tree has all values greater
# than s while maintaining the tree structure of
# the original BST. You can assume that s will be
# one of the node's value in the BST.
# Return both tree's root node as a tuple.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"

def split_bst(bst, s):
    # Fill this in.
    print()

n2 = Node(2)
n1 = Node(1, None, n2)

n5 = Node(5)
n4 = Node(4, None, n5)

root = Node(3, n1, n4)

print("Split a Binary Search Tree 9-11")
print("<-----------------START--------------<")
print(root)
# (3, (1, (2)), (4, None, (5)))
# How the tree looks like
#     3
#   /   \
#  1     4
#   \     \
#    2     5

print(split_bst(root, 2))
# ((1, None, (2)), (3, None, (4, None, (5))))
# Split into two trees
# 1    And   3
#  \          \
#   2          4
#               \
#                5
print("<-----------------END--------------<")

#9/12/20
#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a list of points as a tuple (x, y) and an
# integer k, find the k closest points to the origin (0, 0).

def closest_points(points, k):
    # Fill this in.
    print(points,k)

print("Find Closest Points 9-12")
print("<-----------------START--------------<")
print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]
print("<-----------------END--------------<")

#9/13/20
#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Given a binary tree, find all duplicate
# subtrees (subtrees with the same value and same structure)
# and return them as a list of list [subtree1, subtree2, ...]
# where subtree1 is a duplicate of subtree2 etc.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"

def dup_trees(root):
    # Fill this in.
    print()

n3_1 = Node(3)
n2_1 = Node(2, n3_1)
n3_2 = Node(3)
n2_2 = Node(2, n3_2)
n1 = Node(1, n2_1, n2_2)
# Looks like
#     1
#    / \
#   2   2
#  /   /
# 3   3

print("Duplicate Subtrees 9-13")
print("<-----------------START--------------<")
print(dup_trees(n1))
# [[(3), (3)], [(2, (3)), (2, (3))]]
# There are two duplicate trees
#
#     2
#    /
#   3
# and just the leaf
#
# 3
print("<-----------------END--------------<")

#9/14/20
#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#Given a list of sorted numbers,
# and two integers k and x, find k
# closest numbers to the pivot x.

def closest_nums(nums, k, x):
    # Fill this in.
    print(nums,k,x)
    '''found = False
    start_pos = 0
    end_pos = len(nums)-1
    mid_pos = int((start_pos + end_pos)/2)

    while start_pos <= end_pos:

        if nums[mid_pos] > k:
            end_pos = mid_pos - 1

        elif nums[mid_pos] < k:
            start_pos = mid_pos + 1

        else:
            found = True
            break

        mid_pos = int((start_pos + end_pos)/2)

    if found:
        print(nums[mid_pos])
    else:
        print(str(k) + " was not found in the list: " + str(nums))'''

print("K Closest Elements 9-14")
print("<-----------------START--------------<")
print(closest_nums([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]
print("<-----------------END--------------<")

#9/15/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a list of numbers, for each element
# find the next element that is larger than the current element.
# Return the answer as a list of indices.
# If there are no elements larger than the current
# element, then use -1 instead.

def larger_number(nums):
    # Fill this in.
    print(nums)


print("Index of Larger Next Number 9-15")
print("<-----------------START--------------<")
print(larger_number([3, 2, 5, 6, 9, 8]))
# print [2, 2, 3, 4, -1, -1]
print("<-----------------END--------------<")

#9/16/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a string, determine if you can
# remove any character to create a palindrome.


def create_palindrome(s):
    # Fill this in.
    print(s)

print("Remove Character to Create Palindrome 9-16")
print("<-----------------START--------------<")
print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False
print("<-----------------END--------------<")

#9/17/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a list of meetings that will happen
# during a day, find the minimum number of
# meeting rooms that can fit all meetings.

#Each meeting will be represented by a tuple of
# (start_time, end_time), where both start_time
# and end_time will be represented by an integer
# to indicate the time. start_time will be inclusive,
# and end_time will be exclusive, meaning a meeting
# of (0, 10) and (10, 20) will only require 1 meeting room.

def meeting_rooms(meetings):
    # Fill this in.
    print(meetings)
    time_list = []
    room_list = []

    time_list.append(meetings[0])
    meetings.pop(0)

    while len(meetings) > 0:
        inserted = False
        for tup in time_list:
            start_time = tup[0]
            end_time = tup[1]

            if meetings[0][0] < start_time:
                time_list.insert(0,meetings[0])
                meetings.pop(0)
                inserted = True
                break

        if not inserted:
            time_list.append(meetings[0])
            meetings.pop(0)

    start = time_list[0][0]
    end = time_list[0][1]
    #print(time_list)
    time_list.pop(0)

    for tup in time_list:
        if end <= tup[0]:
            end = tup[1]

        else:
            room_list.append((start,end))
            start = tup[0]
            end = tup[1]

        if tup[1] == time_list[-1][1]:
            room_list.append((start, end))

    print("Merged -> "+ str(room_list))
    return len(room_list)


print("Number of Meeting Rooms 9-17")
print("<-----------------START--------------<")
# print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)
print("<-----------------END--------------<")

#9/18/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a numerator and a denominator,
# find what the equivalent decimal representation
# is as a string. If the decimal representation
# has recurring digits, then put those digits in
# brackets (ie 4/3 should be represented by 1.(3)
# to represent 1.333...). Do not use any built in
# evaluator functions like python's eval. You can
# also assume that the denominator will be nonzero.

def frac_to_dec(numerator, denominator):
    # Fill this in.
    print(str(numerator)+"/"+str(denominator))
    num = str(numerator/denominator)


    count = 1
    dot = False
    solution = ""

    prev = num[0]

    for i in range(1, len(num)):
        if prev == ".":
            dot = True
            solution+= prev
        elif dot:
            if prev == num[i]:
                count+=1
            else:
                solution+=prev
                if count != 1:
                    if count > int(prev):
                        count = int(prev)
                        solution = solution[:-1]
                    solution+="("
                    solution += str(count)
                    solution += ")"
                count = 1
        else:
            solution += prev
        prev = num[i]

    solution += prev
    if count != 1:
        if count > int(prev):
            count = int(prev)
            solution = solution[:-1]

        solution += "("
        solution += str(count)
        solution += ")"

    return(solution)

print("Convert Fraction to Decimal 9-18")
print("<-----------------START--------------<")
print(frac_to_dec(-3, 2))
# -1.5

print(frac_to_dec(4, 3))
# 1.(3)

print(frac_to_dec(1, 6))
# 0.1(6)
print("<-----------------END--------------<")

#9/19/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a positive integer n, find all primes less than n.

def find_primes(n):
    # Fill this in.
    print(n)
    prime_list = []
    i = 2

    while i <= n:
        for x in range(2,i):
            if (i % x) == 0:
                break
        else:
            prime_list.append(i)
        i+=1
    return prime_list

print("Primes 9-19")
print("<-----------------START--------------<")
print(find_primes(14))
# [2, 3, 5, 7, 11, 13]
print("<-----------------END--------------<")

#9/20/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a non-negative integer n, convert
# the integer to hexadecimal and return the
# result as a string. Hexadecimal is a base
# 16 representation of a number, where the
# digits are 0123456789ABCDEF. Do not use any
# builtin base conversion functions like hex.

def to_hex(n):
    # Fill this in.
    print(n)
    bit_stream = ""
    hex = ""

    while n != 0:
        bit_stream += str(n%2)
        n = int(n/2)

    if len(bit_stream)%4 != 0:
        pad = 4 - len(bit_stream)%4

        i = 0
        while i < pad:
            bit_stream+="0"
            i+=1

    bit_stream = bit_stream[::-1]

    if len(bit_stream) > 0:
        start = 0
        end = 4

        while end <= len(bit_stream):
            hex += get_hex(bit_stream[start:end])
            start +=4
            end +=4
    else:
        return "There was an Error!"

    return hex

def get_hex(s):
    if s == "0000":
        return "0"
    elif s == "0001":
        return "1"
    elif s == "0010":
        return "2"
    elif s == "0011":
        return "3"
    elif s == "0100":
        return "4"
    elif s == "0101":
        return "5"
    elif s == "0110":
        return "6"
    elif s == "0111":
        return "7"
    elif s == "1000":
        return "8"
    elif s == "1001":
        return "9"
    elif s == "1010":
        return "A"
    elif s == "1011":
        return "B"
    elif s == "1100":
        return "C"
    elif s == "1101":
        return "D"
    elif s == "1110":
        return "E"
    elif s == "1111":
        return "F"

print("Convert to Hexadecimal 9-20")
print("<-----------------START--------------<")
print(to_hex(123))
# 7B
print("<-----------------END--------------<")

#9/21/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given two strings which represent non-negative
# integers, multiply the two numbers and return
# the product as a string as well. You should
# assume that the numbers may be sufficiently
# large such that the built-in integer type will
# not be able to store the input (Python does have
# BigNum, but assume it does not exist).

def multiply(str1, str2):
    # Fill this in.
    print(str1,str2)

    solution = float(str1)*float(str2)
    return str(int(solution))

print("Multiply 9-21")
print("<-----------------START--------------<")
print(multiply("11", "13"))
# 143
print("<-----------------END--------------<")

#9/22/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a string, we want to remove 2 adjacent
# characters that are the same, and repete the
# process with the new string until we coan no longer
# perform the operation.

def remove_adjacent_dup(s):
    #Fill this in.
    print(s)
    prev_char = s[0]
    temp = ""
    i = 1
    length = len(s)

    while i < length:
        if prev_char == s[i]:
            temp = s[:i-1]
            temp+= s[i+1:]
            s = temp
            length = len(s)
            i = 0
        else:
            prev_char = s[i]
        i+=1

    return s

print("Remove Adjacent Duplicate Characters 9-22")
print("<-----------------START--------------<")
print(remove_adjacent_dup('cabba'))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c
print("<-----------------END--------------<")


#9/23/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

# Given a list of strings, find the list of characters that
# appear in all strings.

def common_characters(strs):
    # Fill this in
    print(strs)
    solution = []
    character_dict = {}
    total_letter_words = 0
    words_of_str = ""

    for words in strs:
        words_of_str += words
        for l in words:
            if l not in character_dict:
                character_dict[l] = words

            elif l in character_dict and character_dict[l] != words_of_str:
                character_dict[l] += words

            total_letter_words += 1


    for x in character_dict:
        if len(character_dict[x]) == total_letter_words:
            solution.append(x)

    return solution

print("Common Characters 9-23")
print("<-----------------START--------------<")
print(common_characters(['google' , 'facebook' , 'youtube']))
# ['e', 'o']
print("<-----------------END--------------<")

#9/24/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a matrix, transpose it. Transposing a matrix
# means the rows are now the colum and vice-versa.

def transpose(mat):
    # Fill this in.
    tran_matrix = []
    n=0

    for x in mat:
        print(x)

    while n < len(mat[0]):
        temp = []
        for i in range(len(mat)):
            temp.append(mat[i][n])
        tran_matrix.append(temp)
        n+=1

    return tran_matrix

mat = [
    [1,2,3],
    [4,5,6],
]

print("Transpose Matrix 9-24")
print("<-----------------START--------------<")
print(transpose(mat))
# [[1,4],
#  [2,5],
#  [3,6]]
print("<-----------------END--------------<")

#9/25/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given 3 sorted lists, find the intersection of those 3 lists.


def intersection(list1, list2, list3):
    # Fill this in.
    print()

print("Intersection of Lists 9-25")
print("<-----------------START--------------<")
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]
print("<-----------------END--------------<")


#9/26/20
#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#You are only allowed to perform 2 operations,
# multiply a number by 2, or subtract a number by 1.
# Given a number x and a number y, find the minimum number
# of operations needed to go from x to y.

def min_operations(x, y):
    # Fill this in.
    print()

print("Minimum Number of Operations 9-26")
print("<-----------------START--------------<")
print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3
print("<-----------------END--------------<")

#9/27/20
#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Given a string s and a character c,
# find the distance for all characters in
# the string to the character c in the string s.
# You can assume that the character c will appear
# at least once in the string.

def shortest_dist(s, c):
    # Fill this in.
    print(s,c)
    distance = []
    count = 0
    rev_count = 0

    for i in range(len(s)):
        for char in s[i:]:
            if char == c:
                break
            else:
                count+=1
        x = i
        while x > 0:
            if s[x] == c:
                break
            else:
                rev_count += 1
            x-=1

        if rev_count<count and rev_count != 0:
            count = rev_count

        distance.append(count)
        rev_count = 0
        count = 0

    return distance

print("Shortest Distance to Character 9-27")
print("<-----------------START--------------<")
print(shortest_dist('helloworld', 'l'))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
print("<-----------------END--------------<")

#9/28/20
#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#Pascal's Triangle is a triangle where all numbers
# are the sum of the two numbers above it.
# Here's an example of the Pascal's Triangle of size 5.
#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1
#Given an integer n, generate the n-th row of the Pascal's Triangle.

def pascal_triangle_row(n):
    # Fill this in.
    print()

print("Pascal's Triangle 9-28")
print("<-----------------START--------------<")
print(pascal_triangle_row(6))
# [1, 5, 10, 10, 5, 1]
print("<-----------------END--------------<")

#9/29/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a list of numbers and a target number n,
# find 3 numbers in the list that sums closest to the
# target number n. There may be multiple ways of
# creating the sum closest to the target number,
# you can return any combination in any order.

def closest_3sum(nums, target):
    # Fill this in.
    print()

print("Closest to 3 Sum 9-29")
print("<-----------------START--------------<")
print(closest_3sum([2, 1, -5, 4], -1))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]
print("<-----------------END--------------<")

#9/30/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given two binary numbers represented as strings,
# return the sum of the two binary numbers as a
# new binary represented as a string. Do this without
# converting the whole binary string into an integer.

def sum_binary(bin1, bin2):
    # Fill this in.
    print(bin1+" + "+bin2)
    total = 0
    base = 0

    if(len(bin1)> len(bin2)):
        temp = bin1
        bin1 = bin2
        bin2 = temp

    while len(bin1)> 0:
        if bin1[-1] == "1":
            total += (2**base)

        if bin2[-1] == "1":
            total+=(2**base)

        base += 1
        bin1 = bin1[:-1]
        bin2 = bin2[:-1]

    while len(bin2)> 0:
        if bin2[-1] == "1":
            total += (2 ** base)
        base += 1
        bin2 = bin2[:-1]

    total = bin(total)
    bin_str_solution = str(total)

    return bin_str_solution[2:]

print("Sum Binary Numbers 9-30")
print("<-----------------START--------------<")
print(sum_binary("11101", "1011"))
# 101000
print("<-----------------END--------------<")

#10/1/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Reshaping a matrix means to take the same elements
# in a matrix but change the row and column length.
# This means that the new matrix needs to have the
# same elements filled in the same row order as the
# old matrix. Given a matrix, a new row size x and
# a new column size y, reshape the matrix.
# If it is not possible to reshape, return None.

def reshape_matrix(mat, x, y):
    # Fill this in.
    print()

print("Reshaping Matrix 10-1")
print("<-----------------START--------------<")
print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
print("<-----------------END--------------<")

#10/2/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given an integer, reverse the digits.
# Do not convert the integer into a string and reverse it.

def reverse_integer(num):
    # Fill this in.
    print(num)
    negative = False
    rev_num = 0
    place = 1

    if num < 0:
        num *= -1
        negative = True

    i = 1

    while i < len(str(num)):
        place *= 10
        i += 1

    while num>0:
        temp = num%10
        num = int(num/10)
        rev_num += temp*place
        place/=10

    if negative:
        rev_num *=-1

    return int(rev_num)

print("Reverse Integer 10-2")
print("<-----------------START--------------<")
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123
print("<-----------------END--------------<")

#10/3/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given an integer, convert the integer to a roman numeral.
# You can assume the input will be between 1 to 3999.

#The rules for roman numerals are as following:

#There are 7 symbols, which correspond to the following values.
#I   1
#V   5
#X   10
#L   50
#C   100
#D   500
#M   1000
#The value of a roman numeral are the digits added together.
# For example the roman numeral 'XX' is V + V = 10 + 10 = 20.
# Typically the digits are listed from largest to smallest,
# so X should always come before I. Thus the largest possible
# digits should be used first before the smaller digits
# (so to represent 50, instead of XXXXX, we should use L).

#There are a couple special exceptions to the above rule.

#To represent 4, we should use IV instead of IIII.
# Notice that I comes before V.
#To represent 9, we should use IX instead of VIIII.
#To represent 40, we should use XL instead of XXXX.
#To represent 90, we should use XC instead of LXXXX.
#To represent 400, we should use CD instead of CCCC.
#To represent 900, we should use CM instead of DCCCC.

def integer_to_roman(num):
    # Fill this in.
    print(num)
    roman_value = ""
    roman_list = [
        1000,900,500,400,
        100,90,50,40,
        10,9,5,4,1]

    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    i = 0
    while num > 0:
        for _ in range(num//roman_list[i]):
            roman_value+=syb[i]
            num -= roman_list[i]

        i+=1

    return roman_value

print("Decimal to Roman 10-3")
print("<-----------------START--------------<")
print(integer_to_roman(1000))
# M
print(integer_to_roman(48))
# XLVIII
print(integer_to_roman(444))
# CDXLIV
print("<-----------------END--------------<")


#10/4/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a list of strings, find the longest
# common prefix between all strings.

def longest_common_prefix(strs):
    # Fill this in.
    print(strs)
    shortest = strs[0]
    solution = ""
    flag = True

    for i in range(1,len(strs)):
        if len(strs[i]) < len(shortest):
            shortest = strs[i]
            index = i

    count = 0
    while count < len(shortest):
        for word in strs:
            if word[count] != shortest[count]:
                flag = False
                break
        if flag:
            solution += shortest[count]
        else:
            break

        count +=1

    if len(solution) == 0:
        solution = "No common prefix found in this list"

    return solution

print("Longest Common Prefix 10-4")
print("<-----------------START--------------<")
print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# hell

print(longest_common_prefix(['daily', 'interview', 'pro']))
# ''
print("<-----------------END--------------<")



#10/5/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a list of numbers, and a target number n,
# find all unique combinations of a, b, c, d,
# such that a + b + c + d = n.


def fourSum(nums, target):
    # Fill this in.
    print(nums, target)

print("4 Sum 10-5")
print("<-----------------START--------------<")
print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])
print("<-----------------END--------------<")

#10/6/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a number n, generate all possible
# combinations of n well-formed brackets.

def generate_brackets(n):
    #Fill this in.
    print(n)

print("Generate Brackets 10-6")
print("<-----------------START--------------<")
print(generate_brackets(1))
# ['()']

print(generate_brackets(3))
# ['((()))', '(()())', '()(())', '()()()', '(())()']
print("<-----------------END--------------<")

#10/7/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a sorted list of size n,
# with m unique elements (thus m < n),
# modify the list such that the first m unique
# elements in the list will be sorted,
# ignoring the rest of the list.
# Your solution should have a space complexity of O(1).
# Instead of returning the list
# (since you are just modifying the original list),
# you should return what m is.

def remove_dups(nums):
    # Fill this in.
    print()
    if len(nums)>0:
        prev = nums[0]
        unique_count =1
    else:
        return "The list is empty"

    i =1
    while i < len(nums):
        if nums[i] == prev:
            nums.pop(i)
            i-=1

        else:
            unique_count+=1
            prev = nums[i]
        i+=1

    return unique_count

print("Remove Duplicates From Sorted List 10-7")
print("<-----------------START--------------<")
nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)
# 1
# [1]
print("<-----------------END--------------<")




# 10/8/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a list of numbers and a target number,
# find all possible unique subsets of the
# list of numbers that sum up to the target number.
# The numbers will all be positive numbers.

def sum_combinations(nums, target):
    # Fill this in.
    print()

print("Unique Sum Combinations 10-8")
print("<-----------------START--------------<")
print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
print("<-----------------END--------------<")



#10/9/20
#Given a sorted list with duplicates,
# and a target number n,
# find the range in which the number exists
# (represented as a tuple (low, high),
# both inclusive. If the number does not
# exist in the list, return (-1, -1)).

def find_num(nums, target):
    # Fill this in.
    print()

print("Range Searching in a Sorted List 10-9")
print("<-----------------START--------------<")
print(find_num([1, 1, 3, 5, 7], 1))
# (0, 1)

print(find_num([1, 2, 3, 4], 5))
# (-1, -1)
print("<-----------------END--------------<")

#10/10/20
#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a binary tree, find the minimum depth of the binary tree.
# The minimum depth is the shortest distance from the root to a leaf.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def min_depth_bst(root):
    # Fill this in.
    print()

n3 = Node(3, None, Node(4))
n2 = Node(2, Node(3))
n1 = Node(1, n2, n3)

#     1
#    / \
#   2   3
#        \
#         4
print("Minimum Depth of Binary Tree 10-10")
print("<-----------------START--------------<")
print(min_depth_bst(n1))
# 2
print("<-----------------END--------------<")

#10/11/20
#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Given a binary tree, and a target number,
# find if there is a path from the root to
# any leaf that sums up to the target.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def target_sum_bst(root, target):
    # Fill this in.
    print()

#      1
#    /   \
#   2     3
#    \     \
#     6     4
n6 = Node(6)
n4 = Node(4)
n3 = Node(3, None, n4)
n2 = Node(2, None, n6)
n1 = Node(1, n2, n3)

print("Target Sum from Root to Leaf 10-11")
print("<-----------------START--------------<")
print(target_sum_bst(n1, 9))
# True
# Path from 1 -> 2 -> 6
print("<-----------------END--------------<")

#10/12/20
#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#A majority element is an element that appears
# more than half the time. Given a list
# with a majority element, find the majority element.

def majority_element(nums):
    # Fill this in.
    print()

print("Majority Element 10-12")
print("<-----------------START--------------<")
print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3
print("<-----------------END--------------<")

#10/13/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given an integer, find the number of 1 bits it has.

def one_bits(num):
    # Fill this in.
    print(num)
    count = 0
    bit_stream = bin(num)

    for c in bit_stream:
        if c == '1':
            count +=1

    return count

print("Number of 1 bits 10-13")
print("<-----------------START--------------<")
print(one_bits(23))
# 4
# 23 = 0b10111
print("<-----------------END--------------<")

#10/14/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a list of positive numbers,
# find the largest possible set such
# that no elements are adjacent numbers of each other.

def maxNonAdjacentSum(nums):
    # Fill this in.
    print()

print("Maximum Non Adjacent Sum 10-14")
print("<-----------------START--------------<")
print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)
print("<-----------------END--------------<")

#10/15/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a matrix that is organized such that the
# numbers will always be sorted left to right,
# and the first number of each row will always
# be greater than the last element of the last
# row (mat[i][0] > mat[i - 1][-1]), search for
# a specific value in the matrix and return
# whether it exists.

def searchMatrix(mat, value):
    # Fill this in.
    print(value)

    for r in mat:
        print(r)

    status = False


    for i in range(len(mat)):
        print(i+1)
        if mat[i][0] == value:
            status = True
            break

        if mat[i][0] > value:
            if i > 0:
                for n in mat[i-1]:
                    if n == value:
                        status = True
                        break
            else:
                break

    return status




mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]


print("Searching a Matrix 10-15")
print("<-----------------START--------------<")
print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
print("<-----------------END--------------<")

#10/16/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a list of unique numbers,
# generate all possible subsets without duplicates.
# This includes the empty set as well.

def generateAllSubsets(nums):
    # Fill this in.
    print(nums)

print("Generate all Subsets 10-16")
print("<-----------------START--------------<")
print(generateAllSubsets([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
print("<-----------------END--------------<")



#10/17/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a binary tree, flatten the binary tree
# using inorder traversal. Instead of creating
# a new list, reuse the nodes, where the
# list is represented by following each right child.
# As such the root should always be the first element
# in the list so you do not need to return anything
# in the implementation, just rearrange the nodes
# such that following the right child will give us the list.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"

def flatten_bst(root):
    # Fill this in.
    print()

n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  /     /
# 5     4

flatten_bst(n1)
print("Flatten Binary Tree 10-17")
print("<-----------------START--------------<")
print(n1)
print("<-----------------END--------------<")
# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4




#10/18/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#A number can be constructed by a path
# from the root to a leaf. Given a binary tree,
# sum all the numbers that can be constructed from the root to all leaves.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def bst_numbers_sum(root, num=0):
    # Fill this in.
    print()

n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5

print("Root to Leaf Numbers Summed 10-18")
print("<-----------------START--------------<")
print(bst_numbers_sum(n1))
# 262
# Explanation: 124 + 125 + 13 = 262
print("<-----------------END--------------<")


#10/19/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a node in a connected directional graph, create a copy of it.

class Node:
    def __init__(self, value, adj=None):
        self.value = value
        self.adj = adj

        # Variable to help print graph
        self._print_visited = set()
        if self.adj is None:
            self.adj = []

    # Able to print graph
    def __repr__(self):
        if self in self._print_visited:
            return ''
        else:
            self._print_visited.add(self)
            final_str = ''
            for n in self.adj:
                final_str += f'{n}\n'

        self._print_visited.remove(self)
        return final_str + f'({self.value}, ({[n.value for n in self.adj]}))'


def deep_copy_graph(graph_node, visited=None):
    # Fill this in.
    print()

n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2)
n1 = Node(1, [n5])
n5.adj = [n3]
n4.adj = [n3, n2]
n2.adj = [n4]
graph_copy = deep_copy_graph(n1)
print("Deep Copy Graph 10-19")
print("<-----------------START--------------<")
print(graph_copy)
# (2, ([4]))
# (4, ([3, 2]))
# (3, ([4]))
# (5, ([3]))
# (1, ([5]))
print("<-----------------END--------------<")



#10/20/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#LRU cache is a cache data structure that has limited space,
# and once there are more items in the cache than available space,
# it will preempt the least recently used item.
# What counts as recently used is any item a key has
# 'get' or 'put' called on it.

#Implement an LRU cache class with the 2 functions
# 'put' and 'get'. 'put' should place a value mapped
# to a certain key, and preempt items if needed.
# 'get' should return the value for a given
# key if it exists in the cache,
# and return None if it doesn't exist.

class LRUCache:
    def __init__(self, space):
        # Fill this in.
        print()

    def get(self, key):
        # Fill this in.
        print()

    def put(self, key, value):
        # Fill this in.
        print()

cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print("LRU Cache 10-20")
print("<-----------------START--------------<")
print(cache.get(3))
# 3
print(cache.get(2))
# None

cache.put(2, 2)

print(cache.get(4))
# None (pre-empted by 2)
print(cache.get(3))
# 3
print("<-----------------END--------------<")


#10/21/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Find all words that are concatenations of a list.

#Input:
#["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

#Output:
#['techlead', 'catsdog']

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        # Fill this in.
        print()

input = ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

print("Concatenated Words 10-21")
print("<-----------------START--------------<")
print(Solution().findAllConcatenatedWordsInADict(input))
print("<-----------------END--------------<")

#Note: This question is classified as "hard."
#HINT: Start with a brute-force solution.


#10/22/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Find the k-th largest number in a sequence of unsorted numbers.
#Can you do this in linear time?

def findKthLargest(arr, k):
    # Fill this in.
    print(arr,k)
    largest = arr[0]
    i = 1

    while i < k:
        if arr[i]> largest:
            largest = arr[i]
        i+=1

    return largest

print("Find the K-th Largest Number 10-22")
print("<-----------------START--------------<")
print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))
# 7
print("<-----------------END--------------<")


#10/23/20
#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a set of words,
# find all words that are concatenations
# of other words in the set.

class Solution(object):
    def findAllConcatenatedWords(self, words):
        # Fill this in.
        print(words)

input = ['rat', 'cat', 'cats', 'dog', 'catsdog', 'dogcat', 'dogcatrat']
print("Word Concatenation 10-23")
print("<-----------------START--------------<")
print(Solution().findAllConcatenatedWords(input))
# ['catsdog', 'dogcat', 'dogcatrat']
print("<-----------------END--------------<")

#10/24/20
#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Find the maximum number of connected colors in a grid.
# Can you solve this both recursively and iteratively?

class Grid:
    def __init__(self, grid):
        self.grid = grid

    def max_connected_colors(self):
        # Fill this in.
        print()

grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 0]]

print("Connected Colors in a Grid 10-24")
print("<-----------------START--------------<")
print(Grid(grid).max_connected_colors())
# 7
print("<-----------------END--------------<")


#10/25/20
#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#Implement auto-completion.
# Given a large set of words (for instance 1,000,000 words)
# and then a single word prefix, find all words that it can complete to.
#Can you solve this optimally
# (in linear time with regards to the result set)?

class Solution:
    def build(self,word_list):
        # Fill this in.
        self.word_list = word_list


    def autocomplete(self, word):
        # Fill this in.
        word_list = self.word_list
        print(word_list)
        print(word)
        flag = False
        result = []


        for w in word_list:
            for i in range(len(word)):
                if word[i] != w[i]:
                    flag = True
                    break
            if not flag:
                result.append(w)
            else:
                flag = False

        return result
s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])

print("Autocompletion 10-25")
print("<-----------------START--------------<")
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']
print("<-----------------END--------------<")

#10/26/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#A criminal is constructing a ransom note.
# In order to disguise his handwriting,
# he is cutting out letters from a magazine.

#Given a magazine of letters and the note he wants to write,
# determine whether he can construct the word.
# Can you do this in linear time?

class Solution(object):
    def canSpell(self, magazine, note):
        # Fill this in.
        print(magazine,note)
        status = True
        my_dict = {}

        for letter in magazine:
            my_dict[letter] = 1

        for l in note:
            if l not in my_dict:
                status = False
                break

        return status

print("Ransom Note 10-26")
print("<-----------------START--------------<")
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
print("<-----------------END--------------<")


#10/27/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a list of points and a number k,
# find the k closest points to the origin.

def findClosestPointsOrigin(points, k):
    # Fill this in.
    print(points,k)
    origin_point = []
    solution =[]
    og_point = points[0]

    for i in range(len(points)):
        temp = (int((og_point[0]+og_point[1])/2) -
                int((points[i][0] + points[i][1])/2))
        origin_point.append(abs(temp))


    largest = origin_point[0]
    i = 0
    while i < k:
        closest = origin_point[0]
        index = 0

        for x in range(1,len(origin_point)):

            if origin_point[x] <= closest:
                closest = origin_point[x]
                index = x
            if largest < origin_point[x]:
                largest = origin_point[x]

        origin_point[index] = largest
        solution.append(points[index])
        i+=1

    return solution

print("Closest Points to Orgin 10-27")
print("<-----------------START--------------<")
print (findClosestPointsOrigin([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
# [[-1, -1], [1, 1], [2, 2]]
print("<-----------------END--------------<")


#10/28/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given two binary trees that are duplicates of one another,
# and given a node in one tree, find that correponding node
# in the second tree.

#For instance, in the tree below, we're looking for Node #4.

#For this problem, you can assume that:
#- There can be duplicate values in the tree
# (so comparing node1.value == node2.value isn't going to work).

#Can you solve this both recursively and iteratively?

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findNode(a, b, node):
    # Fill this in.
    print()
#  1
# / \
#2   3
#   / \
#  4*  5
a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.right.left = Node(4)
a.right.right = Node(5)

b = Node(1)
b.left = Node(2)
b.right = Node(3)
b.right.left = Node(4)
b.right.right = Node(5)

print("Clone Trees 10-28")
print("<-----------------START--------------<")
print(findNode(a, b, a.right.left))
# 4
print("<-----------------END--------------<")

#10/29/20
#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#A Perfect Number is a positive integer that is equal
# to the sum of all its positive divisors except itself.

#For instance,
#28 = 1 + 2 + 4 + 7 + 14

#Write a function to determine if a number is a perfect number.

class Solution(object):
    def checkPerfectNumber(self, num):
        # Fill this in.
        print(num)
        div_list = []
        div_list.append(1)

        i = 2
        while i<num:
            if num % i == 0:
                div_list.append(i)
            i+=1

        total = 0
        for n in div_list:
            total += n

        return(total == num)

print("Perfect Number 10-29")
print("<-----------------START--------------<")
print(Solution().checkPerfectNumber(28))
# True
# 28 = 1 + 2 + 4 + 7 + 14
print("<-----------------END--------------<")



#10/30/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a number like 159,
# add the digits repeatedly until you get a single number.

#For instance, 1 + 5 + 9 = 15.
#1 + 5 = 6.

#So the answer is 6.

class Solution(object):
    # Fill this in.
    def addDigits(self,num):
        print(num)

        while num > 10:
            temp = 0
            for c in str(num):
                temp += int(c)
            num = temp

        return num

print("Add Digits 10-30")
print("<-----------------START--------------<")
print(Solution().addDigits(159))
# 1 + 5 + 9 = 15
# 1 + 5 = 6
# 6
print("<-----------------END--------------<")

#10/31/20
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given an array of size n,
# and all values in the array are in the range 1 to n,
# find all the duplicates.

class Solution(object):
    def findDuplicates(self, nums):
        # Fill this in.
        print(nums)
        solution = []
        my_dic = {}

        for n in nums:
            if n not in my_dic:
                my_dic[n] = 1
            else:
                my_dic[n] += 1


        for x,y in my_dic.items():
            if y>1:
                solution.append(x)

        return solution

print("Find Duplicates 10-31")
print("<-----------------START--------------<")
print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
# [2, 3]
print("<-----------------END--------------<")



#11/1/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a tree, the leaves form a certain order from left to right.
# Two trees are considered "leaf-similar" if their
# leaf orderings are the same.

#For instance, the following two trees are considered
# leaf-similar because their leaves are [2, 1]:
#    3
#   / \
#  5   1
#   \
#    2
#    7
#   / \
#  2   1
#   \
#    2
#Our job is to determine, given two trees, whether they are "leaf similar."

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        # Fill this in.
        print()

#    3
#   / \
#  5   1
#   \
#    2

t1 = Node(3)
t1.left = Node(5)
t1.right = Node(1)
t1.left.left = Node(6)
t1.left.right = Node(2)

#    7
#   / \
#  2   1
#   \
#    2
t2 = Node(7)
t2.left = Node(2)
t2.right = Node(1)
t2.left.left = Node(6)
t2.left.right = Node(2)

print("Leaf-Similar Trees 11-1")
print("<-----------------START--------------<")
print(Solution().leafSimilar(t1, t2))
# True
print("<-----------------END--------------<")



#11/2/20
#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given an array of heights, determine whether the
# array forms a "mountain" pattern.
# A mountain pattern goes up and then down.

#Like
#  /\
# /  \
#/    \
class Solution(object):
    def validMountainArray(self, arr):
        # Fill this in.
        print(arr)
        status = True

        for i in range(int(len(arr)/2)):
            if arr[i] != arr[len(arr)-1-i]:
                status = False
                break

        return status


print("Valid Mountain Array 11-2")
print("<-----------------START--------------<")
print(Solution().validMountainArray([1, 2, 3, 2, 1]))
# True

print(Solution().validMountainArray([1, 2, 3]))
# False
print("<-----------------END--------------<")


#11/3/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a sorted array, convert it into a binary search tree.

#Can you do this both recursively and iteratively?

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
      return f"{self.val}, ({self.left}, {self.right})"

class Solution(object):
    def sortedArrayToBST(self, nums):
        # Fill this in.
        print(nums)

n = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
print("Array to Binary Search Tree 11-3")
print("<-----------------START--------------<")
print(n)
# 0, (-3, (-10, (None, None), None), 9, (5, (None, None), None))
print("<-----------------END--------------<")


#11/4/20
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given an array of numbers,
# determine whether it can be partitioned into 3 arrays of equal sums.

#For instance,
#[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1] can be partitioned into:
#[0, 2, 1], [-6, 6, -7, 9, 1], [2, 0, 1] all of which sum to 3.

class Solution(object):
    def canThreePartsEqualSum(self, A):
        # Fill this in.0
        print(A)

print("Three Equal Sums 11-4")
print("<-----------------START--------------<")
print(Solution().canThreePartsEqualSum(
    [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
# True
print("<-----------------END--------------<")


#11/5/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a linked list,
# remove all duplicate values from the linked list.

#For instance, given 1 -> 2 -> 3 -> 3 -> 4,
# then we wish to return the linked list 1 -> 2 -> 4.

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + " " + str(self.next)

class Solution(object):
    def deleteDuplicates(self, node):
        # Fill this in.
        prev = node
        node = node.next
        while node:
            if prev.val == node.val:
                prev.next = node.next
            else:
                prev = node

            node = node.next

n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print("Remove duplicates from Linked List 11-5")
print("<-----------------START--------------<")
print(n)
# 1 2 3 3 4
Solution().deleteDuplicates(n)
print(n)
# 1 2 4
print("<-----------------END--------------<")


#11/6/20
#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given an array containing only positive integers,
# return if you can pick two integers from the array
# which cuts the array into three pieces such that
# the sum of elements in all pieces is equal.

#Example 1:
#Input: array = [2, 4, 5, 3, 3, 9, 2, 2, 2]

#Output: true
#Explanation: choosing
# the number 5 and 9 results in three
# pieces [2, 4], [3, 3] and [2, 2, 2]. Sum = 6.

#Example 2:
#Input: array =[1, 1, 1, 1],

#Output: false

class Solution(object):
    def canPick2(self, arr):
        # Fill this in.
        print(arr)


print("Array of Equal Parts 11-6")
print("<-----------------START--------------<")
print(Solution().canPick2([2, 4, 5, 3, 3, 9, 2, 2, 2]))
# True

print(Solution().canPick2([1, 2, 3, 4, 5]))
# False
print("<-----------------END--------------<")