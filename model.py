# read data
with open('input.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    
print("length of dataset in characters: ", len(data))

# unique characters in the dataset
chars = sorted(list(set(data)))
vocab_size = len(chars)
print(f'total {vocab_size} characters', ''.join(chars))

# tokenize the characters
stoi = {char:index for index,char in enumerate(chars)}
itos = {index:char for index,char in enumerate(chars)}
encode = lambda string: [stoi[char] for char in string]         # encoder
decode = lambda list: ''.join([itos[index] for index in list])  # decoder

print(encode('Hello World!'))
print(decode(encode('Hello World!')))

"""
# tiktoken by OpenAI
import tiktoken
enc = tiktoken.get_encoder('gpt2')
# print(enc.n_vocab) # 50257

enc.encode('Hello World!') # [15496, 995]
"""

