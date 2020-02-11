import numpy as np

def sigmoid(Z):
	#Sigmoid activation function
	A = 1/(1+np.exp(-Z))
	cache = Z
	return A, cache

def zero_pad(X, pad):
    '''
    Pad with zeros all images of the dataset X. The padding is applied to the height and width of an image 
    Argument:
    X : numpy array of shape (m, n_H, n_W, n_C) representing a batch of m images
    pad : integer, amount of padding around each image on vertical and horizontal dimensions
    Returns:
    padded : padded image of shape (m, n_H + 2*pad, n_W + 2*pad, n_C)
	'''
    
    padded = np.pad(X,((0, 0), (pad, pad), (pad, pad), (0, 0)), 'constant', constant_values=(0, 0))
    
    return padded

def conv_single_step(a_slice_prev, W, b):
    '''
    Apply one filter defined by parameters W on a single slice (a_slice_prev) of the output activation 
    of the previous layer.
    Arguments:
    a_slice_prev : slice of input data of shape (f, f, n_C_prev)
    W : Weight parameters contained in a window - matrix of shape (f, f, n_C_prev)
    b : Bias parameters contained in a window - matrix of shape (1, 1, 1)
    Returns:
    Z : The result of convolution
    '''
   
    # Multiplication of a_slice_prev and W.
    s = np.multiply(a_slice_prev, W)
    # Sum of all entries of s.
    Z = np.sum(s)
    # Add bias b to Z.
    Z = Z + b

    return Z

def forward_convolution(A_prev, W, b, hparameters):
    '''
    Implements the forward propagation 
    Arguments:
    A_prev : output activations of the previous layer, numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    W : Weights, numpy array of shape (f, f, n_C_prev, n_C)
    b : Biases, numpy array of shape (1, 1, 1, n_C)
    hparameters : python dictionary with "stride" and "pad" 
    Returns:
    Z : conv output, numpy array of shape (m, n_H, n_W, n_C)
    cache : cache for the backward_conv()
    '''
    
    # Retrieve dimensions from A_prev's shape   
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    
    # Retrieve dimensions from W's shape 
    (f, f, n_C_prev, n_C) = W.shape
    
    # Retrieve information from "hparameters" 
    stride = hparameters["stride"]
    pad = hparameters["pad"]
    
    # Compute the dimensions of the CONV output volume using the formula given above. 
    # Hint: use int() to apply the 'floor' operation. 
    n_H = int(1+(n_H_prev + 2 * pad - f)/stride)
    n_W = int(1+(n_W_prev + 2 * pad - f)/stride)
    
    # Initialize the output volume Z with zeros. 
    Z = np.zeros((m, n_H, n_W, n_C))
    
    # Create A_prev_pad by padding A_prev
    A_prev_pad = zero_pad(A_prev, pad)
    
    for i in range(m):               # loop over the batch of training examples
        a_prev_pad = A_prev_pad[i]               # Select ith training example's padded activation
        for h in range(n_H):           # loop over vertical axis of the output volume
            # Find the vertical start and end of the current "slice" 
            vert_start = stride * h
            vert_end = vert_start + f
            
            for w in range(n_W):       # loop over horizontal axis of the output volume
                # Find the horizontal start and end of the current "slice" 
                horiz_start = stride * w
                horiz_end = horiz_start + f
                
                for c in range(n_C):   # loop over channels (= #filters) of the output volume
                                        
                    # Use the corners to define the (3D) slice of a_prev_pad (See Hint above the cell). 
                    a_slice_prev = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :]
                    
                    # Convolve the (3D) slice with the correct filter W and bias b, to get back one output neuron. 
                    weights = W[:,:,:,c]
                    biases = b[:,:,:,c]
                    Z[i, h, w, c] = conv_single_step(a_slice_prev, weights, biases)
                                        
    
    
    # Check output shape is correct
    assert(Z.shape == (m, n_H, n_W, n_C))
    
    # Save information in "cache" for the backprop
    cache = (A_prev, W, b, hparameters)
    
    return Z, cache

def pool_forward(A_prev, hparameters, mode = "max"):
    '''
    Implements the forward pass of the pooling layer
    
    Arguments:
    A_prev : Input data, numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    hparameters : python dictionary containing "f" and "stride"
    mode : the pooling mode you would like to use, defined as a string ("max" or "average")
    
    Returns:
    A : output of the pool layer, a numpy array of shape (m, n_H, n_W, n_C)
    cache : cache used in the backward pass of the pooling layer, contains the input and hparameters 
    '''
    
    # Retrieve dimensions from the input shape
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    
    # Retrieve hyperparameters from "hparameters"
    f = hparameters["f"]
    stride = hparameters["stride"]
    
    # Define the dimensions of the output
    n_H = int(1 + (n_H_prev - f) / stride)
    n_W = int(1 + (n_W_prev - f) / stride)
    n_C = n_C_prev
    
    # Initialize output matrix A
    A = np.zeros((m, n_H, n_W, n_C))              
    
    
    for i in range(m):                         # loop over the training examples
        for h in range(n_H):                     # loop on the vertical axis of the output volume
            # Find the vertical start and end of the current "slice" 
            vert_start = stride * h
            vert_end = vert_start + f
            
            for w in range(n_H):                 # loop on the horizontal axis of the output volume
                # Find the vertical start and end of the current "slice" 
                horiz_start = stride * w
                horiz_end = horiz_start + f
                
                for c in range (n_C):            # loop over the channels of the output volume
                    
                    # Use the corners to define the current slice on the ith training example of A_prev, channel c. 
                    a_prev_slice = A_prev[i,vert_start:vert_end, horiz_start:horiz_end, c]
                    
                    # Compute the pooling operation on the slice. 
                    # Use an if statement to differentiate the modes. 
                    # Use np.max and np.mean.
                    if mode == "max":
                        A[i, h, w, c] = np.max(a_prev_slice)
                    elif mode == "average":
                        A[i, h, w, c] = np.mean(a_prev_slice)
    
    
    
    # Store the input and hparameters in "cache" for pool_backward()
    cache = (A_prev, hparameters)
    
    # Check output shape is correct
    assert(A.shape == (m, n_H, n_W, n_C))
    
    return A, cache

def backward_convolution(dZ, cache):
    '''
    Implement the backward propagation for a convolution function
    
    Arguments:
    dZ : gradient of the cost with respect to the output of the conv layer (Z), numpy array of shape (m, n_H, n_W, n_C)
    cache : cache of values needed for the backward_convolution()
    
    Returns:
    dA_prev : gradient of the cost with respect to the input of the conv layer (A_prev),
               numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    dW : gradient of the cost with respect to the weights of the conv layer (W)
          numpy array of shape (f, f, n_C_prev, n_C)
    db : gradient of the cost with respect to the biases of the conv layer (b)
          numpy array of shape (1, 1, 1, n_C)
    '''
    
    
    # Retrieve information from "cache"
    (A_prev, W, b, hparameters) = cache
    
    # Retrieve dimensions from A_prev's shape
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    
    # Retrieve dimensions from W's shape
    (f, f, n_C_prev, n_C) = W.shape
    
    # Retrieve information from "hparameters"
    stride = hparameters['stride']
    pad = hparameters['pad']
    
    # Retrieve dimensions from dZ's shape
    (m, n_H, n_W, n_C) = dZ.shape
    
    # Initialize dA_prev, dW, db with the correct shapes
    dA_prev = np.zeros_like(A_prev)                           
    dW = np.zeros_like(W)
    db = np.zeros_like(b)

    # Pad A_prev and dA_prev
    A_prev_pad = zero_pad(A_prev, pad)
    dA_prev_pad = zero_pad(dA_prev, pad)
    
    for i in range(m):                       # loop over the training examples
        
        # select ith training example from A_prev_pad and dA_prev_pad
        a_prev_pad = A_prev_pad[i, :, :, :]
        da_prev_pad = dA_prev_pad[i, :, :, :]
        
        for h in range(n_H):                   # loop over vertical axis of the output volume
            for w in range(n_W):               # loop over horizontal axis of the output volume
                for c in range(n_C):           # loop over the channels of the output volume
                    
                    # Find the corners of the current "slice"
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                    
                    # Use the corners to define the slice from a_prev_pad
                    a_slice = a_prev_pad[vert_start: vert_end
                                         , horiz_start: horiz_end]

                    # Update gradients for the window and the filter's parameters using the code formulas given above
                    da_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :] += W[:, :, :, c] * dZ[i, h, w, c]
                    dW[:,:,:,c] += a_slice * dZ[i, h, w, c]
                    db[:,:,:,c] += dZ[i, h, w, c]
                    
        # Set the ith training example's dA_prev to the unpaded da_prev_pad (Hint: use X[pad:-pad, pad:-pad, :])
        dA_prev[i, :, :, :] = dA_prev_pad[i, pad: -pad, pad: -pad, :]
    
    
    # Check output shape is correct
    assert(dA_prev.shape == (m, n_H_prev, n_W_prev, n_C_prev))
    
    return dA_prev, dW, db

def create_mask_from_window(x):
    '''
    Creates a mask from an input matrix x, to identify the max entry of x.
    
    Arguments:
    x : Array of shape (f, f)
    
    Returns:
    mask : Array of the same shape as window, contains a True at the position corresponding to the max entry of x.
    '''
    
     
    mask = (x == np.max(x))
    
    
    return mask

def distribute_value(dz, shape):
    '''
    Distributes the input value in the matrix of dimension shape
    
    Arguments:
    dz : input scalar
    shape : the shape (n_H, n_W) of the output matrix for which we want to distribute the value of dz
    
    Returns:
    a : Array of size (n_H, n_W) for which we distributed the value of dz
    '''
    
    
    # Retrieve dimensions from shape 
    (n_H, n_W) = shape
    
    # Compute the value to distribute on the matrix 
    average = np.ones([n_H, n_W]) / (n_H * n_W)
    
    # Create a matrix where every entry is the "average" value 
    a = dz * average
    
    
    return a

def pool_backward(dA, cache, mode = "max"):
    '''
    Implements the backward pass of the pooling layer
    
    Arguments:
    dA : gradient of cost with respect to the output of the pooling layer, same shape as A
    cache : cache output from the forward pass of the pooling layer, contains the layer's input and hparameters 
    mode : the pooling mode you would like to use, defined as a string ("max" or "average")
    
    Returns:
    dA_prev : gradient of cost with respect to the input of the pooling layer, same shape as A_prev
    '''
    
    
    
    # Retrieve information from cache 
    (A_prev, hparameters) = cache
    
    # Retrieve hyperparameters from "hparameters" 
    stride = hparameters['stride']
    f = hparameters['f']
    
    # Retrieve dimensions from A_prev's shape and dA's shape 
    m, n_H_prev, n_W_prev, n_C_prev = A_prev.shape
    m, n_H, n_W, n_C = dA.shape
    
    # Initialize dA_prev with zeros 
    dA_prev = np.zeros_like(A_prev)
    
    for i in range(m):                       # loop over the training examples
        
        # select training example from A_prev 
        a_prev = A_prev[i, :, :, :]
        
        for h in range(n_H):                   # loop on the vertical axis
            for w in range(n_W):               # loop on the horizontal axis
                for c in range(n_C):           # loop over the channels (depth)
                    
                    # Find the corners of the current "slice"
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                    
                    # Compute the backward propagation in both modes.
                    if mode == "max":
                        
                        # Use the corners and "c" to define the current slice from a_prev 
                        a_prev_slice = a_prev[vert_start: vert_end, horiz_start: horiz_end, c]
                        # Create the mask from a_prev_slice 
                        mask = create_mask_from_window(a_prev_slice)
                        # Set dA_prev to be dA_prev + (the mask multiplied by the correct entry of dA) 
                        dA_prev[i, vert_start: vert_end, horiz_start: horiz_end, c] += mask * dA[i, h, w, c]
                        
                    elif mode == "average":
                        
                        # Get the value a from dA 
                        da = dA[i, h, w, c]
                        # Define the shape of the filter as fxf 
                        shape = (f, f)
                        # Distribute it to get the correct slice of dA_prev. i.e. Add the distributed value of da. 
                        dA_prev[i, vert_start: vert_end, horiz_start: horiz_end, c] += distribute_value(da, shape)
                        
    
    
    # Ckeck output shape is correct
    assert(dA_prev.shape == A_prev.shape)
    
    return dA_prev
