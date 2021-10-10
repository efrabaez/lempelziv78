from collections import defaultdict

text = "ABBCBCABABCAABCAAB"
string_index = defaultdict(int)
index = 1
i = 0
current_string = ""
prefix = 0
while i < len(text):
    current_string += text[i]
    if current_string not in string_index:
        string_index[current_string] = [index, str(prefix) + text[i]]
        current_string = ""
        index += 1
        prefix = 0
    else:
        prefix = string_index[current_string][0]
    i += 1


encoded_text = ""
for v, k in string_index.items():
    encoded_text += k[1]

print(encoded_text)
