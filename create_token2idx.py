token2idx = {}
curr_idx = 0

docs = list()
docs.append("this is a simple document")
docs.append("this is a second document")
docs.append("the third short document")

# initialize word/integer pairs:
for doc in docs:
    for token in doc.split(" "):
        if token not in token2idx:
            token2idx[token] = curr_idx
            curr_idx += 1

# display token/integer pairs
for token in token2idx.keys():
    print(f"token: {token:10} value: {token2idx[token]:4}")

print()

# create an integer-based counterpart
int_docs = []
for doc in docs:
    tokens = [token2idx[word] for word in doc.split(" ")]
    int_docs.append(tokens)

print("int_docs:", int_docs)
print()

# create integer-to-token mapping
idx2token = {v: k for k,v in token2idx.items()}
for k,v in idx2token.items():
    print(f"key: {k:4} value: {v:10}")

