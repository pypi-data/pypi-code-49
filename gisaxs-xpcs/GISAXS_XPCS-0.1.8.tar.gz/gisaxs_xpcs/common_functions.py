# -*- coding: utf-8 -*-


import matplotlib as mpl
from matplotlib import cm
from matplotlib.colors import LogNorm


import h5py
from tqdm import tqdm

from .extract_data import *
from .common_tools import *
from .plot_report import *

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

ed0 = ed1 = ExtractData()


def show_folders_info(folder_list: List[int]):
    print('\n'.join([': '.join([str(f), str(len(get_zaptime_files(f))), f'PEN0{get_pen_folder_number(f)}'])
                     for f in folder_list]))


def show_folder_first_and_last(folder_num):
    first, last = ed0.metadata.get_first_and_last(folder_num)
    print('First frame: ', first, sep='\n\n')
    print('-' * 50)
    print('Last frame: ', last, sep='\n\n')


def get_all_files(folder_num_list, max_number_of_files_in_each_folder=None):
    files = list()
    for folder_num in folder_num_list:
        number_of_files = len(get_zaptime_files(folder_num)) - 2
        step = 1 if not max_number_of_files_in_each_folder else int(
            number_of_files / max_number_of_files_in_each_folder)
        files.extend([(folder_num, i) for i in range(1, number_of_files, step)])
    return files


def get_cmap(y):
    y = np.array(y)
    norm = mpl.colors.Normalize(vmin=y.min(), vmax=y.max())
    cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.jet)
    cmap.set_array([])
    return cmap


def get_nm(delta):
    """
    Returns size in [nm] corresponding for the provided delta in degrees
    for 1.5307 [A] wavelength (common approximate formula is lambda [nm] / delta [rad] for small angles).
    """
    return 8.77 / delta


def get_intensity_from_moneta(files, **kwargs):
    intensity_array = np.empty(len(files))
    for i, f in enumerate(tqdm(files)):
        df = ed0.get_images(*f, **kwargs)
        intensity_array[i] = df.sum().sum()
    time_axis = get_time_axis(files)
    plt.plot(time_axis, intensity_array)
    ax = plt.gca()
    ax.set_xlabel('Time (sec)')
    ax.set_ylabel('Integrated intensity of the frame (a.u.)')


def get_intensity_from_h5(files):
    h5_filepath = os.path.join('metadata', 'test_raw_data.h5')

    def dset_path(file: Tuple[int, int], z_number=4):
        return '/'.join(['Raw data', 'zaptime_%d' % file[0], str(file[1]).zfill(z_number)])

    def group_path(file: Tuple[int, int]):
        return '/'.join(['Raw data', 'zaptime_%d' % file[0]])

    intensity_array = np.empty(len(files))

    with h5py.File(h5_filepath) as h5file:
        for i, f in enumerate(tqdm(files)):
            z_number = len(list(h5file[group_path(f)].keys())[0])
            intensity_array[i] = h5file[dset_path(f, z_number)][()].flatten().sum()

    time_axis = get_time_axis(files)
    plt.plot(time_axis, intensity_array)
    ax = plt.gca()
    ax.set_xlabel('Time (sec)')
    ax.set_ylabel('Integrated intensity of the frame (a.u.)')


def plot_metadata(files: List[Tuple[int, int]], metadata_key):
    prop = ed1.metadata.get_image_properties(*files[0], return_dict=False)

    properties = [ed1.metadata.get_image_properties(*f, return_dict=True)[metadata_key] for f in files]
    time_axis = get_time_axis(files)
    plt.plot(time_axis, properties, '.-')
    ax = plt.gca()
    ax.set_xlabel('Time (sec)')
    ylabel = prop[metadata_key].description if metadata_key != 'thickness' else 'Thickness'
    ax.set_ylabel(fr'{ylabel}, {prop[metadata_key].unit}')
    ax.grid(linestyle='--', linewidth=0.5)
    return time_axis, properties


def get_files_list(folder_num, num):
    folder_size = len(get_zaptime_files(folder_num))
    return [(folder_num, int(i)) for i in np.linspace(0, folder_size - 2, num)]


# def get_time_axis(files: List[Tuple[int, int]]):
#     def func(n):
#         try:
#             return ed0.metadata.get_image_properties(*n)['abs_time']
#         except KeyError as err:
#             print('Folder, file : ', n)
#             raise KeyError(err)
#     start = func(files[0])
#     return [func(n) - start for n in files]

# def get_temp_axis(files: List[Tuple[int, int]], key='temp_sample'):
#     def func(n):
#         try:
#             return ed0.metadata.get_image_properties(*n)[key].value
#         except KeyError as err:
#             print('Folder, file : ', n)
#             raise KeyError(err)
#     return [func(n) for n in files]

def show_roi(folder_number, file_number,
             x_region, y_region, gp, **kwargs):
    cut_x = Cut(x_region, axis=0)
    cut_y = Cut(y_region, axis=1)
    plot = PlotReport(folder_number, file_number, cut_x=cut_x,
                      cut_y=cut_y, gp=gp, **kwargs)

    fig3 = plt.figure(figsize=(30, 25))
    gs = fig3.add_gridspec(3, 3)
    f3_ax1 = fig3.add_subplot(gs[0:2, 1])
    f3_ax2 = fig3.add_subplot(gs[0, 0])
    f3_ax3 = fig3.add_subplot(gs[1, 0])

    plt.sca(f3_ax2)
    cut_x.plot_cut(df=plot.df)
    plt.sca(f3_ax3)
    cut_y.plot_cut(df=plot.df)
    plt.sca(f3_ax1)
    plot.plot_im(ax=f3_ax1)
    plt.subplots_adjust(hspace=0.25)


def get_cut_from_df(df, cut, axis, sigma=0, **kwargs):
    df = df.iloc[(df.index > cut[0]) * (df.index < cut[1]),
                 (df.columns > cut[2]) * (df.columns < cut[3])]

    axes = (df.columns, df.index)
    y = df.mean(axis=axis)
    if sigma > 0:
        y = gaussian_filter1d(y, sigma=sigma)
    x = axes[axis]
    return x, y


def get_cut(folder_num, file_num, cut, axis, sigma=0, **kwargs):
    df = ExtractData().get_images(folder_num, file_num,
                                  plot=False, **kwargs)

    return get_cut_from_df(df, cut, axis, sigma=sigma, **kwargs)


def compare_cuts(files: List[Tuple[int, int]], cut, axis, sigma=0, *,
                 substrate_file: Tuple[int, int] = None, logscale=True,
                 temp_axis_key=None, figsize=(7, 7), title: str = None, **kwargs):
    cut_list = list()

    if substrate_file is not None:
        x, substrate = get_cut(*substrate_file, cut, axis, sigma, **kwargs)

    if temp_axis_key is None:
        time_axis = get_time_axis(files)
    else:
        time_axis = get_temp_axis(files, temp_axis_key)
    cmap = get_cmap(time_axis)

    plt.figure(figsize=figsize)
    ax = plt.gca()
    for t, f in zip(time_axis, files):
        x, y = get_cut(*f, cut, axis, sigma, **kwargs)
        if substrate_file is not None:
            y -= substrate
        cut_list.append(y)
        if logscale:
            ax.semilogy(x, y, color=cmap.to_rgba(t))
        else:
            ax.plot(x, y, color=cmap.to_rgba(t))

    if axis == 0:
        ax.set_xlabel(r'$2 \theta$, deg')
    else:
        ax.set_xlabel(r'$\alpha$, deg')
    if logscale:
        ax.set_ylabel(r'$log(I)$')
    else:
        ax.set_ylabel(r'$I$')
    ax.grid(linestyle='--', linewidth=0.5)
    cbar = plt.colorbar(cmap)
    if temp_axis_key is None:
        cbar_label = 'Time (sec)'
    else:
        prop = ExtractData().metadata.get_image_properties(*files[0])[temp_axis_key]
        if temp_axis_key == 'thickness':
            prop.description = 'Thickness'
        cbar_label = f'{prop.description}, {prop.unit}'

    cbar.set_label(cbar_label)

    if title is not None:
        plt.title(title)
    elif axis == 0:
        horizontal_title(cut)
    else:
        vertical_title(cut)

    return cut_list


def plot_gisaxs(df, ax=None, colorbar=True):
    ax = ax if ax is not None else plt.gca()
    extent = ed1.get_extent(df)
    im = ax.imshow(df, extent=extent, cmap='jet')
    ax.set_xlabel(r'$2 \theta$, deg')
    ax.set_ylabel(r'$\alpha$, deg')
    if colorbar:
        cbar = plt.colorbar(im, fraction=0.046, pad=0.04)


#         cbar.set_label(r'$log(I)$')

def log_df(df, background=0.01):
    return np.log(np.clip(df, background, np.amax(df.values)))


def gisaxs_difference(file: Tuple[int, int], substrate_file: Tuple[int, int], plot=True, **kwargs):
    df = ed1.get_images(*file, apply_log=False, **kwargs)
    df_substrate = ed1.get_images(*substrate_file, apply_log=False, **kwargs)
    df_clean = df - df_substrate
    df_clean = log_df(df_clean)
    if plot:
        plt.figure(figsize=(10, 10))
        plot_gisaxs(df_clean)
    return df_clean


def get_rectangle(cut, props):
    return patches.Rectangle((cut[2], cut[0]), cut[3] - cut[2], cut[1] - cut[0], **props)


def get_title(file, title=None):
    title = title or 'Pentacene sample %d' % get_pen_folder_number(file[0])
    try:
        title = '%s%s(folder %d, image %d)' % (
            title,
            ed1.metadata.get_latex_title(*file),
            *file)
    except Exception as err:
        pass
    return title


def show_roi_diff(file: Tuple[int, int], substrate_file: Tuple[int, int],
                  x_region, y_region, **kwargs):
    sigma = kwargs.pop('sigma', 2)
    title = kwargs.pop('title', None)
    title = get_title(file, title)

    cut_x = Cut(x_region, axis=0, sigma=sigma)
    cut_y = Cut(y_region, axis=1, sigma=sigma)
    rectangle_props = dict(fill=False, color='red', alpha=1, lw=3, ls='--')

    rectangle_props.update(kwargs.pop('rect', dict()))

    df_original = ed1.get_images(*file, apply_log=True, background=0.1, **kwargs)
    df = gisaxs_difference(file, substrate_file, plot=False, **kwargs)

    fig3 = plt.figure(figsize=(30, 25))
    gs = fig3.add_gridspec(3, 3)
    f3_ax1 = fig3.add_subplot(gs[0:2, 1])
    f3_ax2 = fig3.add_subplot(gs[0, 0])
    f3_ax3 = fig3.add_subplot(gs[1, 0])

    r1 = get_rectangle(x_region, rectangle_props)
    r2 = get_rectangle(y_region, rectangle_props)

    plt.sca(f3_ax2)
    cut_x.plot_cut(df=df)
    plt.sca(f3_ax3)
    cut_y.plot_cut(df=df)
    plt.sca(f3_ax1)
    plot_gisaxs(df_original)
    f3_ax1.add_patch(r1)
    f3_ax1.add_patch(r2)
    plt.subplots_adjust(hspace=0.25)
    plt.title(title)


def get_simple_title(file):
    attrs = ed1.metadata.get_image_properties(*file)
    return '$T_{sample} = %.2f$ %s, $T_{pen} = %.2f$ %s, $d = %.1f$ %s\n(folder %d, image %d)' % \
           (attrs['temp_sample'].value, attrs['temp_sample'].unit,
            attrs['temp_evaporation'].value, attrs['temp_evaporation'].unit,
            attrs['thickness'].value, attrs['thickness'].unit,
            *file)


def get_very_simple_title(file, key):
    latex_dict = dict(temp_sample='$T_{sample} = %.2f$ %s',
                      temp_evaporation='$T_{pen} = %.2f$ %s',
                      thickness='$d = %.1f$ %s')
    attrs = ed1.metadata.get_image_properties(*file)

    title = latex_dict[key] % (attrs[key].value, attrs[key].unit)
    return title


def four_gisaxs_pics(files: List[Tuple[int, int]], figsize=(9, 9), key=None, regions=None, **kwargs):
    assert len(files) == 4, 'It is 4 GISAXS pics, man!'

    default_params = dict(apply_log=True, background=0.1,
                          x_range=(-0.2, 0.2), y_range=(0, 0.4))

    rectangle_props = dict(fill=False, color='red', alpha=1, lw=3, ls='--')
    rectangle_props.update(kwargs.pop('rect', dict()))
    default_params.update(kwargs)

    fig, axs = plt.subplots(2, 2, sharey=False, figsize=figsize)
    axs = axs.flatten()
    for i, (ax, file) in enumerate(zip(axs, files)):
        df = ed1.get_images(*file, plot=False, **default_params)
        if i == 1 or i == 3:
            ax.yaxis.tick_right()
        if i == 0 or i == 1:
            ax.xaxis.tick_top()
        extent = ed1.get_extent(df)
        im = ax.imshow(df, extent=extent, cmap='jet')
        if i == 2 or i == 3:
            ax.set_xlabel(r'$2 \theta$, deg')
        if i == 0 or i == 2:
            ax.set_ylabel(r'$\alpha$, deg')

        if key:
            label = get_very_simple_title(file, key)
            text = ax.text(0.5, 0.85, label,  # r'$T_$ nm', #% get_very_simple_title(file, key),
                           horizontalalignment='center',
                           verticalalignment='center',
                           transform=ax.transAxes, color='white', fontsize=18, weight='extra bold')
            text.set_bbox(dict(facecolor='black', alpha=0.65, edgecolor='black'))

        if regions is not None:
            for cut in regions:
                ax.add_patch(get_rectangle(cut, rectangle_props))

    plt.subplots_adjust(hspace=0, wspace=0.2)


def one_gisaxs_pic(file: Tuple[int, int], figsize=(9, 9), regions=None,
                   title: str = False, axis_off: bool = True, **kwargs):
    default_params = dict(apply_log=True, background=0.1,
                          x_range=(-0.2, 0.2), y_range=(0, 0.4))

    rectangle_props = dict(fill=False, color='red', alpha=1, lw=3, ls='--')
    rectangle_props.update(kwargs.pop('rect', dict()))
    rectangles = list()

    if regions is not None:
        for cut in regions:
            rectangles.append(get_rectangle(cut, rectangle_props))
    default_params.update(kwargs)

    fig = plt.figure(figsize=figsize)
    ax = plt.gca()
    df = ed1.get_images(*file, plot=False, **default_params)
    plot_gisaxs(df, ax, False)
    if title:
        ax.set_title(get_simple_title(file))
    for r in rectangles:
        ax.add_patch(r)
    plt.tight_layout()
    if axis_off:
        ax.set_axis_off()


def vertical_title(cut):
    plt.title(fr'Vertical cuts ' \
                  fr'$2 \theta = {cut[2]} .. {cut[3]}$ deg');


def horizontal_title(cut):
    plt.title(fr'Horizontal cuts ' \
                  fr'$\alpha = {cut[0]} .. {cut[1]}$ degree');


def plot_cut_fit(cut, p0=None, fit=True):
    """
    If fit is True, fits the cut with initial p0
    (or with predefined initial point if p0 is None) and plots the result of fitting.

    If fit is False, just plots cut with initial fitting function.
    """
    if fit:
        cut.fit.fit(x=cut.x, y=cut.y, p0=p0)
        p0 = cut.fit.fit_res[0]
    plt.figure(figsize=(10, 5))
    cut.fit.plot(x=cut.x, y=cut.y, args=p0)
    ax = plt.gca()
    ax.set_ylim([np.min(cut.y) * 0.95, np.max(cut.y) * 1.05])


def plot_simple_cut(file: Tuple[int, int],
                    cut: Tuple[float, float, float, float],
                    axis: int,
                    *,
                    sigma: float = 0,
                    logscale: bool = True,
                    title: str = None,
                    figsize: Tuple[int, int] = (8, 8)
                    ):
    df = ExtractData().get_images(*file, apply_log=False, x_range=cut[:2],
                                  y_range=cut[2:], plot=False)
    y = df.mean(axis=axis)
    x = (df.columns, df.index)[axis]
    if sigma > 0:
        y = gaussian_filter1d(y, sigma)
    plt.figure(figsize=figsize)
    if logscale:
        plt.semilogy(x, y)
    else:
        plt.plot(x, y)

    ax = plt.gca()
    if axis == 0:
        ax.set_xlabel(r'$2 \theta$, deg')
    else:
        ax.set_xlabel(r'$\alpha$, deg')
    if logscale:
        ax.set_ylabel(r'$log(I)$')
    else:
        ax.set_ylabel(r'$I$')
    ax.grid(linestyle='--', linewidth=0.5)

    if title is not None:
        plt.title(title)
    elif axis == 0:
        horizontal_title(cut)
    else:
        vertical_title(cut)
