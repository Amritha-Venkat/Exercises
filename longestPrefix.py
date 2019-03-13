def longestCommonPrefix(strs: 'List[str]') -> 'str':
    if len(strs) == 0:
        prefix = ''
    else:
        prefix = strs[0]
    for s in strs:
        while not s.startswith(prefix) and len(prefix) > 0:
            prefix = prefix[:-1]
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))




