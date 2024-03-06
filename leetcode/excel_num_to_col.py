alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_to_title_recursive(n):
    """
    :type columnNumber: int
    :rtype: str
    """

    if n == 0:
        return ""
    
    q = (n - 1) // 26
    r = (n - 1) % 26

    return convert_to_title_recursive(q) + alphabet[r]

def convert_to_title_iterative(n):

    res = ""
    while n:
        q = (n - 1) // 26
        r = (n - 1) % 26

        res += alphabet[q]
        n = q

    return res + alphabet[r]
