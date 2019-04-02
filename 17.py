from num2words import num2words

all_nums = ""
for i in range(1, 1001):
    all_nums += num2words(i)

only_chars = ""
for char in all_nums:
    if char.isalpha():
        only_chars += char

print(len(only_chars))