from collections import defaultdict

encoded_text = "0A0B2C3A2A4A6B"

i = 0
index_string = defaultdict(int)
index = 1
prefix_str = ""
while i < len(encoded_text):

    while encoded_text[i].isdigit():
        prefix_str += encoded_text[i]
        i += 1

    prefix = int(prefix_str)
    if prefix not in index_string:
        index_string[index] = encoded_text[i]
    else:
        index_string[index] = index_string[prefix] + encoded_text[i]

    i += 1
    index += 1
    prefix_str = ""


print("{:<10} {:<10} {:<10}".format("Index", "String", "Output"))
for k, v in index_string.items():
    print("{:<10} {:<10} {:<10}".format(k, v, v))


decoded_text = ""
for v, k in index_string.items():
    decoded_text += k

print(decoded_text)
