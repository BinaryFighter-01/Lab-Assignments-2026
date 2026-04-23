"""Design RNN or its variant including LSTM or GRU a) Select a suitable time series dataset.
Example – predict sentiments based on product reviews b) Apply for prediction"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# a) Load dataset (text → numbers already)
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=5000)

# Pad sequences (same length)
X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=100)
X_test = tf.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=100)

# b) Build LSTM model
model = Sequential([
    Embedding(5000, 32),   # word embedding
    LSTM(32),              # RNN variant
    Dense(1, activation='sigmoid')  # output (0/1 sentiment)
])

# Compile
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=3, verbose=0)

# c) Prediction & Evaluation
acc = model.evaluate(X_test, y_test, verbose=0)[1]
print(f"Accuracy: {acc:.4f}")

# Predict sample
pred = model.predict(X_test[:3])
print("Predictions:", pred)



"""**Short Explanation of RNN (LSTM) Sentiment Analysis Code**

1. **Dataset Loading**
   The IMDB dataset is loaded, which contains movie reviews already converted into numerical sequences. Only the top 5000 most frequent words are used to limit vocabulary size.

2. **Preprocessing**
   The sequences are padded to a fixed length of 100 so that all inputs have the same size, which is required for training the model.

3. **Model Design (LSTM)**
   A Sequential model is created with:

* **Embedding layer** to convert word indices into dense vectors
* **LSTM layer** to capture sequence dependencies in the text
* **Dense layer (sigmoid)** to classify sentiment as positive or negative

4. **Compilation**
   The model uses the Adam optimizer, binary crossentropy loss for classification, and accuracy as the evaluation metric.

5. **Training**
   The model is trained on the training dataset for 3 epochs.

6. **Evaluation and Prediction**
   The trained model is evaluated on test data to get accuracy. It also predicts sentiments for a few sample inputs.

**Conclusion:**
The LSTM model learns patterns in text sequences and successfully predicts sentiment (positive/negative) based on input reviews.
"""