'''
This algorithm finds set of items that give the largest product possible given:
C: Capacity of container
S: Array containing sizes of items
V: Array containing values of items

This algorithm works by recursively trying each possible combination of products, and returning the maximum.
This maximum is stored in "ReturnArray", which is printed at the end of the wrapper function.
The returned value by maxProductWrapper() represents the product of those respective items.

Note: The algorithm assumes each item can only be used once. It also assumes that if the knapsack cannot be filled completely,
it will still return the highest possible value. 
'''

def maxProduct(C,S,V,Array):
    # If capacity is negative (we have run out of space), return invalid possibility.
    if C < 0:
        Array[C] = [1]
    # If S no longer has items (we have run out of items), return 1. 
    if not S:
        Array[C] = [1]
    # If current value has not been calculated, calculate it.
    if Array[C] == None:
        currentMax = 0
        newArray = []
        # This loops through all items in S and recursively tries adding each item to the knapsack.
        for num, item in enumerate(S):
            # Obtain value of respective item.
            value = V[num]
            # Calculate new capacity with item.
            tempC = C - item
            # Create new arrays without item.
            tempS = S[:num] + S[(num + 1):]
            tempV = V[:num] + V[(num + 1):]
            # Calculates product with item.
            childArray = maxProduct(tempC,tempS,tempV,Array)
            product = childArray[0] * value
            if product > currentMax:
                currentMax = product
                newArray = childArray + [item]
                newArray[0] *= value
        Array[C] = newArray
    return Array[C]

def maxProductWrapper(C,S,V):
    Array = [None] * (C+1)
    Array[0] = [1]
    return maxProduct(C,S,V,Array)

C = 12
S = [3,7,4,6,5]
V = [5,12,6,9,7]

print(maxProductWrapper(C,S,V))
