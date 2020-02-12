import matplotlib.pyplot as plt
import numpy as np


def pairs_histogram_factory(n, m, name, generating_function):
    assert (
        name == "angle" or name == "distance"
    ), "This is implemented only for angles or distances between pairs of points."
    geometrical_quantity = generating_function(n, m)
    print(
        "The mean of the {}s in R^{} is {}".format(
            name, n, np.mean(geometrical_quantity)
        )
    )
    print(
        "The stdev of the {}s in R^{} is {}".format(
            name, n, np.std(geometrical_quantity)
        )
    )
    plt.hist(geometrical_quantity)
    if name == "angle":
        plt.xlim(0, 180.5)
        plt.xlabel("angle (degrees)")
    elif name == "distance":
        plt.xlim(0, 2.05)
        plt.xlabel("distance")
    plt.title(
        "Pairs of points in sphere in $\mathbb{R}^{"
        + str(n)
        + "}$"
        + " with a certain {} between them".format(name)
    )
    plt.ylabel("count")


def distance_histogram_factory(n, m, sample_in_sphere, distance_from_origin):
    """
    n: number of dimensions
    m: number of points to sample
    """
    distances = []

    ## Use a previously defined function to generate
    ## m sample points from R^n
    points = sample_in_sphere(n, m)  # SOLUTION

    for i in range(points.shape[1]):

        ## Obtain a n-length one-dimensional ndarray that represents the ith point sampled from R^n
        point = points[:, i]  # SOLUTION

        ## Calculate the distance between point and the origin
        distance = distance_from_origin(point)  # SOLUTION

        distances.append(distance)

    print("The mean of the distances in R^{} is {}".format(n, np.mean(distances)))
    print("The stdev of the distances in R^{} is {}".format(n, np.std(distances)))
    plt.hist(distances)
    plt.xlim(0, 1.05)
    plt.ylabel("count")
    plt.xlabel("distance")
    plt.title(
        "Points in sphere in $\mathbb{R}^{"
        + str(n)
        + "}$ with a certain distance from origin"
    )
