# def generate_hashtag(s):
#     for i in range(len(s)):
#         if s[i] == ' ':
#             s[i+1].upper()
#     s = s.replace(' ', '')
#     print(s)
#
# print(generate_hashtag(" Hello there thanks for trying my Kata"))

string = 'he wer ewe tew'
array = []
string = string.replace(' ', '*')
for i in string.split():
    print(string[i])
print(string)

# Пока сложно