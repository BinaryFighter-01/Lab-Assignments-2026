# Version 1

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample reviews
texts = [
    "good product",
    "bad quality",
    "excellent phone",
    "worst item",
    "nice service",
    "poor battery"
]

# Labels
# 1 = Positive
# 0 = Negative
labels = [1,0,1,0,1,0]

# Convert text to numbers
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(texts)

seq = tokenizer.texts_to_sequences(texts)

# Same length sequences
X = pad_sequences(seq, maxlen=3)

y = labels

# Build RNN model
model = Sequential([
    
    Embedding(input_dim=50, output_dim=8, input_length=3),

    SimpleRNN(8),

    Dense(1, activation='sigmoid')
])

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X, y, epochs=100, verbose=0)

# Prediction
test = tokenizer.texts_to_sequences(
    ["good service"]
)

test = pad_sequences(test, maxlen=3)

pred = model.predict(test)

print("Prediction =", pred[0][0])




# Version 2

import networkx as nx
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer

# ---- Data ----
texts = [
    "this class is amazing",
    "very boring lecture",
    "excellent teaching",
    "i hate this subject",
    "great explanation",
    "worst class ever",
    "very interesting topic",
    "not good teaching"
]

# ---- Tokenize ----
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# ---- Build Graph (adjacent words only) ----
G = nx.Graph()
for seq in sequences:
    for i in range(len(seq) - 1):
        w1 = tokenizer.index_word[seq[i]]
        w2 = tokenizer.index_word[seq[i+1]]
        G.add_edge(w1, w2)

# ---- Optional: color sentiment words ----
pos_words = {"good", "great", "excellent", "amazing", "interesting"}
neg_words = {"bad", "worst", "hate", "boring"}

colors = []
for node in G.nodes():
    if node in pos_words:
        colors.append("green")
    elif node in neg_words:
        colors.append("red")
    else:
        colors.append("lightblue")

# ---- Draw Graph ----
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, k=2, seed=42)  # better spacing

nx.draw(G, pos,
        with_labels=True,
        node_color=colors,
        node_size=900,
        font_size=10,
        edge_color="black",
        width=1.2)

plt.title("Word Network Graph (Sentiment)")
plt.show()
