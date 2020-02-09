import keras.backend as K


def recall(y_true, y_pred):
    tp = K.sum(K.cast(y_true * y_pred, 'float'), axis=0)
    fn = K.sum(K.cast(y_true * (1 - y_pred), 'float'), axis=0)

    return tp / (tp + fn + K.epsilon())


def precision(y_true, y_pred):
    tp = K.sum(K.cast(y_true * y_pred, 'float'), axis=0)
    fp = K.sum(K.cast((1 - y_true) * y_pred, 'float'), axis=0)
    return tp / (tp + fp + K.epsilon())


# def pr_loss(y_true, y_pred):
#     precision = precision_m(y_true, y_pred)
#     recall = recall_m(y_true, y_pred)
#     #     return 2 - K.mean(precision + recall) #+  K.mean(K.abs(precision - recall))
#     return K.mean(3 - (1.5 * precision + recall))  # +  K.mean(K.abs(precision - recall))


def f1_score(y_true, y_pred):
    precision_value = precision(y_true, y_pred)
    recall_value = recall(y_true, y_pred)
    return 2 * ((precision_value * recall_value) / (precision_value + recall_value + K.epsilon()))


# def f1_loss(y_true, y_pred):
#     tp = K.sum(K.cast(y_true * y_pred, 'float'), axis=0)
#     #     tn = K.sum(K.cast((1-y_true)*(1-y_pred), 'float'), axis=0)
#     fn = K.sum(K.cast(y_true * (1 - y_pred), 'float'), axis=0)
#     fp = K.sum(K.cast((1 - y_true) * y_pred, 'float'), axis=0)
#
#     r = tp / (tp + fn + K.epsilon())
#     p = tp / (tp + fp + K.epsilon())
#
#     f1 = 2 * 3 * p * r / (3 * p + r + K.epsilon())
#     f1 = tf.where(tf.is_nan(f1), tf.zeros_like(f1), f1)
#     return 1 - K.mean(f1)


# def iou_loss_core(true, pred):
#     intersection = true * pred
#     notTrue = 1 - true
#     union = true + (notTrue * pred)
#
#     return -(K.sum(intersection, axis=-1) + K.epsilon()) / (K.sum(union, axis=-1) + K.epsilon())


def iou(y_true, y_pred):
    intersection = y_true * y_pred
    not_true = ~y_true # 1 - y_true
    union = y_true + (not_true * y_pred)
    return (K.sum(intersection, axis=-1) + K.epsilon()) / (K.sum(union, axis=-1) + K.epsilon())
