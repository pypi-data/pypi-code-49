import mxnet as mx


def get_gpu(num=4):
    ctx = []
    for i in range(num):
        try:
            tmp = mx.nd.zeros((1,), ctx=mx.gpu(i))
            ctx.append(mx.gpu(i))
        except mx.MXNetError:
            if len(ctx) == 0:
                ctx.append(mx.cpu())
            break
    return ctx