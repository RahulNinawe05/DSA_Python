"""
A Hash Table is a data structure that stores data in key → value form.

How it works:
    You give a key (like a name).
    A hash function converts that key into a number (index).
    The value is stored at that index (called a bucket).
    Because the index is direct, search is very fast (average O(1)).

Example:-

    Key: "Rahul"
    Value: "9876543210"
    Hash function decides where to store Rahul’s number.
"""
phone = {
    "Rahul": 9876543210,
    "Amit": 9123456789
}

print(phone["Rahul"])  # fast lookup