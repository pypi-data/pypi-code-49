


class Indices(object):

    def __init__(self):
        pass

    def indices(self):
        raise NotImplementedError

    def get_sequences(orientation):
        raise NotImplementedError


class ContiguousIndices(Indices):

    def indices(self):
        return range(start, end) % modulo


class EpisodeIndices(Indices):

    def indices(self):
        return range(start, end) % modulo

    def get_sequences(orientation):



class ScatteredIndices(Indices):

    def indices(self):
        return self.indices

    def get_sequences(orientation):




class Sequences(object):

    def __init__(self):
        pass

    def lengths(self):
        raise NotImplementedError

    def start_indices(self):
        raise NotImplementedError

    def end_indices(self):
        raise NotImplementedError


class ContiguousSequences(Sequences):

    def __init__(self, orientation):
        self.start = None
        self.end = None
        self.modulo = None
        self.lengths = None
        self.num = None

    def lengths(self):
        return self.lengths

    def start_indices(self):
        if orientation == 'start':
            return range(self.start, self.start + self.num) % self.modulo
        else:
            return (self.end_indices() - self.lengths) % self.modulo

    def end_indices(self):
        if orientation == 'end':
            return range(self.end - self.num, self.end) % self.modulo
        else:
            return (self.start_indices() + self.lengths) % self.modulo


class ScatteredSequences(Sequences):

    def __init__(self):
        self.indices = None
        self.lengths = None

    def lengths(self):
        return self.lengths

    def start_indices(self):
        return self.indices[tf.math.cumsum(x=self.lengths, exclusive=True)]

    def end_indices(self):
        return self.indices[tf.math.cumsum(x=lengths) - one]
