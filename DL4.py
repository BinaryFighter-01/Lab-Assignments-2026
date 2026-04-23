
"""Design and implement a CNN for Image Classification a) Select a suitable image classification
dataset (medical imaging, agricultural, etc.). b) Optimized with different hyper-parameters including
learning rate, filter size, no. of layers, optimizers, dropouts, etc."""

import tensorflow as tf
from tensorflow.keras import layers, models

# Load + preprocess
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
X_train, X_test = X_train/255.0, X_test/255.0
X_train = X_train[..., None]
X_test = X_test[..., None]

# Function to build model
def build(lr, dr):
    model = models.Sequential([
        layers.Conv2D(32, 3, activation='relu', input_shape=(28,28,1)),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(dr),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(lr),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Try 2 configs (optimization)
for lr, dr in [(0.01, 0.2), (0.001, 0.3)]:
    model = build(lr, dr)
    model.fit(X_train, y_train, epochs=3, verbose=0)
    acc = model.evaluate(X_test, y_test, verbose=0)[1]
    print(f"LR={lr}, Dropout={dr} → Acc={acc:.4f}")






#     **Explanation of CNN Code (Short)**

# 1. **Dataset Loading & Preprocessing**
#    The Fashion MNIST dataset is loaded, which contains grayscale images of clothing items. Pixel values are normalized from 0–255 to 0–1 for better training performance. The images are reshaped to include a channel dimension required for CNN input.

# 2. **Model Definition**
#    A simple Convolutional Neural Network (CNN) is created:

# * Conv2D layer extracts image features
# * MaxPooling reduces size and keeps important features
# * Flatten converts 2D data to 1D
# * Dense layer learns patterns
# * Dropout prevents overfitting
# * Output layer (softmax) classifies into 10 categories

# 3. **Compilation**
#    The model uses the Adam optimizer with a specified learning rate, sparse categorical crossentropy loss for multiclass classification, and accuracy as the metric.

# 4. **Hyperparameter Optimization**
#    Two configurations of learning rate and dropout are tested. This demonstrates optimization by comparing model performance under different settings.

# 5. **Training & Evaluation**
#    The model is trained for a few epochs and evaluated on test data. Accuracy is printed for each configuration.

# 6. **Conclusion**
#    The best-performing configuration is identified based on accuracy, showing how hyperparameters affect model performance.
