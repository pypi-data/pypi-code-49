import matplotlib.pyplot as plt
import numpy as np


def scree_plot_factory(sorted_eigenvalues, proportion_explained, ylim=[-0.1, 1.1]):
    # Calculate the vector containing the proportion of
    # total variance explained by each principal component.
    out = proportion_explained(sorted_eigenvalues)

    number_of_pcs = len(sorted_eigenvalues)
    xlim = [-0.1, number_of_pcs + 0.1]

    # Plot the scree plot based on this information.
    fig = plt.figure()
    axes = plt.gca()
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    fig.suptitle("Proportion of variance explained by each principal component")
    plt.xlabel("$k$th principal component")
    plt.ylabel("Proportion of variance")

    xticks = np.arange(np.ceil(xlim[0]), np.floor(xlim[1]))
    plt.xticks(xticks)

    plt.plot(out, "-o")
    plt.show()


def cumulative_variance_plot_factory(
    sorted_eigenvalues, proportion_explained, cumulative_explained
):
    proportions = proportion_explained(sorted_eigenvalues)
    cumulative_proportions = cumulative_explained(sorted_eigenvalues)

    number_of_pcs = len(sorted_eigenvalues)

    with plt.style.context("seaborn-whitegrid"):
        plt.figure(figsize=(6, 4))

        plt.bar(
            range(number_of_pcs),
            proportions,
            alpha=0.5,
            width=1,
            align="edge",
            label="Individual explained variance",
        )
        plt.step(
            range(number_of_pcs),
            cumulative_proportions,
            where="post",
            label="Cumulative explained variance",
        )
        plt.ylabel("Proportion of explained variance")
        plt.xlabel("Principal components ranked by eigenvalues")
        xticks = np.arange(0, number_of_pcs)
        plt.xticks(xticks)
        plt.title("Variance explained by the PCs")
        plt.legend(loc="best")
        plt.tight_layout()
