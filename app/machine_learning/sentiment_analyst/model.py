import numpy as np
from scipy.optimize import minimize
from scipy.special import softmax,logsumexp

class SoftmaxRegressor():
    def __init__(self,alpha=0.01):
        self.alpha = alpha

    def fit(self,X,y):
        n_samples , n_features = X.shape
        n_classes = y.shape[1]

        def loss_and_gradient(params):

            W = params[:n_features * n_classes].reshape(
                n_features, n_classes
            )

            b = params[n_features * n_classes:]

            logits = X @ W + b
            log_probs = logits - logsumexp(
                logits, axis=1, keepdims=True
            )

            probs = np.exp(log_probs)

            loss = -np.sum(y * log_probs) / n_samples
            loss += self.alpha * np.sum(W ** 2) / 2

            error = (probs - y) / n_samples

            grad_W = X.T @ error + self.alpha * W
            grad_b = np.sum(error, axis=0)

            gradient = np.concatenate([
                np.asarray(grad_W).ravel(),
                grad_b
            ])

            return loss, gradient

        initial = np.zeros(
            n_features * n_classes + n_classes
        )

        result = minimize(
            loss_and_gradient,
            initial,
            jac=True,
            method='L-BFGS-B'
        )

        self.W = result.x[:n_features * n_classes].reshape(
            n_features, n_classes
        )

        self.b = result.x[n_features * n_classes:]

        return self

    def predict_proba(self, X):

        logits = X @ self.W + self.b

        return softmax(logits, axis=1)
