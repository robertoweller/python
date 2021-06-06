def ziP(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

l_A = [1, 2, 3]
l_B = ["A", "B", "C"]

myList = ziP(l_A, l_B)

print(list(myList))
