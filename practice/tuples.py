

def stringcases(arg):
    s = str(arg)
    low = s.lower()
    up = s.upper()
    title = s.title()
    rev = s[::-1]
    t = (low, up, title, rev)
    print(t)


def combo(*lst):
    newlist = []
    a,b = lst
    for index, item in (enumerate(a)):
        newlist.append((a[index], b[index]))
    print(newlist)

def combo2(*var):
    a,b = var
    list_1 = list(a)
    list_2 = list(b)
    return zip(list_1, list_2)
combo2([1, 2, 3], 'abc')
#combo('abc', 'def')
