import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles
import numpy as np

file_path = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
            "3-Vencode/Fantom5/R projects/Plots/Validations/Venn/"

subsets_dict = {"HeLaS3": (56247, 2000, 1534),
                "HEK293": (13167, 6952, 1136)}


def venn_2():
    for name, subset in subsets_dict.items():
        normalize = 0.0015

        v = venn2(subsets=subset, normalize_to=normalize)
        v.get_patch_by_id('10').set_color('orangered')
        v.get_patch_by_id("B").set_color('grey')
        v.get_label_by_id('A').set_text('')
        v.get_label_by_id('B').set_text('')
        v.get_label_by_id('11').set_text("")
        v.get_label_by_id('10').set_text("")
        v.get_label_by_id('01').set_text("")
        c = venn2_circles(subsets=subset, color="black", normalize_to=normalize, linewidth=1.5)

        file_name = name + "_notext.png"
        file_final_path = file_path + file_name
        plt.savefig(file_final_path, transparent=True, bbox_inches="tight", pad_inches=-1.1)
        plt.close()


subsets_dict_3 = {"GM12878": (49672, 4551, 3558, 66254, 15453, 1816, 2433),
                  "HepG2": (50160, 1866, 1394, 2236, 1823, 124, 273),
                  "SCLC": (21770, 585, 311, 193507, 20223, 374, 307)}


def venn_3():
    for name, subset in subsets_dict_3.items():
        normalize = 0.0015

        v = venn3(subsets=subset, normalize_to=normalize, set_labels=("", "", ""))
        v.get_patch_by_id('100').set_color('orangered')
        v.get_patch_by_id("010").set_color('grey')
        v.get_patch_by_id("001").set_color('yellow')
        v.get_label_by_id('111').set_text("")
        v.get_label_by_id('110').set_text("")
        v.get_label_by_id('101').set_text("")
        v.get_label_by_id('011').set_text("")
        v.get_label_by_id('10').set_text("")
        v.get_label_by_id('010').set_text("")
        v.get_label_by_id('001').set_text("")
        c = venn3_circles(subsets=subset, color="black", normalize_to=normalize, linewidth=1.5)

        file_name = name + "_notext.png"
        file_final_path = file_path + file_name
        plt.savefig(file_final_path, transparent=True, bbox_inches="tight", pad_inches=-1.1)
        plt.close()


def venn_legend():
    subset = (1000, 100, 0, 10, 0, 0, 0)
    normalize = 0.0015

    v = venn3(subsets=subset, normalize_to=normalize, set_labels=("", "", ""))
    v.get_label_by_id('100').set_text('')
    v.get_label_by_id('010').set_text('')
    v.get_label_by_id('001').set_text('')
    v.get_patch_by_id('100').set_color('orangered')
    v.get_patch_by_id("010").set_color('orangered')
    v.get_patch_by_id("001").set_color('orangered')
    c = venn3_circles(subsets=subset, color="black", normalize_to=normalize, linewidth=1.5)

    file_name = "LEGEND.png"
    file_final_path = file_path + file_name
    plt.savefig(file_final_path, transparent=True, bbox_inches="tight", pad_inches=0)
    plt.close()


def venn_stacked():
    from matplotlib.cbook import flatten

    figure, axes = plt.subplots(len(subsets_dict), 1, figsize=(3, 30))

    # plt.show()
    for name, subset in subsets_dict.items():
        i = 0
        normalize = 0.0015

        v = venn2(subsets=subset, normalize_to=normalize, ax=axes[i])
        v.get_patch_by_id('10').set_color('orangered')
        v.get_patch_by_id("B").set_color('grey')
        v.get_label_by_id('A').set_text('')
        v.get_label_by_id('B').set_text('')
        v.get_label_by_id('11').set_text("")
        v.get_label_by_id('10').set_text("")
        v.get_label_by_id('01').set_text("")
        c = venn2_circles(subsets=subset, color="black", normalize_to=normalize, linewidth=1.5, ax=axes[i])
        i += 1
        # plt.axis('off')
        plt.show()
    data = subsets_dict.values()
    max_area = max(map(sum, data))

    def set_venn_scale(ax, true_area, reference_area=max_area):
        s = np.sqrt(float(reference_area) / true_area)
        ax.set_xlim(-s, s)
        ax.set_ylim(-s, s)

    for a, d in zip(flatten(axes), data):
        set_venn_scale(a, sum(d))

    plt.show()


if __name__ == "__main__":
    venn_2()
    # venn_3()
    # venn_legend()
    # venn_stacked()
