def flatten_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item


nested_list = [1, 2, [3, 4, [5, [6]], 7], 8, 9, 10]
flat_generator = flatten_generator(nested_list)
flat_list = list(flat_generator)
print(flat_list)
