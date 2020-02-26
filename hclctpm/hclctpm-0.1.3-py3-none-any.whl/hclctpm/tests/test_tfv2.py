import tensorflow as tf

#tf.compat.v1.disable_eager_execution()
scope_str = 'simpletcranker' 
reuse = tf.compat.v1.AUTO_REUSE
input_dim = 50
num_hidden = 30
with tf.compat.v1.variable_scope(scope_str, reuse=reuse) as scope:
    print(scope_str) 
    w_init = tf.compat.v1.keras.initializers.glorot_uniform() 
    w = tf.Variable(initial_value=w_init(shape=(input_dim, num_hidden), dtype='float64'), trainable=True)
    print(w)    
    b_init = tf.compat.v1.keras.initializers.zeros() 
    b = tf.Variable(initial_value=b_init(shape=(num_hidden,),dtype='float64'), trainable=True) 
    print(b)

#reuse = True
with tf.compat.v1.variable_scope(scope_str, reuse=reuse) as scope:
    print(scope_str) 
    w_init = tf.compat.v1.keras.initializers.glorot_uniform() 
    w = tf.Variable(initial_value=w_init(shape=(input_dim, num_hidden), dtype='float64'), trainable=True)
    print(w)    
    b_init = tf.compat.v1.keras.initializers.zeros() 
    b = tf.Variable(initial_value=b_init(shape=(num_hidden,),dtype='float64'), trainable=True) 
    print(b)
    
