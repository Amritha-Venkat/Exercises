# def lengthOfLongestSubstring(word):
#     n = len(word)
#     longest = 0
#     for i in range(n):
#         seen = set()
#         for j in range(i, n):
#             if word[j] in seen: break
#             seen.add(word[j])
#         longest = max(len(seen), longest)
#     return longest
#
# print(lengthOfLongestSubstring("hello"))

#longest sequence of characters that is same in both strings starting from 0 index

# upstream_seq = "hello"
# downstream_seq = "hellmyfriend"
#
# print(upstream_seq, downstream_seq)
# mh = 0
# pos_count = 0
# seq = ""
# position =""
# longest_hom=""
# for i in range(len(upstream_seq)):
#     pos_count += 1
#     if upstream_seq[i] == downstream_seq[i]:
#         mh += 1
#         seq += upstream_seq[i]
#         position = pos_count
#         longest_hom = mh
#
#     else:
#         mh = 0
#         break
#
# print(position , longest_hom, seq)


upstream_seq = "hello"
downstream_seq = "myhellfriend"
def all_substrings(string):
    n = len(string)
    for i in range(n):
        for j in range(i,n):
            print(string[i:j + 1])

# print(all_substrings('ABCA'))
print(all_substrings(upstream_seq) )
print(all_substrings(downstream_seq))
print(max(all_substrings(upstream_seq) & all_substrings(downstream_seq), key=len))