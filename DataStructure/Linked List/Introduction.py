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
    def __init__(self,value):
        self.value = value
        self.next  = None

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

print(node1.next) # Next Adderess (means Node 2 Adderess)
# <__main__.Node object at 0x000001D571338CD0>

print(node1.next.value) # Next value 
# 10

print(node1.next.next.next.value)
# 20


# Create Singly list Class 
# becouse, if the abave object is 10000000... so i have to write every times 
# alternate used is singly linked list or Method For easy for me to solve question
 
# Methods

# START at HEAD
#      │
#      ▼
#   [ 10 ] ──► [ 25 ] ──► [ 47 ] ──► [ 26 ] ──► [ 89 ] ──► NULL
#   STOP HERE — no more nodes!

# 1) Append

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class singly_Linked_List:   # just create a Linked list the all 1st node is None
    def __init__(self):
        self.head = None  # 1 st none node  

#   1) if SLL can be empty
#   2) if SLL is not empty

    def append(self,value):
        new_node = Node(value)  #  create a box
        if self.head == None:   #   list is empty
            self.head = new_node    # yes → attach to head
        else:
            currunt = self.head     # no → start walking
            while currunt.next is not None:
                currunt= currunt.next    # move forward
            currunt.next = new_node     # attach at end

    def traversal(self):
        if self.head is None:
            print("SLL is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()



sll = singly_Linked_List()
sll.append(10)
sll.append(47)
sll.append(25)
sll.traversal()

# What Happens in Memory

# sll.append(10)
# HEAD
#  │
#  ▼
# ┌──────┬──────┐
# │  10  │ NULL │
# └──────┴──────┘

# sll.append(25)
# HEAD
#  │
#  ▼
# ┌──────┬──────┐     ┌──────┬──────┐
# │  10  │  ──────►   │  25  │ NULL │
# └──────┴──────┘     └──────┴──────┘

# sll.append(47)
# HEAD
#  │
#  ▼
# ┌──────┬──────┐     ┌──────┬──────┐     ┌──────┬──────┐
# │  10  │  ──────►   │  25  │  ──────►   │  47  │ NULL │
# └──────┴──────┘     └──────┴──────┘     └──────┴──────┘

# 2) Traversal

# Traversal = VISITING every node ONE BY ONE         
#            from HEAD → to → NULL  


# current = head

# ─────────────────────────────────
# current
#   │
#   ▼
# ┌──────┬──────┐
# │  10  │  ──► │    → print(10)  →  current = current.next
# └──────┴──────┘
# ─────────────────────────────────
#          current
#            │
#            ▼
#         ┌──────┬──────┐
#         │  25  │  ──► │   → print(25) →  current = current.next
#         └──────┴──────┘
# ─────────────────────────────────
#                    current
#                      │
#                      ▼
#                   ┌──────┬──────┐
#                   │  47  │  ──► │  → print(47)  →  current = current.next
#                   └──────┴──────┘
# ─────────────────────────────────
#                              current
#                                │
#                                ▼
#                             ┌──────┬──────┐
#                             │  89  │ NULL │  → print(89) →  current = NULL
#                             └──────┴──────┘
# ─────────────────────────────────
# current = NULL → while loop STOPS