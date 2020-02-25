import tensorflow as tf

def custom_fully_connected(inputs, num_hidden, activation_fn=tf.nn.tanh, reuse=tf.compat.v1.AUTO_REUSE, scope_str="default_tfv2_scope"):
    ## custom function to implement a fully connected layer in tensorflow v1 
    input_dim = inputs.shape[1] 
    with tf.compat.v1.variable_scope(scope_str, reuse=reuse) as scope:
        print(scope_str) 
        w_init = tf.compat.v1.keras.initializers.glorot_uniform() 
        w = tf.Variable(initial_value=w_init(shape=(input_dim, num_hidden), dtype='float64'), trainable=True)
        print(w)
        
        b_init = tf.compat.v1.keras.initializers.zeros() 
        b = tf.Variable(initial_value=b_init(shape=(num_hidden,),dtype='float64'), trainable=True) 
        print(b)
        
        z = tf.matmul(inputs, w) + b 
        out = activation_fn(z) 
    
    return out 
