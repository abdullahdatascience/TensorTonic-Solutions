import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column (or 1D array) using mean or median.
    Fully handles 1D, 2D, integer inputs, all-NaN cases, and returns a float copy.
    """
    X_arr = np.asarray(X, dtype=float).copy()
    
    # 1D case
    if X_arr.ndim == 1:
        valid_mask = ~np.isnan(X_arr)
        if np.any(valid_mask):
            stat = np.mean(X_arr[valid_mask]) if strategy=='mean' else np.median(X_arr[valid_mask])
            X_arr[~valid_mask] = stat
        else:
            X_arr[:] = 0.0
        return X_arr
    
    # 2D case
    elif X_arr.ndim == 2:
        n_rows, n_cols = X_arr.shape
        for j in range(n_cols):
            col = X_arr[:, j]
            valid_mask = ~np.isnan(col)
            
            if np.any(valid_mask):
                stat = np.mean(col[valid_mask]) if strategy=='mean' else np.median(col[valid_mask])
                col[~valid_mask] = stat
            else:
                col[:] = 0.0
        return X_arr
    else:
        raise ValueError("Input must be 1D or 2D array")
