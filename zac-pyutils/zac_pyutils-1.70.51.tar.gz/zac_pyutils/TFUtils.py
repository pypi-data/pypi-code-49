# author: zac
# create-time: 2019-08-27 10:29
# usage: - 
import tensorflow as tf


def convert_ckpt2pb(ckpt_fp, pb_fp, output_name_list):
    """
    将ckpt模型存储为pb格式，示例：
        convert_ckpt2pb('ckpt/cnn.ckpt-10000','pb/cnn.pb',['output/proba'])
    :param ckpt_fp: 输入.ckpt的路径 |
    :param pb_fp: 输出.pb的路径 |
    :param output_name_list: 输出节点的名字，一般就是一个，['output/proba']，注意此参数接受的是节点名（没有后面的数字）
    """
    saver = tf.train.import_meta_graph(ckpt_fp + '.meta', clear_devices=True)

    with tf.Session() as sess:
        saver.restore(sess, ckpt_fp)  # 恢复图并得到数据
        output_graph_def = tf.graph_util.convert_variables_to_constants(
            sess=sess,
            input_graph_def=sess.graph_def,
            output_node_names=output_name_list)

        with tf.gfile.GFile(pb_fp, "wb") as f:  # 保存模型
            f.write(output_graph_def.SerializeToString())  # 序列化输出
        print("%d ops in the final graph." % len(output_graph_def.node))  # 得到当前图有几个操作节点


def predict_pb(pb_fp, output_tensor_name, feed_dict_names):
    """
    示例：
        feed_dict_names={'input:0':xxx,'keep_prob:0':1.0,'is_training:0':0}
        predict_pb('model.pb','output/proba:0',feed_dict_names)
    :param pb_fp: pb文件路径
    :param output_tensor_name: 最终输出的tensor名字
    :param feed_dict_names: 字典，key是tensor名字(不是操作名)，v是该tensor的输入值
    :return:
    """
    with tf.Graph().as_default():
        output_graph_def = tf.GraphDef()
        # 恢复图并得到数据
        with open(pb_fp, "rb") as f:
            output_graph_def.ParseFromString(f.read())
            tf.import_graph_def(output_graph_def, name="")
        # 计算output
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            output_tensor = sess.graph.get_tensor_by_name(output_tensor_name)
            fd = {sess.graph.get_tensor_by_name(k): v for k, v in feed_dict_names.items()}
            output = sess.run(output_tensor, feed_dict=fd)
            return output


def predict_ckpt(ckpt_fp, output_tensor_name, feed_dict_names):
    """
    示例：
        feed_dict_names={'input:0':xxx,'keep_prob:0':1.0,'is_training:0':0}
        predict_pb('model.pb','output/proba:0',feed_dict_names)
    :param ckpt_fp: ckpt文件路径
    :param output_tensor_name: 最终输出的tensor名字
    :param feed_dict_names: 字典，key是tensor名字(不是操作名)，v是该tensor的输入值
    :return:
    """
    # 恢复图并得到数据
    saver = tf.train.import_meta_graph(ckpt_fp + '.meta', clear_devices=True)
    with tf.Session() as sess:
        saver.restore(sess, ckpt_fp)
        # 计算output
        sess.run(tf.global_variables_initializer())
        output_tensor = sess.graph.get_tensor_by_name(output_tensor_name)
        fd = {sess.graph.get_tensor_by_name(k): v for k, v in feed_dict_names.items()}
        output = sess.run(output_tensor, feed_dict=fd)
        return output


def print_all_tensors_from_ckpt(ckpt_fp):
    from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
    print_tensors_in_checkpoint_file(ckpt_fp, tensor_name=None, all_tensors=False)


def get_all_variable(target_graph=None):
    if target_graph is None:
        target_graph = tf.get_default_graph()
    with target_graph.as_default():
        return tf.global_variables()


def print_all_variable(target_graph=None, name=True, value=True):
    variables = get_all_variable(target_graph)
    for v in variables:
        to_print = ""
        if name:
            to_print += f"[name]: {v.name}"
        if value:
            to_print += f"[values]: {v}"
        print(to_print)


def get_all_operation(target_graph=None):
    if target_graph is None:
        target_graph = tf.get_default_graph()
    return target_graph.get_operations()


def print_all_operation(target_graph=None, name=True, type=True, value=True):
    opts = get_all_operation(target_graph)
    for v in opts:
        to_print = ""
        if name:
            to_print += f"[name]: {v.name}"
        if type:
            to_print += f"[type]: {v.type}"
        if value:
            to_print += f"[values]: {v.values}"
        print(to_print)


def restore_ckpt(ckpt_fp, sess):
    with sess.graph.as_default():
        saver = tf.train.Saver()
        saver.restore(sess, ckpt_fp)


# todo: without test
def restore_pb(pb_fp, target_graph=None):
    if target_graph is None:
        target_graph = tf.get_default_graph()
    with target_graph.as_default():
        output_graph_def = tf.GraphDef()
        # 恢复图并得到数据
        with tf.gfile.GFile(pb_fp, "rb") as f:
            output_graph_def.ParseFromString(f.read())
            tf.import_graph_def(output_graph_def)


def img2tfrecord(img_dir, output_dir):
    raise NotImplementedError
