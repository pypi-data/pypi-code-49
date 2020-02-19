import logging
import os
import pkg_resources

import torch
import torch.nn as nn
from torch.optim import lr_scheduler
import numpy as np
import pandas as pd
import tables
from ctapipe.instrument import CameraGeometry
from ctapipe.visualization import CameraDisplay
from astropy import units as u
from PIL import Image
from torchvision import transforms
import torchvision.utils as t_utils
from indexedconv.engine import IndexedConv
import indexedconv.utils as cvutils
from ctaplot import ana

import gammalearn.utils as utils
import gammalearn.criterions as criterions
import gammalearn.datasets as dsets

import matplotlib as mpl
mpl.use('Agg')  # Because of an issue in Qt5 causing seg fault
import matplotlib.pyplot as plt


class RunConfigDescription(tables.IsDescription):
    num_showers = tables.Int32Col()
    shower_reuse = tables.Int32Col()
    spectral_index = tables.Float64Col()
    max_scatter_range = tables.Float64Col()
    energy_range_max = tables.Float64Col()
    energy_range_min = tables.Float64Col()
    min_alt = tables.Float64Col()
    max_alt = tables.Float64Col()


def create_send_log_vars_to_tensorboard_mt(experiment):
    """
    Handler to send loss to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)
    try:
        assert isinstance(experiment.compute_loss, criterions.MultilossBalancing)
    except AssertionError as err:
        logger.exception('Plotting log vars works only with Multilossbalancing !')
    log_vars = experiment.compute_loss.log_vars

    def send_log_vars_loss(engine):

        vars_dict = {}
        for i, task in enumerate(experiment.targets.keys()):
            vars_dict['Logvar_' + task] = log_vars[i]
        experiment.tensorboard_writer.add_scalars('Log_vars', vars_dict, global_step=engine.state.epoch)

    return send_log_vars_loss


def create_send_gradnorm_weights_to_tensorboard_mt(experiment):
    """
    Handler to send loss to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)
    try:
        assert isinstance(experiment.compute_loss, criterions.GradNormBalancing)
    except AssertionError as err:
        logger.exception('Plotting gradnorm weights works only with GradNormBalancing !')
    weights = experiment.compute_loss.weights

    def send_weights(engine):
        if engine.state.iteration % experiment.save_every == 0:
            weights_dict = {}
            for i, task in enumerate(experiment.targets.keys()):
                weights_dict['Gradnorm_w_' + task] = weights[i]
            experiment.tensorboard_writer.add_scalars('Gradnorm_weights', weights_dict,
                                                      global_step=engine.state.iteration)

    return send_weights


def create_send_pareto_scales_to_tensorboard_mt(experiment):
    """
    Handler to send loss to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)

    def send_scales(engine):
        scales_dict = {}
        for i, task in enumerate(experiment.targets.keys()):
            scales_dict['Scale ' + task] = experiment.pareto_scales[i]
        experiment.tensorboard_writer.add_scalars('Pareto_scales', scales_dict, global_step=engine.state.epoch)

    return send_scales


def create_send_model_parameters_to_tensorboard(experiment):
    """
    Handler to send histograms of the weights of the network to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)

    def send_model_parameters(engine):
        for name, param in experiment.net.named_parameters():
            experiment.tensorboard_writer.add_histogram(name, param.clone().cpu().data,
                                                        bins='sqrt',
                                                        global_step=engine.state.epoch)
    return send_model_parameters


def create_send_model_weights_to_tensorboard(experiment):
    """
    Handler to send sum of squared weigths of the network to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    def send_model_parameters(engine):
        weights = 0
        for name, param in experiment.net.named_parameters():
            if 'weight' in name:
                weights += torch.sum(param.data ** 2)
        experiment.tensorboard_writer.add_scalar('weights', weights, global_step=engine.state.epoch)
    return send_model_parameters


def create_send_model_param_weights_to_tensorboard(experiment):
    """
    Handler to send sum of squared weigths of the network to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer
    """
    def send_model_parameters(engine):
        """

        Parameters
        ----------
        trainer (ignite.Trainer)

        Returns
        -------

        """
        weights = {}
        for name, param in experiment.net.named_parameters():
            if 'weight' in name:
                weights[name] = torch.sum(param.data ** 2)
            experiment.tensorboard_writer.add_scalars('Param_weights', weights, global_step=engine.state.iteration)

    return send_model_parameters


def make_activation_sender(writer, name, global_step):
    """
    Creates the adapted activations sender to tensorboard
    Parameters
    ----------
    writer (SummaryWriter): the tensorboardX writer
    name (string) : name of the module
    global_step (int): the step (eg epoch, iteration...)

    Returns
    -------
    An adapted function
    """
    logger = logging.getLogger(__name__)

    def send(m, input, output):
        """
        The function to send the activation of a module to tensorboard
        Parameters
        ----------
        m (nn.Module): the module (eg nn.ReLU, ...)
        input
        output

        Returns
        -------

        """
        writer.add_histogram(name, output.clone().cpu().data, bins='sqrt', global_step=global_step)
        logger.debug('{} : activation histogram sent !'.format(name))

    return send


def create_hook_relu_activation(experiment):
    """
    Creates the function to place a hook on relu activations
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)

    def hook_relu_activation(engine):
        if engine.state.iteration == 1:
            logger.debug('Activation hook : look for relu ')
            for name, child in experiment.net.named_children():
                logger.debug(name)
                if isinstance(child, nn.ReLU):
                    logger.debug('Activation hook : found ', name)
                    sender = make_activation_sender(experiment.tensorboard_writer, name, engine.state.iteration)
                    experiment.hooks[name] = child.register_forward_hook(sender)

    return hook_relu_activation


def create_remove_hook_relu_activation(experiment):
    """
    Creates the function to remove hooks on relu activations
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)

    def remove_hook_relu_activation(engine):
        if engine.state.iteration == 1:
            for key in experiment.hooks.keys():
                if 'relu' in key:
                    experiment.hooks[key].remove()

    return remove_hook_relu_activation


def make_grad_sender(writer, name, global_step):
    """
    Creates the gradient sender to tensorboard
    Parameters
    ----------
    writer (SummaryWriter): the tensorboardX writer
    name (string) : name of the module
    global_step (int): the step (eg epoch, iteration...)

    Returns
    -------
    An adapted function
    """
    logger = logging.getLogger(__name__)

    def send(m, grad_input, grad_output):
        logger.debug('{} grad_in min : {}, max : {}, norm : {}'.format(name, grad_input[0].data.min(),
                                                                      grad_input[0].data.max(),
                                                                      grad_input[0].data.norm()))
        writer.add_histogram(name + 'grad_in', grad_input[0].data.cpu(), bins='sqrt', global_step=global_step)
        logger.debug('{} : gradient histogram sent !'.format(name))

    return send


def create_hook_gradient(experiment):
    """
    Creates the function to place hooks on Linear layers
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)

    def hook_lin_grad(engine):

        logger.debug('Gradient hook : look for linear ')
        for name, child in experiment.net.named_modules():
            logger.debug(name)
            if isinstance(child, nn.Linear):
                logger.debug('Gradient hook : found ', name)
                sender = make_grad_sender(experiment.tensorboard_writer, name, engine.state.iteration)
                experiment.hooks['grad_' + name] = child.register_backward_hook(sender)

    return hook_lin_grad


def create_remove_hook_linear_grad(experiment):
    """
    Creates the function to remove hooks on Linear gradients
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer

    """
    logger = logging.getLogger(__name__)

    def remove_hook_linear_grad(engine):
        logger.debug('linear grad hook remove function')
        for key in experiment.hooks.keys():
            logger.debug('hook : {}'.format(key))
            if 'grad' in key:
                experiment.hooks[key].remove()
                logger.debug('hook {} removed'.format(key))

    return remove_hook_linear_grad


def create_send_features_to_tensorboard(experiment):
    """

    Parameters
    ----------
    experiment

    Returns
    -------

    """
    logger = logging.getLogger(__name__)

    nice_input = np.load(pkg_resources.resource_filename(__name__, 'data/nice_lst.npy'))
    logger.debug('nice input {}'.format(nice_input.shape))
    # nice_input = np.array([nice_input, nice_input, nice_input])
    dummy_input = torch.from_numpy(nice_input[0]).unsqueeze(0).unsqueeze(0).unsqueeze(0)
    dummy_input = dummy_input.to(experiment.device)

    def send_features(engine):
        logger.info('Plot feature images')
        ax = plt.axes()
        ax.set_aspect('equal', 'datalim')
        epoch = engine.state.epoch
        experiment.net.plot_mode = True
        experiment.net.eval()
        features = experiment.net(dummy_input)
        geom = CameraGeometry.guess(list(map(lambda x: x[1], experiment.net.pixels_position)) * u.m,
                                    list(map(lambda x: x[0], experiment.net.pixels_position)) * u.m,
                                    28 * u.m,
                                    apply_derotation=False)
        for j, f in enumerate(features):
            # logger.info('feature : {}'.format(f[0].data))
            images_list = []
            if isinstance(f, tuple):
                images = f[0].data
                logger.debug('indx_mtx shape {}'.format(f[1].shape))
                pix_pos = cvutils.build_hexagonal_position(f[1].squeeze().squeeze())
                geom = CameraGeometry.guess(list(map(lambda x: x[1], pix_pos)) * u.m,
                                            list(map(lambda x: x[0], pix_pos)) * u.m,
                                            28 * u.m,
                                            apply_derotation=False)
            else:
                images = f.data

            for i in range(images.shape[1]):
                ax.clear()
                disp = CameraDisplay(geom)
                disp.image = images[0, i].squeeze()
                canvas = plt.get_current_fig_manager().canvas
                canvas.draw()
                pil_img = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
                images_list.append(transforms.ToTensor()(pil_img))

            grid = t_utils.make_grid(images_list)

            experiment.tensorboard_writer.add_image('Features_{}'.format(j), grid, epoch)
        experiment.net.plot_mode = False

    return send_features


def create_send_kernels_to_tensorboard(experiment):
    """

    Parameters
    ----------
    experiment

    Returns
    -------

    """
    logger = logging.getLogger(__name__)
    if experiment.net.conv_kernel == 'Pool':
        kernel = np.ones((2, 2), dtype=bool)
    elif experiment.net.conv_kernel == 'Hex_2':
        kernel = np.ones((5, 5), dtype=bool)
        kernel[0, 3:5] = False
        kernel[1, 4] = False
        kernel[3:5, 0] = False
        kernel[4, 1] = False

    else:
        kernel = np.ones((3, 3), dtype=bool)
        if experiment.net.conv_kernel == 'Hex':
            kernel[0, 2] = False
            kernel[2, 0] = False
    idx = 0
    index_matrix = np.ones(kernel.shape) * -1
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            if kernel[i, j]:
                index_matrix[i, j] = idx
                idx += 1
    pix_pos = cvutils.build_hexagonal_position(index_matrix)
    geom = CameraGeometry.guess(list(map(lambda x: x[1], pix_pos)) * u.m,
                                list(map(lambda x: x[0], pix_pos)) * u.m,
                                28 * u.m,
                                apply_derotation=False)

    def send_kernels(engine):

        epoch = engine.state.epoch
        ax = plt.axes()
        ax.set_aspect('equal', 'datalim')
        for name, child in experiment.net.named_children():
            logger.debug(name)
            if isinstance(child, IndexedConv):
                # logger.debug('Activation hook : found ', name)
                for name_p, parameter in child.named_parameters():
                    if name_p == 'weight':
                        k_name = name_p
                        conv_weight = parameter
                logger.debug('layer {} kernel {}'.format(k_name, kernel.shape))
                images_list = []
                for i in range(conv_weight.shape[0]):
                    kernel_vec = torch.sum(conv_weight[i], 0)  # TODO plot the kernel with max total value
                    logger.debug('kernel {} shape {}'.format(i, kernel_vec.shape))
                    ax.clear()
                    disp = CameraDisplay(geom)
                    disp.image = kernel_vec.detach()
                    canvas = plt.get_current_fig_manager().canvas
                    canvas.draw()
                    pil_img = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
                    images_list.append(transforms.ToTensor()(pil_img))

                grid = t_utils.make_grid(images_list)

                experiment.tensorboard_writer.add_image('Kernel_{}'.format(name), grid, epoch)

    return send_kernels


def create_send_gpu_usage_to_tensorboard(experiment):
    """
    Handler to send the gpu usage to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)

    def send_gpu_usage(engine):
        """

        Parameters
        ----------
        trainer (ignite.Trainer)

        Returns
        -------

        """
        logger.debug('gpu_history : {}'.format(experiment.gpu_history))
        experiment.tensorboard_writer.add_scalars('GPU_memory', {'used': experiment.gpu_history.simple_moving_average(
            window_size=len(experiment.gpu_history), transform=lambda x: x[0])}, global_step=engine.state.epoch)
        experiment.tensorboard_writer.add_scalars('GPU_memory', {'total': experiment.gpu_history.simple_moving_average(
            window_size=len(experiment.gpu_history), transform=lambda x: x[1])}, global_step=engine.state.epoch)
        experiment.tensorboard_writer.add_scalar('GPU_utilization', experiment.gpu_history.simple_moving_average(
            window_size=len(experiment.gpu_history), transform=lambda x: x[2]), global_step=engine.state.epoch)
        experiment.gpu_history.clear()

    return send_gpu_usage


def create_send_gradient_norm_to_tensorboard(experiment):
    """
    Handler to send the gradient total norm to tensorboard
    Parameters
    ----------
    experiment (Experiment): the experiment
    Returns
    -------
    A function registrable by ignite Trainer
    """

    def send_gradient_norm(engine):
        """

        Parameters
        ----------
        trainer (ignite.Trainer)

        Returns
        -------

        """
        norm = 0
        for p in list(filter(lambda p: p.grad is not None, experiment.net.parameters())):
            norm += p.grad.data.norm(2).item()**2
        norm = norm**(1./2)

        experiment.tensorboard_writer.add_scalar('Gradient_norm', norm, global_step=engine.state.epoch)

    return send_gradient_norm


def create_save_model_handler(experiment):
    """
    Handler to save the model parameters
    Parameters
    ----------
    experiment (Experiment): the experiment

    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)

    def save_model(engine):

        if (engine.state.epoch % experiment.save_every) == 0 or engine.state.epoch == experiment.nepochs:
            logger.info('Epoch {} : saved model checkpoint'.format(engine.state.epoch))
            torch.save(experiment.net.state_dict(),
                       f='{}/{}/checkpoint_{}.tar'.format(experiment.main_directory,
                                                          experiment.experiment_name,
                                                          engine.state.epoch))

    return save_model


def create_lr_plateau_scheduler_regression_handler(experiment, **options):
    """
    Handler to update the learning rate with the Reduce on plateau method
    Parameters
    ----------
    experiment (Experiment):

    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)
    schedulers = {}

    for net_param, param in options.items():
        if experiment.optimizers[net_param] is not None:
            try:
                factor = param['factor']
            except KeyError as e:
                logger.warning('Plateau LR scheduler needs a factor parameter. Setting default value to 0.1')
                logger.error(e)
                factor = 0.1
            try:
                patience = param['patience']
            except (TypeError, KeyError) as e:
                logger.warning('Plateau LR scheduler needs a patience parameter. Setting default value to 10')
                logger.error(e)
                patience = 30

            schedulers[net_param] = lr_scheduler.ReduceLROnPlateau(experiment.optimizers[net_param],
                                                                   factor=factor,
                                                                   patience=patience)

    def update_lr(engine):
        metrics = engine.state.metrics
        total_loss = 0
        for n, m in metrics.items():
            if 'Loss' in n:
                total_loss += m

        for name, scheduler in schedulers.items():
            scheduler.step(total_loss)
            logger.info('{} learning rate : {}'.format(name, [group['lr'] for group in scheduler.optimizer.param_groups]))

    return update_lr


def create_lr_step_scheduler_handler(experiment, **options):
    """
    Handler to update the learning rate with the step method
    Parameters
    ----------
    experiment (Experiment):

    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)
    schedulers = {}

    for net_param, param in options.items():
        if experiment.optimizers[net_param] is not None:

            try:
                gamma = param['gamma']
            except (TypeError, KeyError) as e:
                logger.warning('Step LR scheduler needs a gamma parameter. Setting default value to 0.1')
                logger.error(e)
                gamma = 0.1

            try:
                step_size = param['step_size']
            except (TypeError, KeyError) as e:
                logger.warning('Step LR scheduler needs a step size parameter. Setting default value to 30')
                logger.error(e)
                step_size = 30

            schedulers[net_param] = lr_scheduler.StepLR(experiment.optimizers[net_param],
                                                        step_size=step_size,
                                                        gamma=gamma)

    def update_lr(engine):
        for name, scheduler in schedulers.items():
            scheduler.step()
            logger.info('{} learning rate : {}'.format(name, [group['lr'] for group in scheduler.optimizer.param_groups]))

    return update_lr


def create_lr_multistep_scheduler_handler(experiment, **options):
    """
    Handler to update the learning rate with the step method
    Parameters
    ----------
    experiment (Experiment):

    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)
    schedulers = {}

    for net_param, param in options.items():
        if experiment.optimizers[net_param] is not None:

            try:
                gamma = param['gamma']
            except (TypeError, KeyError) as e:
                logger.warning('Step LR scheduler needs a gamma parameter. Setting default value to 0.1')
                logger.error(e)
                gamma = 0.1

            try:
                milestones = param['milestones']
            except (TypeError, KeyError) as e:
                logger.warning('MultiStep LR scheduler needs the list of milestones. Setting default value to [50%, 75%]')
                logger.error(e)
                milestones = [experiment.nepochs // 2, 3 * experiment.nepochs // 4]

            schedulers[net_param] = lr_scheduler.MultiStepLR(experiment.optimizers[net_param],
                                                             milestones=milestones,
                                                             gamma=gamma)

    def update_lr(engine):
        for name, scheduler in schedulers.items():
            scheduler.step()
            logger.info('{} learning rate : {}'.format(name, [group['lr'] for group in scheduler.optimizer.param_groups]))

    return update_lr


def create_regularization_multistep_handler(experiment, **options):
    """
    Handler to update the regularization coefficient
    Parameters
    ----------
    experiment (Experiment):

    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)
    if options is not None:
        try:
            milestones = options['milestones']
        except (TypeError, KeyError) as e:
            logger.warning('MultiStep regularization needs a list of milestones. Setting default value to [20, 50, 70]')
            logger.error(e)
            milestones = [20, 50, 70]
        try:
            coefficient = options['lambda']
        except (TypeError, KeyError) as e:
            logger.warning('MultiStep regularization needs the list of coefficient. Setting default value to [1e-3, 1e-4, 1e-6]')
            logger.error(e)
            coefficient = [1e-3, 1e-4, 1e-6]

    def update_regularization(engine):
        if engine.state.trainer_epoch == milestones[0]:
            experiment.regularization['weight'] = coefficient[0]
            milestones.pop(0)
            coefficient.pop(0)

    return update_regularization


def create_lr_exponential_scheduler_handler(experiment, **options):
    """
    Handler to update the learning rate
    Parameters
    ----------
    experiment (Experiment):

    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)
    schedulers = {}

    for net_param, param in options.items():
        if experiment.optimizers[net_param] is not None:

            try:
                gamma = param['gamma']
            except (TypeError, KeyError) as e:
                logger.warning('Exponential LR scheduler needs a gamma parameter. Setting default value to 0.9')
                logger.error(e)
                gamma = 0.9

            schedulers[net_param] = lr_scheduler.ExponentialLR(experiment.optimizers[net_param], gamma)

    def update_lr(engine):
        for name, scheduler in schedulers.items():
            scheduler.step(engine.state.trainer_epoch)
            logger.info('{} learning rate : {}'.format(name, [group['lr'] for group in scheduler.optimizer.param_groups]))

    return update_lr


def create_write_gammaboard_files(experiment):
    """
        Creates the function to handle testing result data
        Parameters
        ----------
        experiment (Experiment)

        Returns
        -------
        A function registrable by ignite Trainer
        """
    assert experiment.test, 'The gammaboard file is the result of the test process'
    # TODO update with targets

    def write_gammaboard_files(engine):
        """

        Parameters
        ----------
        trainer

        Returns
        -------

        """
        data_pd = pd.DataFrame()
        gb_file_path = experiment.main_directory + '/' + experiment.experiment_name + '/' + \
                       experiment.experiment_name + '.h5'
        if os.path.exists(gb_file_path):
            os.remove(gb_file_path)

        # Retrieve MC information
        mc_energies = []
        num_showers = []
        shower_reuse = []
        spectral_index = []
        max_scatter_range = []
        energy_range_max = []
        energy_range_min = []
        min_alt = []
        max_alt = []
        particleness = []
        # targets = []

        def fetch_dataset_info(d):
            if isinstance(d, torch.utils.data.ConcatDataset):
                for d_c in d.datasets:
                    fetch_dataset_info(d_c)
            elif isinstance(d, dsets.Subset):
                fetch_dataset_info(d.dataset)
            else:
                particleness.append(d.particle)
                if d.particle == 'hadroness' and d.particle_types[0] == 0 or \
                        d.particle == 'gammaness' and d.particle_types[0] == 1:
                    num_showers.extend([d.num_showers])
                    shower_reuse.extend([d.shower_reuse])
                    spectral_index.extend([d.spectral_index])
                    max_scatter_range.extend([d.max_scatter_range])
                    energy_range_max.extend([d.energy_range_max])
                    energy_range_min.extend([d.energy_range_min])
                    min_alt.extend([d.min_alt])
                    max_alt.extend([d.max_alt])
                    en_mask = np.full(d.telescope_ids.shape[0], True, dtype=bool)
                    for param in experiment.data_filter['parameter']:
                        if 'tel_id' in param.keys():
                            en_mask = np.bitwise_and(en_mask, (d.telescope_ids == param['tel_id']))
                        if 'multiplicity' in param.keys():
                            en_mask = np.bitwise_and(en_mask, (d.multiplicity == param['multiplicity']))
                    mc_energies.extend(d.energies[en_mask])
                    # targets.append(d.targets)

        if experiment.dataset_class == dsets.UCMCamDataset:
            fetch_dataset_info(experiment.test_loader.dataset)

            mc_energies = np.array(mc_energies)
            num_showers = np.array(num_showers)
            shower_reuse = np.array(shower_reuse)
            spectral_index = np.array(spectral_index)
            max_scatter_range = np.array(max_scatter_range)
            energy_range_max = np.array(energy_range_max)
            energy_range_min = np.array(energy_range_min)
            min_alt = np.array(min_alt)
            max_alt = np.array(max_alt)
            if not experiment.split_by_file and experiment.test_folders is None:
                np.random.shuffle(mc_energies)
                mc_energies = mc_energies[:int(len(mc_energies) * experiment.validating_ratio)]
                num_showers = num_showers * experiment.validating_ratio

        # def fetch_old_dataset_info(d):
        #     if isinstance(d, torch.utils.data.ConcatDataset):
        #         for d_c in d.datasets:
        #             fetch_old_dataset_info(d_c)
        #     elif isinstance(d, dsets.Subset):
        #         fetch_old_dataset_info(d.dataset)
        #     else:
        #         particleness.append(d.particle)
        #         if d.particle == 'hadroness' and d.particle_types[0] == 0 or \
        #                 d.particle == 'gammaness' and d.particle_types[0] == 1:
        #             targets.append(d.targets)
        # if experiment.dataset_class == dsets.UCMCamDatasetOld:
        #     fetch_old_dataset_info(experiment.test_loader.dataset)
        #     targets = targets[0]

        # Retrieve test data
        metrics = engine.state.metrics
        outputs = metrics['outputs']
        labels = metrics['labels']
        mc_energy = metrics['mc_energy']
        tel_info = metrics['tel_info']
        tel_position = tel_info[:, 2:].numpy()
        tel_altitude = tel_info[:, 0].numpy()
        tel_azimuth = tel_info[:, 1].numpy()
        outputs = outputs.numpy()
        labels = labels.numpy()
        data_pd['mc_energy'] = 10 ** mc_energy
        i = 0
        for j, obj in enumerate(experiment.targets):
            if obj == 'energy':
                data_pd['reco_energy'] = 10 ** outputs[:, i]

                i += 1
            elif obj == 'xmax':
                data_pd['mc_xmax'] = labels[:, i]
                data_pd['reco_xmax'] = outputs[:, i]

                i += 1
            elif obj == 'class':
                data_pd['mc_particle'] = labels[:, i].astype(int)
                data_pd['reco_particle'] = np.argmax(outputs[:, i:], 1)
                data_pd['reco_' + particleness[0]] = np.exp(outputs[:, i+1])  # Networks return logsoftmax
            else:
                if obj == 'direction':
                    data_pd['mc_altitude'] = labels[:, i]
                    data_pd['mc_azimuth'] = labels[:, i+1]
                    data_pd['reco_altitude'] = outputs[:, i]
                    data_pd['reco_azimuth'] = outputs[:, i+1]
                    if experiment.targets[obj]['unit'] == 'degrees':
                        data_pd['mc_altitude'] /= (180 / np.pi)
                        data_pd['mc_azimuth'] /= (180 / np.pi)
                        data_pd['reco_altitude'] /= (180 / np.pi)
                        data_pd['reco_azimuth'] /= (180 / np.pi)
                    data_pd['mc_altitude'] += tel_altitude
                    data_pd['mc_azimuth'] += tel_azimuth
                    data_pd['reco_altitude'] += tel_altitude
                    data_pd['reco_azimuth'] += tel_azimuth

                elif obj == 'impact':
                    data_pd['mc_impact_x'] = labels[:, i] + tel_position[:, 0]
                    data_pd['mc_impact_y'] = labels[:, i+1] + tel_position[:, 1]
                    data_pd['reco_impact_x'] = outputs[:, i] + tel_position[:, 0]
                    data_pd['reco_impact_y'] = outputs[:, i+1] + tel_position[:, 1]

                i += 2
        data_pd.to_hdf(gb_file_path, key='data')

        if experiment.dataset_class == dsets.UCMCamDataset:

            pd.DataFrame({'mc_trig_energies': mc_energies}).to_hdf(gb_file_path, key='triggered_events')

            # Write mc info to gammaboard file
            gb_file = tables.open_file(gb_file_path, mode='a')
            gb_file.create_group('/', 'simulation')
            rc_tab = gb_file.create_table('/simulation', 'run_config', description=RunConfigDescription)
            for i in range(len(num_showers)):
                rc_tab.row['num_showers'] = num_showers[i]
                rc_tab.row['shower_reuse'] = shower_reuse[i]
                rc_tab.row['spectral_index'] = spectral_index[i]
                rc_tab.row['max_scatter_range'] = max_scatter_range[i]
                rc_tab.row['energy_range_max'] = energy_range_max[i]
                rc_tab.row['energy_range_min'] = energy_range_min[i]
                rc_tab.row['min_alt'] = min_alt[i]
                rc_tab.row['max_alt'] = max_alt[i]
                rc_tab.row.append()
            gb_file.flush()
            gb_file.close()

    return write_gammaboard_files


def create_send_resolution_to_tensorboard(experiment):
    """
        Handler to send some point of energy and angular resolution on validation set to tensorboard
        Parameters
        ----------
        experiment (Experiment): the experiment
        Returns
        -------
        A function registrable by ignite Trainer
        """

    def send_resolution(engine):
        """

        Parameters
        ----------
        trainer (ignite.Trainer)

        Returns
        -------

        """
        metrics = engine.state.metrics
        outputs = metrics['outputs'].numpy()
        labels = metrics['labels'].numpy()
        mc_energy = 10 ** metrics['mc_energy'].numpy()
        tel_info = metrics['tel_info']
        tel_altitude = tel_info[:, 0].numpy()
        tel_azimuth = tel_info[:, 1].numpy()
        gamma_mask = np.full(len(mc_energy), True)
        i = 0
        for obj in experiment.targets:
            if obj == 'class':
                mc_particle = labels[:, i].astype(int)
                print(mc_particle)
                gamma_mask = mc_particle == 1
                i += 2
            if obj == 'energy':
                i += 1
            else:
                i += 2
        print(gamma_mask)

        i = 0
        for j, obj in enumerate(experiment.targets):
            if obj == 'energy':
                reco_energy = 10 ** outputs[:, i]
                _, res_en = ana.energy_resolution_per_energy(mc_energy[gamma_mask], reco_energy[gamma_mask])
                print(res_en)
                experiment.tensorboard_writer.add_scalars('Energy_resolution_validating',
                                                          {'R68_30GeV': res_en[0, 0],
                                                           'R68_130GeV': res_en[3, 0],
                                                           'R68_1.25TeV': res_en[8, 0],
                                                           'R68_3.2TeV': res_en[10, 0]
                                                           },
                                                          global_step=engine.trainer_epoch)
                i += 1
            else:
                if obj == 'direction':
                    mc_altitude = labels[:, i]
                    mc_azimuth = labels[:, i + 1]
                    reco_altitude = outputs[:, i]
                    reco_azimuth = outputs[:, i + 1]
                    if experiment.targets[obj]['unit'] == 'degrees':
                        mc_altitude /= (180 / np.pi)
                        mc_azimuth /= (180 / np.pi)
                        reco_altitude /= (180 / np.pi)
                        reco_azimuth /= (180 / np.pi)
                    mc_altitude += tel_altitude
                    mc_azimuth += tel_azimuth
                    reco_altitude += tel_altitude
                    reco_azimuth += tel_azimuth

                    _, res_an = ana.angular_resolution_per_energy(reco_altitude[gamma_mask], reco_azimuth[gamma_mask],
                                                                  mc_altitude[gamma_mask], mc_azimuth[gamma_mask],
                                                                  mc_energy[gamma_mask])
                    experiment.tensorboard_writer.add_scalars('Angular_resolution_validating',
                                                              {'R68_30GeV': res_an[0, 0],
                                                               'R68_130GeV': res_an[3, 0],
                                                               'R68_1.25TeV': res_an[8, 0],
                                                               'R68_3.2TeV': res_an[10, 0]
                                                               },
                                                              global_step=engine.trainer_epoch)

                i += 2

    return send_resolution


def create_store_gpu_history(experiment):
    """
    Handler to store gpu utilization
    Parameters
    ----------
    experiment (Experiment)

    Returns
    -------
    A function registrable by ignite Trainer
    """
    logger = logging.getLogger(__name__)

    def store_gpu_history(engine):
        if engine.state.iteration % experiment.gpu_frequency == 0:
            gpu_usage = utils.get_gpu_usage_map(experiment.device.index)
            experiment.gpu_history.append([item for key, item in gpu_usage.items()])

    return store_gpu_history

