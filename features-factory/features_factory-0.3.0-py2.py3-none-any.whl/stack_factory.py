from typing import List

from features_factory.stack import Stack


class StackFactory:

    @staticmethod
    def clones(FeatureMatrix, args: List[dict]) -> Stack:
        """
        Generate a stack containing features of the same kind (FeatureMatrix), initialized with the arguments
        specified in args.

        :param FeatureMatrix: the Feature class that should be cloned
        :param args: list of kwargs to pass to Feature at initialization time
        :return:

        E.g.
            int1 = IntInputFeature('int1')
            int2 = IntInputFeature('int2')
            float1 = FloatInputFeature('float1')

            names = ['2 x int1', '2 x int2', '2 x float1']
            dependencies = [int1, int2, float1]
            args = [{'name': name, 'dependency': feat, 'map_function': lambda x: 2*x}
                    for name, feat in zip(names, dependencies)]
            stack: Stack = StackFactory.create_clones(OneComponentFeature, args)
        """
        features = list()
        for kwarg in args:
            features.append(FeatureMatrix(**kwarg))

        return Stack(features)
