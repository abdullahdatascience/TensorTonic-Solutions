def matrix_trace(A):
    n = len(A)        # number of rows
    trace_sum = 0
    
    for i in range(n):
        trace_sum += A[i][i]
    
    return trace_sum