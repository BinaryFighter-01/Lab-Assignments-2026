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