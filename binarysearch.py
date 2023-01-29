# Algoritmo:

# 1 Sort the array in ascending order.
# 2 Set the low index to the first element of the array and the high index to the last element.
# 3 Set the middle index to the average of the low and high indices.
# 4 If the element at the middle index is the target element, return the middle index.
# 5 If the target element is less than the element at the middle index, set the high index to the middle index – 1.
# 6 If the target element is greater than the element at the middle index, set the low index to the middle index + 1.
# 7 Repeat steps 3-6 until the element is found or it is clear that the element is not present in the array.