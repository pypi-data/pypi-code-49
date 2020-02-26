import tensorflow as tf 

def DefineKerasSimpleTCModel(input_dim, num_hidden, sample_size, activation=tf.nn.tanh): 
    ## define the simple TC model from scratch
    
    inputs_tr = tf.keras.Input(shape=(input_dim,)) 
    inputs_co = tf.keras.Input(shape=(input_dim,)) 
    print('inputs_tr :' + str(inputs_tr.shape))
    
    c_tr = tf.keras.Input(shape=(1,)) 
    c_co = tf.keras.Input(shape=(1,)) 
    g_tr = tf.keras.Input(shape=(1,)) 
    g_co = tf.keras.Input(shape=(1,)) 
    
    weight_layer = tf.keras.layers.Dense(num_hidden, activation=activation, name='score_output') 
    x_tr = weight_layer(inputs_tr) 
    x_co = weight_layer(inputs_co) 
    print('x_tr :' + str(x_tr.shape))
    
    scores = x_tr
    
    sm_layer_batchaxis = tf.keras.layers.Softmax(axis=0) 
    
    s_tr = sm_layer_batchaxis(x_tr) 
    s_co = sm_layer_batchaxis(x_co) 
    print('s_tr :' + str(s_tr.shape))
    
    dc_tr = tf.reduce_sum(tf.multiply(s_tr, c_tr), axis=0) 
    dc_co = tf.reduce_sum(tf.multiply(s_co, c_co), axis=0) 
    
    dg_tr = tf.reduce_sum(tf.multiply(s_tr, g_tr), axis=0) 
    dg_co = tf.reduce_sum(tf.multiply(s_co, g_co), axis=0) 
    
    print('dc_tr :' + str(dc_tr.shape))
    print('dg_tr :' + str(dg_tr.shape))
    
    outputs = tf.divide(dc_tr - dc_co, dg_tr - dg_co, name='main_output') 
    
    print('outputs :')
    print(outputs)
    
    print('outputs size : ' + str(outputs.shape))
    
    model = tf.keras.Model(inputs=[inputs_tr, inputs_co, c_tr, c_co, g_tr, g_co], outputs=[outputs, scores]) 
    return model 
