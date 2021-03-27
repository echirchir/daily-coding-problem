
def main(values):
    """
    
    step 1: loop through the list of integers
    step 2: remove current value from temp list of original values
    step 3: multiply remaining items and add product to new list
    step 4: return new list of products
    
    """
    
    products_list = list()
    
    for value in values:
        items = values[::]
        items.remove(value)
        product = 1
        for item in items:
            product *= item
        products_list.append(product)
    return products_list


if __name__ == "__main__":
    print(main([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
    print(main([3, 2, 1]))  # [2, 3, 6]
    print(main([3, 2, 1, 3]))  # [6, 9, 18, 6]
