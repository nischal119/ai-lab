import numpy as np


class GaussianNaiveBayes:
    def fit(self, X_train, y_train):
        self.classes = np.unique(y_train)
        self.class_prior = {}
        self.mean = {}
        self.var = {}

        for c in self.classes:
            X_c = X_train[y_train == c]
            self.class_prior[c] = len(X_c) / len(X_train)
            self.mean[c] = np.mean(X_c, axis=0)
            self.var[c] = np.var(X_c, axis=0)

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            posteriors = []
            for c in self.classes:
                prior = self.class_prior[c]
                likelihood = np.prod(self._pdf(c, x))
                posterior = prior * likelihood
                posteriors.append(posterior)
            predictions.append(self.classes[np.argmax(posteriors)])
        return predictions

    def _pdf(self, class_label, x):
        mean = self.mean[class_label]
        var = self.var[class_label]
        numerator = np.exp(-((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator


# Example usage:
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([0, 0, 1, 1])
X_test = np.array([[1.5, 2.5], [3.5, 4.5]])

model = GaussianNaiveBayes()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)  # Output: [0, 1]
