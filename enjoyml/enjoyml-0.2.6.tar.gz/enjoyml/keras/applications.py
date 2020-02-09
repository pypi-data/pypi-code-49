from keras.models import Model
from keras.layers import Input, Conv2D, Dropout, MaxPooling2D, UpSampling2D, concatenate


def U_net(pretrained_weights=None, input_size=(256, 256, 1), n_output_channels=1,
          channels_start=4, dropout=0.0, head_dropout=0.3, depth=5, pool_size=2,
          final_activation='sigmoid'):
    """
    model = U_net(
        input_size=(None, None, 3), n_output_channels=1,
        channels_start=8, dropout=0.0, head_dropout=0.4,
        depth=5, pool_size=2, final_activation='sigmoid'\
    )
    """
    assert channels_start > n_output_channels * 2
    assert final_activation in ['sigmoid', 'softmax']
    inputs = Input(input_size)

    in_depth_layers = []
    x = inputs

    for i in range(depth):
        x = Conv2D(2 ** i * channels_start, 3, activation='relu', padding='same', kernel_initializer='he_normal')(x)
        x = Conv2D(2 ** i * channels_start, 3, activation='relu', padding='same', kernel_initializer='he_normal')(x)
        x = drop = Dropout(dropout)(x)
        x = MaxPooling2D(pool_size=(pool_size, pool_size))(x)

        in_depth_layers.append(drop)

    x = Conv2D(2 ** depth * channels_start, 3, activation='relu', padding='same', kernel_initializer='he_normal')(x)
    x = Conv2D(2 ** depth * channels_start, 3, activation='relu', padding='same', kernel_initializer='he_normal')(x)
    x = Dropout(dropout)(x)

    for i in reversed(range(depth)):
        x = Conv2D(2 ** i * channels_start, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            UpSampling2D(size=(pool_size, pool_size))(x))
        x = concatenate([in_depth_layers[i], x], axis=3)
        x = Conv2D(2 ** i * channels_start, 3, activation='relu', padding='same', kernel_initializer='he_normal')(x)
        x = Conv2D(2 ** i * channels_start, 3, activation='relu', padding='same', kernel_initializer='he_normal')(x)

    x = Conv2D(n_output_channels * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(x)
    x = Dropout(head_dropout)(x)
    x = Conv2D(n_output_channels * 2, 1, activation='relu')(x)
    x = Dropout(head_dropout)(x)
    x = Conv2D(n_output_channels, 1, activation=final_activation)(x)

    model = Model(input=inputs, output=x)

    if pretrained_weights is not None:
        model.load_weights(pretrained_weights)

    return model
