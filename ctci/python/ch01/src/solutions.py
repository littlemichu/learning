from sets import Set

# QUESTION 1.1
def is_unique(s):
    charMap = {}
    for i in range(len(s)):
        if charMap.has_key(s[i]):
            return False
        else:
            charMap[s[i]] = True
    return True

# Not allowed additional data structures
def is_unique2(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# QUESTION 1.2
def reverse(list_obj):
    for i in range(len(list_obj)/2):
        temp = list_obj[i]
        list_obj[i] = list_obj[len(list_obj) - 1 - i]
        list_obj[len(list_obj) - 1 - i] = temp
    return list_obj

# QUESTION 1.3
def is_permutation(s1, s2):
    m1 = {}
    m2 = {}
    for char in s1:
        if m1.has_key(char):
            m1[char] += 1
        else:
            m1[char] = 1

    for char in s2:
        if m2.has_key(char):
            m2[char] += 1
        else:
            m2[char] = 1

    for key in m1.keys():
        if key not in m2 or m1[key] != m2[key]:
            return False

    return True

# QUESTION 1.4
def replace(arr, length):
    from_i = length -  1
    to_i = len(arr) - 1
    while from_i != to_i:
        if arr[from_i] == ' ':
            arr[to_i] = '0'
            arr[to_i - 1] = '2'
            arr[to_i - 2] = '%'
            to_i -= 3
        else:
            arr[to_i] = arr[from_i]
            to_i -= 1
        from_i -= 1
    return arr

# QUESTION 1.5
def compress(s):
    compressed = []
    curr = s[0]
    counter = 1
    for i in range(len(s) - 1):
        if curr == s[i + 1]:
            counter += 1
        else:
            compressed.append(curr)
            compressed.append(str(counter))
            curr = s[i + 1]
            counter = 1

    compressed.append(curr)
    compressed.append(str(counter))
    if len(compressed) < len(s):
        return "".join(compressed)
    else:
        return s

# QUESTION 1.6
def rotate(img, n):
    rotated = [[0 for x in range(n)] for x in range(n)]
    for row in range(n):
        for col in range(n):
            rotated[col][n - 1 - row] = img[row][col]
    return rotated

# QUEStION 1.7
def zero(matrix, n, m):
    zeroed = [row[:] for row in matrix]
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 0:
                for col2 in range(m):
                    zeroed[row][col2] = 0
                for row2 in range(n):
                    zeroed[row2][col] = 0
    return zeroed

def zero2(matrix, n, m):
    rows = Set()
    cols = Set()
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row in rows:
        matrix[row] = [0 for col in range(m)]

    for col in cols:
        for row in range(n):
            matrix[row][col] = 0

    return matrix
