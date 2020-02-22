import mxnet as mx
from mxnet.gluon import nn


vgg16base_config = {'conv': [(2, (64,  3, 1, 1, 1)), 
                    (2, (128, 3, 1, 1, 1)), 
                    (3, (256, 3, 1, 1, 1)), 
                    (3, (512, 3, 1, 1, 1)), 
                    (3, (512, 3, 1, 1, 1))],
                    'pool': [(2,2,0), (2,2,0), (2,2,0), (2,2,0), (3,1,1)]}


class Scale(nn.Block):
    def __init__(self, std=(0.229, 0.224, 0.225), **kwargs):
        super(Scale, self).__init__(**kwargs)
        scale = mx.nd.array([0.229, 0.224, 0.225]).reshape((1, 3, 1, 1)) * 255
        self.scale = self.params.get_constant('scale', scale)

    def forward(self, x):
        return mx.nd.broadcast_mul(x, self.scale.data())


class BaseBlk(nn.Block):
    def __init__(self, init=None, activation=None, use_batch=False, **kwargs):
        super(BaseBlk, self).__init__(**kwargs)
        if init is None:
            self.init = {'weight_initializer': mx.init.Xavier(
                        rnd_type='gaussian', factor_type='out', magnitude=2),
                        'bias_initializer': 'zeros'}
        else:
            self.init = init

        if activation is None:
            self.act = 'relu'
        else:
            self.act = activation

        self.use_batch = use_batch

    def _get_conv(self, c, k, s, p, d=1, prefix=None):
        conv = nn.Sequential()
        conv.add(nn.Conv2D(channels=c, kernel_size=k, strides=s, padding=p, 
                           dilation=d, **self.init))
        if self.use_batch:
            conv.add(nn.BatchNorm())
        conv.add(nn.Activation(self.act))
        return conv

    def _get_blk(self, blk_config, prefix=None):
        blk = nn.Sequential(prefix=prefix)
        with blk.name_scope():
            if blk_config[0] > 0:
                (c, k, s, p, d) = blk_config[1]
                for i in range(blk_config[0]):
                    blk.add(self._get_conv(c, k, s, p, d, prefix='conv%d_'%i))
            else:
                for i, (c, k, s, p, d) in enumerate(blk_config[1:]):
                    blk.add(self._get_conv(c, k, s, p, d, prefix='conv%d_'%i))
        return blk

    def forward(self, x):
        raise NotImplementedError


class VGGbase(BaseBlk):
    def __init__(self, config, ceil_mode=True,**kwargs):
        super(VGGbase, self).__init__(**kwargs)
        self.ceil_mode = ceil_mode

        with self.name_scope():
            self.base_blks = nn.Sequential(prefix='base_')
            self.base_pools = nn.Sequential(prefix='base_')

            with self.base_blks.name_scope():
                for i, conf in enumerate(config['conv']):
                    self.base_blks.add(self._get_blk(conf, prefix='blk%d_'%i))
            with self.base_pools.name_scope():
                for i, conf in enumerate(config['pool']):
                    self.base_pools.add(nn.MaxPool2D(pool_size=conf[0], strides=conf[1],
                                                     padding=conf[2], ceil_mode=self.ceil_mode, 
                                                     prefix='blk%d_pool_'%i))

    def forward(self, x):
        for blk, pool in zip(self.base_blks, self.base_pools):
            x = blk(x)
            x = pool(x)

        return x


class L2Norm(nn.Block):
    def __init__(self, n_channel, initial=20, eps=1e-5, **kwargs):
        super(L2Norm, self).__init__(**kwargs)
        self.eps = eps
        self.scale = self.params.get('normalize_scale', 
                                     shape=(1, n_channel, 1, 1),
                                     init=mx.init.Constant(initial))

    def forward(self, x):
        x = mx.nd.L2Normalization(x, mode='channel', eps=self.eps)
        return mx.nd.broadcast_mul(x, self.scale.data())


feature_config = [(0, (1024, 3, 1, 6, 6),  (1024, 1, 1, 0, 1)),
                  (0, (256,  1, 1, 0, 1),  (512,  3, 2, 1, 1)),
                  (0, (128,  1, 1, 0, 1),  (256,  3, 2, 1, 1)),
                  (0, (128,  1, 1, 0, 1),  (256,  3, 1, 0, 1)),
                  (0, (128,  1, 1, 0, 1),  (256,  3, 1, 0, 1))]


class VGGFeature(VGGbase):
    def __init__(self, base_config, feature_config, **kwargs):
        super(VGGFeature, self).__init__(config=base_config, **kwargs)

        self.in_scale = Scale()

        self.blk4_norm = L2Norm(512, prefix='norm_')

        with self.name_scope():
            self.feature_blks = nn.Sequential(prefix='feature_')
            with self.feature_blks.name_scope():
                for i, conf in enumerate(feature_config):
                    self.feature_blks.add(self._get_blk(conf, prefix='blk%d_'%i))

    def forward(self, x):
        x = self.in_scale(x)

        feature = []

        for i, (blk, pool) in enumerate(zip(self.base_blks, self.base_pools)):
            x = blk(x)
            if i == 3:
                norm = self.blk4_norm(x)
                feature.append(norm)
            x = pool(x)

        for blk in self.feature_blks:
            x = blk(x)
            feature.append(x)

        return feature


def get_VGG16base():
    return VGGbase(vgg16base_config)


def get_VGG16Feature():
    return VGGFeature(vgg16base_config, feature_config)

