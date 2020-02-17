import numpy as np


class Salience():
    def __init__(
        self,
        weights,
        word2id,
        N=50,
        metric="cosine",
        kernel="power"
    ):
        self.word2id = word2id
        self.weights = weights
        self.dim = weights.shape[1]
        self.N = N
        self.metric = metric
        self.kernel = kernel

    def split_tokens(self, tokens):
        N = self.N

        # map token to word indices using the WordVectors model
        tokens = [
            self.word2id[item] for item in tokens
            if item in self.word2id]
        num_tokens = len(tokens)
        assert num_tokens >= 2  # ensure than we can split data in two

        # simpler case: the number of tokens is more than the two cuts
        if num_tokens >= 2 * N:
            tokens_a = tokens[:N]
            tokens_b = tokens[N:N + N]
            return tokens_a, tokens_b
        else:  # if not, we just use a subset
            num_a = num_tokens // 2
            num_b = num_tokens - num_a
            tokens_a = [0] * (N - num_a) + tokens[:num_a]
            tokens_b = [0] * (N - num_b) + tokens[num_a:]
            assert len(tokens_a) == N and len(tokens_b) == N
            return tokens_a, tokens_b

    def prepare_dataset(self, series):
        X, Y = [], []
        for tokens in series:
            a, b = self.split_tokens(tokens)
            X.append(a)
            Y.append(b)
        X, Y = np.array(X), np.array(Y)
        series_length = len(X)

        # random indexation
        index = np.arange(len(X))
        np.random.shuffle(index)
        X = X[index]
        Y = Y[index]

        X = np.vstack([X, X[:-1]])
        Y = np.vstack([Y, Y[1:]])
        Z = np.zeros(len(X))
        Z[:series_length] = 1
        return X, Y, Z

    def cosine_model(self):
        from keras.models import Model
        from keras.layers import Input, Embedding, Dot
        from .attention import AttentionWeightedAverage

        # num words in vocabulary
        num_words = len(self.word2id) + 1

        # create embedding layer
        embedding = Embedding(
            num_words, self.dim,
            input_length=self.N, trainable=False,
            weights=[self.weights], mask_zero=True)
        attention = AttentionWeightedAverage(norm=False)

        left_inp = Input((self.N,))
        left_encoder = embedding(left_inp)
        left_encoder = attention(left_encoder)

        right_inp = Input((self.N,))
        right_encoder = embedding(right_inp)
        right_encoder = attention(right_encoder)

        cosine = Dot(-1, normalize=True)([left_encoder, right_encoder])
        model = Model([left_inp, right_inp], cosine)
        model.compile("nadam", "mse", metrics=["accuracy"])
        model.summary()
        return model, attention

    def euclidean_model(self):
        from keras.models import Model
        from keras.layers import Input, Embedding, Lambda
        from .attention import AttentionWeightedAverage
        import keras.backend as K

        # num words in vocabulary
        num_words = len(self.word2id) + 1

        # create embedding layer
        embedding = Embedding(
            num_words, self.dim,
            input_length=self.N, trainable=False,
            weights=[self.weights], mask_zero=True)
        attention = AttentionWeightedAverage(norm=False)

        left_inp = Input((self.N,))
        left_encoder = embedding(left_inp)
        left_encoder = attention(left_encoder)

        right_inp = Input((self.N,))
        right_encoder = embedding(right_inp)
        right_encoder = attention(right_encoder)

        distance = Lambda(
            lambda x: K.sum(K.square(x[0] - x[1]), axis=-1, keepdims=True),
            name='euclidean_distance')([left_encoder, right_encoder])
        if self.kernel == "gaussian":
            similarity = Lambda(
                lambda x: K.exp(-x), name="similarity")(distance)
        elif self.kernel == "power":
            similarity = Lambda(
                lambda x: 1 / (1 + x), name="similarity")(distance)

        model = Model([left_inp, right_inp], similarity)
        model.compile("nadam", "mse", metrics=["accuracy"])
        model.summary()
        return model, attention

    def fit(self, series, **kwargs):
        X, Y, Z = self.prepare_dataset(series)

        # chose model
        if self.metric == "cosine":
            model, attention = self.cosine_model()
        elif self.metric == "euclidean":
            model, attention = self.euclidean_model()

        model.fit([X, Y], Z, **kwargs)
        W, W2 = attention.get_weights()

        # double feed forward
        logits = np.tanh(np.dot(self.weights, W))
        logits = np.exp(np.dot(logits, W2))

        word2salience = {}
        for word, index in self.word2id.items():
            word2salience[word] = float(logits[index])
        return word2salience
