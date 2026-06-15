# What is a Linked List?
# A Linked List is a linear data structure where elements (called nodes) are stored in sequence,
# but unlike arrays, the elements are not stored in contiguous memory locations.
# Each node holds two things — the actual data and a pointer (reference) to the next node in the sequence.
# The list starts at a node called the Head and ends at a node whose next pointer is None.

#     • data — the value stored
#     • next — a pointer/reference to the next node

# HEAD
#  │
#  ▼
# ┌──────┬──────┐     ┌──────┬──────┐     ┌──────┬──────┐     ┌──────┬──────┐     ┌──────┬──────┐
# │ DATA │ NEXT │     │ DATA │ NEXT │     │ DATA │ NEXT │     │ DATA │ NEXT │     │ DATA │ NEXT │
# │  10  │  ──────►   │  25  │  ──────►   │  47  │  ──────►   │  26  │  ──────►   │  89  │ NULL │
# └──────┴──────┘     └──────┴──────┘     └──────┴──────┘     └──────┴──────┘     └──────┴──────┘
#   Node 1               Node 2               Node 3               Node 4               Node 5

# don't index value

# HEAD always points to the FIRST node
# NEXT of the LAST node is always NULL
# You can only travel LEFT ──► RIGHT (in singly linked list)
# You CANNOT go backwards

class Node:
    def __init__(self, value):
        self.value = value  # Just Create a node
        self.next = None   # defoult next value is "None"


# Object of Class Node
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

# just show what is a next node
node1.next = node2
node2.next = node3
node3.next = node4

print(node1)        # Adderess of Node 1
# Adderess like - <__main__.Node object at 0x000001D5710A7230>

print(node1.value)  # Value of Node 1
# 5

print(node1.next)  # Next Adderess (means Node 2 Adderess)
# <__main__.Node object at 0x000001D571338CD0>

print(node1.next.value)  # Next value
# 10

print(node1.next.next.next.value)
# 20


# ************Create Singly list Class***************

# You only Forword Direction
# why create a method:- becouse, if the abave object is 10000000... so i have to write every times
# solve this problem is singly linked list or Method For easy for me to solve question


# Methods:-  1) Append  tc-O(n)
# ---------------------------------------------------------

# this is class to help to create a linked list as well as
# store the data in linked list.
# # just create a class node, in this node are create a linked list
# the store the value  & next value but in every node the next value
# is None
# the starting node is point to head
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# crate a linked list the head is None

class singly_Linked_List:
    def __init__(self):
        self.head = None

# always insert node at the end
# in this append method create a new node but they have 2 condition
#   1) if SLL can be empty:- craete a box of linked list but in linked list are point as a none/head
#   mens linked list is empty after that the currunt box are head

#   2) if SLL is not empt:- the currunt linked list is a None they are move to forword direction
#   if the find out None after that they have store at the end

    def append(self, value):
        new_node = Node(value)  # create a box
        if self.head == None:  # list is empty
            self.head = new_node    # yes → attach to head
        else:
            currunt = self.head     # no → start walking
            while currunt.next is not None:
                currunt = currunt.next    # move forward
            currunt.next = new_node     # attach at end

# Methods:-  2) Traversal   tc - O(n)
# ---------------------------------------------------------

# Traversal = VISITING every node ONE BY ONE
#            from HEAD → to → NULL

# 1. If the linked list is empty (head is None),
#    print "SLL is Empty".
# 2. Otherwise:
#    - Start from head
#    - Print data of each node
#    - Move to next node
#    - Stop when current becomes None

    def traversal(self):
        # Case 1: Linked List is empty

        if self.head is None:
            print("SLL is Empty")

        # Case 2: Linked List is not empty
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print() # for new line

# Method: 3) insert_at  tc - O(n) | sc - O(1)
# ---------------------------------------------------------

# This method inserts a new node at a given position
# in a Singly Linked List.
#
# Parameters:
# value    → data to be inserted in the new node
# position → index where the new node should be inserted
#
# Example:
# List: 10 -> 20 -> 30
# insert_at(15, 1)
# Result: 10 -> 15 -> 20 -> 30

    def insert_at(self,value,position):

        # Create a new node with given value
        new_node = Node(value)

        # CASE 1: Insert at position 0 (beginning of list)
        if position == 0:
            # Point new node to current head
            new_node.next = self.head

            # Move head to new node
            self.head = new_node

         # CASE 2: Insert at any position other than 0
        else:
            # Start traversal from head
            currunt = self.head

            # This will store the previous node
            prev_node = None

            # Counter to track current position
            cout = 0

            # Traverse list until required position is reached
            while currunt is not None and cout < position:
                # Move prev_node to current node
                prev_node = currunt

                # Move current to next node
                currunt = currunt.next

                # Increase position counter
                cout += 1

            # Link previous node to new node
            prev_node.next = new_node

            # Link new node to current node
            new_node.next = currunt

# Method: 4) Delete  
# ---------------------------------------------------------
    def delete(self,value):
        temp = self.head

        if temp.next is not None:
            if temp.value == value:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.value == value:
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    prev("Node not found")


sll = singly_Linked_List()
sll.append(10)
sll.append(47)
sll.append(25)
sll.insert_at(1000,1)
sll.traversal()
