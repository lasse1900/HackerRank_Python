
# https://www.youtube.com/watch?v=W1z1KqLVHqE

def find_missing_int(lst):
    # space complexity O(n)
    missing_int_set = set(lst)
    # space complexity O(n)
    int_set = {i for i in range(1, len(lst) + 2)}
    missing_int = int_set.difference(missing_int_set)
    iterator = iter(missing_int)
    return next(iterator)

if __name__ == '__main__':
    missing_int = [1,2,6,7,9,3,4,10,8]
    # [1,2,6,7,9,3,4,10,8,5]
    print(find_missing_int(missing_int))

