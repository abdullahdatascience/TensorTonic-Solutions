import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    y = np.asarray(y)
    N = y.shape[0]

    # Determine number of classes
    if num_classes is None:
        K = np.max(y) + 1
    else:
        K = num_classes
        if np.max(y) >= K:
            raise ValueError("Label value exceeds num_classes")

    # Create zero matrix
    one_hot_matrix = np.zeros((N, K), dtype=float)

    # Vectorized index assignment
    one_hot_matrix[np.arange(N), y] = 1.0

    return one_hot_matrix
