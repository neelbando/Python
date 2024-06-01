def find_longest_substring(s):
    st = 0
    m = 0
    d = {}

    for i, v in enumerate(s):
        if v in d:
            st = d[v] + 1
        else:
            m = max(m, i-st+1)

        d[v] = i

    return m

strx = 'abcabdcabb'
find_longest_substring(strx)