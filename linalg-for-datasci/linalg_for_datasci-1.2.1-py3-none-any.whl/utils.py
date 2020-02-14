import numpy as np
import pandas as pd


def sort_eigs(eigvals, eigvecs):
    idx = eigvals.argsort()[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    return eigvals, eigvecs


def ball_to_box_ratio(num_trials, callback):
    num_hits = 0
    for _ in range(num_trials):
        dart = callback()
        if dart["in_ball"]:
            num_hits += 1
    return num_hits / num_trials


def throw_darts(num_trials, callback):
    darts = np.array([])

    for _ in range(num_trials):
        dart = callback()

        d = len(dart["coordinates"])

        if d == 1:
            dart["coordinates"] = np.pad(dart["coordinates"], (0, 2))
        elif d == 2:
            dart["coordinates"] = np.pad(dart["coordinates"], (0, 1))
        elif d == 3:
            pass
        else:
            raise ValueError("Dart must be two or three dimensional")

        dart = np.append(dart["coordinates"], dart["in_ball"])
        darts = np.append(darts, dart)

    darts = darts.reshape([-1, 4])
    darts = pd.DataFrame(darts).rename(
        columns={
            0: "First Dimension",
            1: "Second Dimension",
            2: "Third Dimension",
            3: "Inside Ball",
        }
    )
    return darts
