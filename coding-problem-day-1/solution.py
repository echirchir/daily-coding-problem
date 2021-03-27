
def main(values, key):
    """
    
    step 1: loop through the list (outer loop)
    step 2: loop through the list again (inner loop)
    step 3: check if value in outer loop matches second value in inner loop (don't add number to itself)
    step 4: if values from different indices add to key, return True
    step 5: if they do not add to key, return False
    
    Question: Should the list contain duplicate values at different indices? e.g [10, 15, 8, 10]?
    
    """
    for _ in values:
        for __ in values:
            if _ == __:
                continue
            elif _ + __ == key:
                return True
            else:
                continue
    return False


if __name__ == "__main__":
    print(main([9, 15, 8, 7], 17))  # True
    print(main([9, 15, 8, 7], 20))  # False
    print(main([9, 15, 11, 7], 18))  # True
    print(main([10, 15, 8, 7], 21))  # False
    print(main([10, 15, 8, 10], 20))  # False
