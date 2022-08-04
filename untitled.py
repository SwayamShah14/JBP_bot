import markovify

# Get raw text as string.
with open("JP_tr.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence(tries=100))
