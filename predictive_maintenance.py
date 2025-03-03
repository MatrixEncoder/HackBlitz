import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input

class PredictiveMaintenance:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.create_model()

    def create_model(self):
        model = tf.keras.Sequential([
            Input(shape=(10,)),  # Adjust input shape
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def load_data(self, data_path):
        data = np.load(data_path)  # Load your dataset
        X = data['features']
        y = data['labels']
        return train_test_split(X, y, test_size=0.2)

    def train(self, data_path, epochs=10):
        X_train, X_test, y_train, y_test = self.load_data(data_path)
        self.model.fit(X_train, y_train, epochs=epochs, validation_data=(X_test, y_test))
        self.model.save(self.model_path)

    def predict(self, data):
        return self.model.predict(data)

# Example usage
if __name__ == '__main__':
    pm = PredictiveMaintenance('path/to/model')
    pm.train('actual/path/to/your/data.npz')  # Replace with the actual path to your dataset
    sample_data = np.array([[0, 1, 0, 1]])  # Replace with actual data
    prediction = pm.predict(sample_data)
    print('Prediction:', prediction)
