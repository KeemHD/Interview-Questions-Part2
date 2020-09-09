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
print("<-----------------START--------------<PPPPPPPPPPPPPPPPPPP")
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
    return 0

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

print("Sum of Squares 9-4")
print("<-----------------START--------------<")
print(square_sum(13))
# Min sum is 32 + 22
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
