banana = {'name': 'banana', 'price': 10}
apple = {'name': 'apple', 'price': 2.75}
kiwi = {'name': 'kiwi', 'price': 3.15}
orange = {'name': 'orange', 'price': 12}
grape = {'name': 'grape', 'price': 0.12}

cart = [banana, kiwi, apple, orange, banana, grape, kiwi, grape]

def remove_duplicates(l: list) -> list:
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)
    return nl

def swap(l: list, a, b) -> list:
    aidx = l.index(a)
    bidx = l.index(b)
    l[aidx] = b
    l[bidx] = a
    return l

def sort_list(fn, l: list, x=0) -> list:
    if x <= 0:
        l = remove_duplicates(l)
    c = len(l)-1
    n = x+1
    if n <= c:
        current_item = l[x]
        next_item = l[n]
        swappable = fn(current_item, next_item)
        if swappable:
            l = swap(l, current_item, next_item)
            return sort_list(fn, l)
        return sort_list(fn, l, n)
    return l

def comp_by_key_l(key: str, a, b) -> bool:
    return a[key] >= b[key]

def comp_by_key_h(key: str, a, b) -> bool:
    return a[key] <= b[key]

cart_by_lowest_price = sort_list(lambda a,b: comp_by_key_l('price', a, b), cart)

cart_by_highest_price = sort_list(lambda a,b: comp_by_key_h('price', a, b), cart)

cart_by_az = sort_list(lambda a,b: comp_by_key_l('name', a, b), cart)

cart_by_za = sort_list(lambda a,b: comp_by_key_h('name', a, b), cart)

print(cart)

print(cart_by_lowest_price)
print(cart_by_highest_price)

print(cart_by_az)
print(cart_by_za)