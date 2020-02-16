import numpy as np
import random
from tqdm import tqdm

def initialize_layers(layers):
    """
    Initialize the layer parameters
    
    Arguments:
    layers -- A list of element where each element defines the type of layer and the hyperparameters.
    
    Returns:
    new_layers -- The list of layers with the initialized values.
    """
    new_layers = []
    for i, layer in enumerate(layers):
        mode = layer['mode'] # 'fc', 'conv', 'pool'
        # Pooling layer
        if mode == 'pool': 
            new_layers.append(layer)
            continue
        # Fully Connected layer
        elif mode == 'fc':
            n_now = layer['n_now']
            n_prev = layer['n_prev']
            layer['W']=(np.random.rand(n_now, n_prev) - 0.5) * 0.2 # random sample in [-0.1, 0.1] 
            layer['b']=(np.random.rand(n_now,1) - 0.5) * 0.2
            layer['dW']=np.zeros_like(layer['W'])
            layer['db']=np.zeros_like(layer['b'])
        #Convolution layer
        elif mode == 'conv':
            f = layer['filters']
            n_C = layer['n_C']
            n_C_prev = layer['n_C_prev']
            layer['W']=(np.random.rand(f, f, n_C_prev, n_C) - 0.5) * 0.2 # random sample in [-0.1, 0.1] 
            layer['b']=(np.random.rand(1, 1, 1, n_C) - 0.5) * 0.2
            layer['dW']=np.zeros_like(layer['W'])
            layer['db']=np.zeros_like(layer['b'])
        else:
            print('Wrong layer in [{}]'.format(i))
        new_layers.append(layer)
            
    return new_layers

def sigmoid_activation(Z):
    '''
    Calculates the value of sigmoid functions 

    Arguments:
    Z -- A numeric value

    Returns:
    A -- The result of the sigmoid function calculation for the Z
    cache -- The initial value of Z
    '''
    # Sigmoid function
    A = 1/(1+np.exp(-Z))
    cache = Z
    return A, cache

def relu_activation(Z):
    '''
    Calculates the value of relu function 

    Arguments:
    Z -- A numeric value

    Returns:
    A -- The result of the sigmoid function calculation for the Z
    cache -- The initial value of Z
    '''
    # Relu function
    A = np.maximum(0,Z)
    cache = Z
    return A, cache

def softmax_activation(Z):
    '''
    Calculates the value of Softmax turn logits (numeric output of the last linear 
    layer of a multi-class classification neural network) into probabilities by taking 
    the exponents of each output and then normalize each number by the sum of those 
    exponents so the entire output vector adds up to one

    Arguments:
    Z -- A numeric value

    Returns:
    A -- The result of the sigmoid function calculation for the Z
    cache -- The initial value of Z
    '''
    # Softmax activation function
    n, m = Z.shape
    A = np.exp(Z)
    A_sum = np.sum(A, axis = 0)
    A_sum = A_sum.reshape(-1, m)
    A = A / A_sum
    cache = Z
    return A, cache

def zero_padding(X, pad):
    '''
    Pad with zeros all images of the dataset X. The padding is applied to the height and width of an image

    Arguments:
    X : numpy array of shape (m, n_H, n_W, n_C) representing a batch of m images
    pad : integer, amount of padding around each image on vertical and horizontal dimensions

    Returns:
    padded -- padded image of shape (m, n_H + 2*pad, n_W + 2*pad, n_C)
	'''
    
    padded = np.pad(X,((0, 0), (pad, pad), (pad, pad), (0, 0)), 'constant', constant_values=(0, 0))
    
    return padded

def forward_linear_activation(A_prev, layer, activation='relu'):
    '''
    Execute a linear forward activation based on the input activation type

    Arguments:
    A_prev -- The values of the previous layer
    layer -- they current layer with the hyperparameters
    activation -- the type of activation to execute on the layer

    Returns:
    A -- The results of the linear activation
    Z --  The results of the dot product of W and A_prev increased by b
    '''
    W = layer['W']
    b = layer['b']
    if activation=='sigmoid':
        Z, linear_cache=np.dot(W, A_prev)+b, (A_prev, W, b)
        A, activation_cache=sigmoid_activation(Z)
    elif activation=='relu':
        Z, linear_cache=np.dot(W, A_prev)+b, (A_prev, W, b)
        A, activation_cache=relu_activation(Z)
    else:
        Z = np.dot(W, A_prev)+b
        A = Z
    return A, Z


def forward_convolution(A_prev, layer):
    """
    Implements the forward propagation for a convolution function
    
    Arguments:
    A_prev -- output activations of the previous layer, numpy array of 
    shape (m, n_H_prev, n_W_prev, n_C_prev)
    layer -- a dictionary contains weights, bias, hyperparameters and 
    shape of data
        
    Returns:
    Z -- conv output, numpy array of shape (m, n_H, n_W, n_C)
    """
    # Retrieve information from layer
    W = layer['W']
    b = layer['b']
    stride = layer['stride']
    pad = layer['pad']
    
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    
    (f, f, n_C_prev, n_C) = W.shape
    
    n_H = 1 + int((n_H_prev + 2 * pad - f) / stride)
    n_W = 1 + int((n_W_prev + 2 * pad - f) / stride) 
    
    # Initialize the output volume Z with zeros
    Z = np.zeros((m, n_H, n_W, n_C))
    
    # Create A_prev_pad by padding A_prev
    if pad > 0:
        A_prev_pad = zero_padding(A_prev, pad)
    else:
        A_prev_pad = A_prev
    
    for i in range(m):                     # loop over the batch of training examples
        a_prev_pad = A_prev_pad[i]         # Select ith training example's padded activation
        for h in range(n_H):               # loop over vertical axis of the output volume
            for w in range(n_W):           # loop over horizontal axis of the output volume
                for c in range(n_C):       # loop over channels (= #filters) of the output volume
                    
                    # Find the corners of the current "slice" (≈4 lines)
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                    
                    # Use the corners to define the (3D) slice of a_prev_pad 
                    a_slice_prev = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :]
                  
                    # Convolve the (3D) slice with the correct filter W and bias b, to get back 
                    # one output neuron
                    Z[i, h, w, c] = np.sum(np.multiply(a_slice_prev, W[:, :, :, c])) + b[0, 0, 0, c]

    return Z

def forward_pooling(A_prev, hparameters, mode = "max"):
    '''
    Implements the forward pass of the pooling layer
    
    Arguments:
    A_prev -- Input data, numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    hparameters -- python dictionary containing "filters" and "stride"
    mode -- the pooling mode you would like to use, defined as a string ("max" or "average")
    
    Returns:
    A -- output of the pool layer, a numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache used in the backward pass of the pooling layer, contains the input and hparameters 
    '''
    
    # Retrieve dimensions from the input shape
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    
    f = hparameters["filters"]
    stride = hparameters["stride"]
    
    # Define the dimensions of the output
    n_H = int(1 + (n_H_prev - f) / stride)
    n_W = int(1 + (n_W_prev - f) / stride)
    n_C = n_C_prev
    
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
                    
                    # Use the corners to define the current slice on the ith training example of A_prev,
                    #  channel c. 
                    a_prev_slice = A_prev[i,vert_start:vert_end, horiz_start:horiz_end, c]
                    
                    # Compute the pooling operation on the slice. 
                    if mode == "max":
                        A[i, h, w, c] = np.max(a_prev_slice)
                    elif mode == "average":
                        A[i, h, w, c] = np.mean(a_prev_slice)
    
    
    
    # Store the input and hparameters in "cache" for backward_pooling()
    cache = (A_prev, hparameters)
    
    return A, cache

def forward_propogation(X, layers):
    '''
    Executes the forward propagation on the given layers

    Arguments:
    X -- An array containing the set of images
    layers -- An array of dictionaries where each dictionary represents a layer 
    and contains information about the layer and hyperparameters

    Returns:
    A --  The output of the last softmax layer which is a distribution of 
    posibilities for each possible outcome
    layers -- The layers with the calculated weights and biases
    shapes -- The output shapes of each layer
    '''
    m = X.shape[0]
    A = X
    flattened = False
    shapes = []
    #Iterate through all layers except the last one
    for layer in layers[:-1]:
        layer['A_prev'] = A

        #convolution layer
        if layer['mode'] == 'conv':
            Z = forward_convolution(A, layer)
            layer['Z'] = Z
            A, _ = relu_activation(Z)

        #pooling layer
        elif layer['mode'] == 'pool':
            layer['A_prev'] = A
            A, _ = forward_pooling(A, layer, mode = "average")

        #fully connected layer
        elif layer['mode'] == 'fc':
            if not flattened:
                flattened_A = (A.reshape(m,-1)).T # flatten
                layer['A_prev'] = flattened_A
                flattened = True
                A, Z = forward_linear_activation(flattened_A, layer, activation='relu')
                layer['Z'] = Z
            else:
                layer['A_prev'] = A
                A, Z = forward_linear_activation(A, layer, activation='relu')
                layer['Z'] = Z
        shapes.append((layer["mode"], A.shape))
            
    #Last fully connected softmax layer 
    layers[-1]['A_prev'] = A
    _, Z = forward_linear_activation(A, layers[-1], activation='none')
    layers[-1]['Z'] = Z
    A, _ = softmax_activation(Z)
    shapes.append(("fc", A.shape))

    return A, layers, shapes

def calculate_cost(AL, Y):
    '''
    Calculates the cost of the network

    Arguments:
    AL -- The predicted values
    Y -- The actual values

    Returns:
    cost -- The cost of the network 

    '''
    n, m = Y.shape
    cost = - np.sum(np.log(AL) * Y) / m
    cost=np.squeeze(cost)

    return cost  

def backward_convolution(dZ, layer):
    """
    Implement the backward propagation for a convolution function
    
    Arguments:
    dZ -- gradient of the cost with respect to the output of the conv layer (Z), 
    numpy array of shape (m, n_H, n_W, n_C)
    layer -- a dictionary contains weights, bias, hyperparameters and shape of data
    
    Returns:
    dA_prev -- gradient of the cost with respect to the input of the conv layer (A_prev),
               numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    dW -- gradient of the cost with respect to the weights of the conv layer (W)
          numpy array of shape (f, f, n_C_prev, n_C)
    db -- gradient of the cost with respect to the biases of the conv layer (b)
          numpy array of shape (1, 1, 1, n_C)
    """
    # Retrieve informations from layer
    A_prev = layer['A_prev']
    W = layer['W']
    b = layer['b']
    Z = layer['Z']
    stride = layer['stride']
    pad = layer['pad']
    
    # Retrieve dimensions from A_prev's shape
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    
    # Retrieve dimensions from W's shape
    (f, f, n_C_prev, n_C) = W.shape
    
    # Retrieve dimensions from dZ's shape
    (m, n_H, n_W, n_C) = dZ.shape
    
    # Initialize dA_prev, dW, db with the correct shapes
    dA_prev = np.zeros((m, n_H_prev, n_W_prev, n_C_prev))                           
    dW = np.zeros((f, f, n_C_prev, n_C))
    db = np.zeros((1, 1, 1, n_C))

    # Pad A_prev and dA_prev
    if pad > 0:
        A_prev_pad = zero_padding(A_prev, pad)
        dA_prev_pad = zero_padding(dA_prev, pad)
    else:
        A_prev_pad = A_prev
        dA_prev_pad = np.copy(dA_prev)

    for i in range(m):                   # loop over the training examples
        for h in range(n_H):             # loop over vertical axis of the output volume
            for w in range(n_W):         # loop over horizontal axis of the output volume
                for c in range(n_C):     # loop over the channels of the output volume
                    
                    # Find the corners of the current "slice"
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                    
                    # Use the corners to define the slice from a_prev_pad
                    a_slice = A_prev_pad[i, vert_start:vert_end, horiz_start:horiz_end, :]

                    # Update gradients for the window and the filter's parameters using the code formulas
                    dA_prev_pad[i, vert_start:vert_end, horiz_start:horiz_end, :] += W[:,:,:,c] * dZ[i, h, w, c]
                    dW[:,:,:,c] += dZ[i, h, w, c] * a_slice
                    db[:,:,:,c] += dZ[i, h, w, c]
                    
                    
        # Set the ith training example's dA_prev to the unpaded da_prev_pad
        if pad == 0:
            dA_prev[i, :, :, :] = dA_prev_pad[i, :, :, :]
        else:
            dA_prev[i, :, :, :] = dA_prev_pad[i, pad:-pad, pad:-pad, :]
    
    return dA_prev, dW, db



def create_mask_from_matrix(x):
    '''
    Creates a mask from an input matrix x, to identify the max entry of x.
    
    Arguments:
    x : Array of shape (f, f)
    
    Returns:
    mask : Array of the same shape as window, contains a True at the position 
    corresponding to the max entry of x.
    '''
    
    mask = (x == np.max(x))
    
    return mask

def distribute_values_into_matrix(dz, shape):
    '''
    Distributes the input value in the matrix of dimension shape
    
    Arguments:
    dz : input scalar
    shape : the shape (n_H, n_W) of the output matrix for which we want to
    distribute the value of dz
    
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

def backward_pooling(dA, layer, mode = "max"):
    """
    Implements the backward pass of the pooling layer
    
    Arguments:
    dA -- gradient of cost with respect to the output of the pooling layer, same shape as A
    layer -- the pooling layer, contains the layer's input and hparameters 
    mode -- the pooling mode you would like to use, defined as a string ("max" or "average")
    
    Returns:
    dA_prev -- gradient of cost with respect to the input of the pooling layer, same shape as A_prev
    """
    # Retrieve information from layer
    A_prev = layer['A_prev']
    stride = layer['stride']
    f = layer['filters']
    
    # Retrieve dimensions from A_prev's shape and dA's shape
    m, n_H_prev, n_W_prev, n_C_prev = A_prev.shape
    m, n_H, n_W, n_C = dA.shape
    
    # Initialize dA_prev with zeros
    dA_prev = np.zeros_like(A_prev)
    
    for i in range(m):                         # loop over the training examples
        # select training example from A_prev
        a_prev = A_prev[i]
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
                        a_prev_slice = a_prev[vert_start:vert_end, horiz_start:horiz_end, c]
                        # Create the mask from a_prev_slice
                        mask = create_mask_from_matrix(a_prev_slice)
                        # Set dA_prev to be dA_prev + (the mask multiplied by the correct entry of dA)
                        dA_prev[i, vert_start: vert_end, horiz_start: horiz_end, c] += mask * dA[i, h, w, c]
                        
                    elif mode == "average":
                        # Get the value a from dA
                        da = dA[i, h, w, c]
                        # Define the shape of the filter as fxf
                        shape = (f, f)
                        # Distribute it to get the correct slice of dA_prev. i.e. Add the distributed value of da.
                        dA_prev[i, vert_start: vert_end, horiz_start: horiz_end, c] += distribute_values_into_matrix(da, shape)

    return dA_prev

def backward_sigmoid(dA, cache):
    '''
    Calculates the backward propagation of sigmoid activation
    function

    Arguments:
    dA -- gradient of cost with respect to the input of the 
    conv layer
    cache -- The cached output of the convolution

    Returns:
    dZ -- gradient of cost with respect to the output of the
    conv layer
    '''
    # Backpropogation of sigmoid activation function
    Z = cache
    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)
    return dZ

def backward_relu(dA, cache):
    '''
    Calculates the backward propagation of RELU activation
    function

    Arguments:
    dA -- gradient of cost with respect to the input of the 
    conv layer
    cache -- The cached output of the convolution

    Returns:
    dZ -- gradient of cost with respect to the output of the
    conv layer
    '''
    # Backpropogation of Relu activation function 
    Z = cache
    dZ = np.array(dA, copy=True) # just converting dz to a correct object.
    dZ[Z < 0] = 0
    return dZ

def backward_softmax(A, Y):
    '''
    Calculates the backward propagation of sigmoid activation
    function

    Arguments:
    A -- The input of the fully connected layer
    Y -- The cached output of the fully connected layer

    Returns:
    dZ -- gradient of cost with respect to the output of the
    fully connected layer
    '''
    # Backpropogation of softmax activation function
    m = A.shape[1]
    dZ = (A - Y) / np.float(m)
    return dZ

def backward_linear_activation(dA, layer, activation):
    '''
    Calculates the backward propagation of a linear activation
    function

    Arguments:
    dA -- The gradient of cost with respect to the input of the 
    conv layer
    layer -- Dictionary containing the layer parameters
    activation -- The type of the activation

    Returns:
    dA_prev -- The gradient of cost with respect to the input of 
    the previous layer
    dW -- The gradient of the cost with respect to the weight
    db -- The gradient of the cost with respect to the biases
    '''
    # Backward propagatIon module - linear activation backward
    A_prev = layer['A_prev']
    W = layer['W']
    b = layer['b']
    Z = layer['Z']
    if activation=='relu':
        dZ=backward_relu(dA, Z)
    elif activation=='sigmoid':
        dZ=backward_sigmoid(dA, Z)
    else:
        dZ = dA 
    n, m = dA.shape
    dA_prev=np.dot(W.T, dZ)
    dW = np.dot(dZ, A_prev.T)
    db = np.sum(dZ, axis = 1).reshape(n,1)
    
    return dA_prev, dW, db

def backward_propagation(AL, Y, layers):
    '''
    Executes the backward propagation for all layers

    Arguments:
    AL -- The input of the fully connected layer
    Y -- The cached output of the fully connected layer
    layers -- A list of all layers with the respective parameters

    Returns:
    layers -- A list of all layers with the respective updated parameters
    '''
    m = Y.shape[1]

    # Last fully connected softmax layer
    dZ = backward_softmax(AL, Y)
    dA_prev, dW, db = backward_linear_activation(dZ, layers[-1], 'none')
    layers[-1]['dW'] = dW
    layers[-1]['db'] = db

    for layer in reversed(layers[:-1]):
        print(f'Current shape at layer {layers["mode"]} is {dA.shape}')
        flattend = True
        if layer['mode'] == 'fc':
            dA_prev, dW, db = backward_linear_activation(dA_prev, layer, 'relu')
            layer['dW'] = dW
            layer['db'] = db
        elif layer['mode'] == 'conv':
            if flattend:
                dA = (dA_prev.T).reshape(m,1,1,layer['n_C']) # flatten backward
                flattend = False
            
            dZ = backward_relu(dA, layer['Z'])
            dA_prev, dW, db = backward_convolution(dZ, layer)
            layer['dW'] = dW
            layer['db'] = db
        
        elif layer['mode'] == 'pool':
            dA_prev = backward_pooling(dA_prev, layer, mode = "average")

    return layers

def update_parameters(layers, learning_rate):
    '''
    Updates the parameters of the layer

    Arguments:
    layers -- The list with the layers along with the coresponding hyperparameters
    learning_rate -- The learning rate by which the model is learning

    Returns:
    layers -- The updated list with the layers along with the oresponding hyperparameters
    '''
    num_layer = len(layers)
    for i in range(num_layer):
        mode = layers[i]['mode'] # 'fc', 'conv', 'pool'
        if mode == 'pool':
            continue
        elif (mode == 'fc' or mode == 'conv'):
            layers[i]['W'] = layers[i]['W'] - learning_rate*layers[i]['dW']
            layers[i]['b'] = layers[i]['b'] - learning_rate*layers[i]['db']
        else:
            print('Wrong layer mode in [{}]'.format(i))

    return layers

def predict(X_test, Y_test, layers):
    '''
    Makes a prediction based on the trained layers and calculates the accuracy 
    of the prediction

    Arguments:
    X_test -- The dataset with the images
    Y_test -- The actual labels of the images
    layers -- The trained layers

    Returns:
    pred -- The predicted labels
    accuracy -- The accuracy of the prediction
    '''

    m = X_test.shape[0]
    n = Y_test.shape[1]
    pred = np.zeros((n,m))
    pred_count = np.zeros((n,m)) - 1 # for counting accurate predictions 
    
    # Forward propagation
    AL, _, _ = forward_propogation(X_test, layers)

    # convert prediction to 0/1 form
    max_index = np.argmax(AL, axis = 0)
    pred[max_index, list(range(m))] = 1
    pred_count[max_index, list(range(m))] = 1
    
    accuracy = np.float(np.sum(pred_count == Y_test.T)) / m
    
    return pred, accuracy

def calculate_accuracy(AL, Y):
    '''
    Measures the performance of the results of a forward_propagation.
    
    Arguments:
    AL -- The predicted values
    Y -- The actual values
    
    Returns:
    accuracy -- The accuracy of the network
    '''

    n, m = Y.shape
    pred_count = np.zeros((n,m)) - 1
    
    max_index = np.argmax(AL, axis = 0)
    pred_count[max_index, list(range(m))] = 1
    
    accuracy = np.float(np.sum(pred_count == Y)) / m
    
    return accuracy

def train(X_train, Y_train, X_test, Y_test, layers, batch_size=10, num_epoch=1, learning_rate=0.01):
    '''
    Trains the modeles using the predifined functions

    Arguments:
    X_train -- The set of train images
    Y_train -- The actuall labels of train images
    X_test -- The set of test images
    Y_test -- The actuall labels of test images
    layers -- The layers which define the architecture of the model
    batch_size -- The amount of images that will be trained at once
    num_epoch -- The number of epochs
    learning_rate -- The learning rate by which the model will be trained

    Returns:
    layers -- The trained layers with the updated parameters (Weights, biases)
    accuracy_train_list -- The list with the train accuracy  for each epoch
    accuracy_test_list -- The list with the test accuracy  for each epoch
    '''
    # number of iteration
    num_sample=X_train.shape[0]
    num_iteration = num_sample // batch_size
    index = list(range(num_sample))
    
    accuracy_train_list = []
    accuracy_test_list = []
    for epoch in range(num_epoch):
        losses = []
        accuracies = []
        random.seed(10+epoch)
        random.shuffle(index) # random sampling every epoch
        pbar = tqdm(range(num_iteration))
        for iteration in pbar:
            pbar.set_description(f"Epoch : {epoch + 1}")
            batch_start = iteration * batch_size
            batch_end = (iteration + 1) * batch_size
            if batch_end > num_sample:
                batch_end = num_sample

            X_train_batch = X_train[index[batch_start:batch_end]]
            Y_train_batch = Y_train[index[batch_start:batch_end]]


            AL, layers, shapes = forward_propogation(X_train_batch, layers)
            #Display the shapes of the output of each layer only for the first time 
            if epoch == 0 and iteration == 0:
                print("______________________________________")
                print("Layer (type)          Output Shape    ")
                print("======================================")
                for shape in shapes:
                    if shape[0] == "fc":
                        print(f'{shape[0]}                 {shape[1]}')
                    else:
                        print(f'{shape[0]}               {shape[1]}')
                    
                    print("______________________________________")
            loss = calculate_cost(AL, Y_train_batch.T)
            accuracy = calculate_accuracy(AL, Y_train_batch.T)
            layers = backward_propagation(AL, Y_train_batch.T, layers)
            layers = update_parameters(layers, learning_rate)
            losses.append(loss)
            accuracies.append(accuracy)
            if (iteration+1) % 300 == 0:
                print('Epoch [{}] Iteration [{}]: loss = {} accuracy = {}'.format(epoch, iteration+1, loss, accuracy))

        _, accuracy_test = predict(X_test, Y_test, layers)
        pred_train, _ = forward_propogation(X_train[:10000], layers)
        loss_train = calculate_cost(pred_train, Y_train[:10000].T)
        accuracy_train = calculate_accuracy(pred_train, Y_train[:10000].T)
        accuracy_train_list.append(accuracy_train)
        accuracy_test_list.append(accuracy_test)
        print('Epoch [{}] average_loss = {} average_accuracy = {}'.format(epoch, np.mean(losses), np.mean(accuracies)))
        print('Epoch [{}] train_loss = {} train_accuracy = {}'.format(epoch, loss_train, accuracy_train))
        print('Epoch [{}] test_accuracy = {}'.format(epoch, accuracy_test))
    
    return layers, accuracy_train_list, accuracy_test_list

