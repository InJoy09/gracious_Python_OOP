
text = "Lorem Ipsum is simply dummy text"
len_text = len(text)
max_len = 12

res = text if len_text <= max_len else text[:max_len] + '...'

print(res)