import os
import random
import warnings
import math
import numpy as np
from ..callbacks import CallbackBase
from ..backend.common import *
from ..backend.load_backend import get_backend
from ..data.image_common import *
from ..misc.visualization_utils import *

if get_backend() == 'pytorch':
    import torch
    import torch.nn as nn
    from ..backend.pytorch_backend import to_numpy, to_tensor, ReplayBuffer
    from ..backend.pytorch_ops import binary_crossentropy, shuffle, random_choice
    from ..optims.pytorch_losses import CrossEntropyLoss, MSELoss
    from ..optims.pytorch_constraints import min_max_norm
    from ..optims.pytorch_trainer import *
    from ..layers.pytorch_activations import *
elif get_backend() == 'tensorflow':
    from ..backend.tensorflow_backend import to_numpy, to_tensor, ReplayBuffer
    from ..optims.tensorflow_losses import CrossEntropyLoss, MSELoss
    from ..optims.tensorflow_constraints import min_max_norm
    from ..optims.tensorflow_trainer import *
elif get_backend() == 'cntk':
    from ..backend.cntk_backend import to_numpy, to_tensor, ReplayBuffer
    from ..optims.cntk_losses import CrossEntropyLoss, MSELoss
    from ..optims.cntk_constraints import min_max_norm
    from ..optims.cntk_trainer import *

__all__ = ['GanCallbacksBase', 'GanCallback']


class GanCallbacksBase(CallbackBase):
    def __init__(self):
        super(GanCallbacksBase, self).__init__(is_shared=True)

    pass


def pullaway_loss(embeddings):
    norm = torch.sqrt(torch.sum(embeddings ** 2, -1, keepdim=True))
    normalized_emb = embeddings / norm
    similarity = torch.matmul(normalized_emb, normalized_emb.transpose(1, 0))
    batch_size = embeddings.size(0)
    loss_pt = (torch.sum(similarity) - batch_size) / (batch_size * (batch_size - 1))
    return loss_pt


class GanCallback(GanCallbacksBase):

    def __init__(self, generator=None, discriminator=None, gan_type='gan', label_smoothing=False, noisy_labels=False,
                 noised_real=True, noise_intensity=0.05, weight_clipping=False, tile_image_frequency=100,
                 experience_replay=False, use_total_variation=False, use_ttur=False,  # two timel-scale update rule
                 g_train_frequency=1, d_train_frequency=1, **kwargs):
        _available_gan_type = ['gan', 'began', 'ebgan', 'wgan', 'wgan-gp', 'lsgan', 'lsgan1', 'rasgan']
        super(GanCallback, self).__init__()
        if isinstance(generator, ImageGenerationModel):
            self.generator = generator.model
        if isinstance(discriminator, ImageClassificationModel):
            self.discriminator = discriminator.model
        self.training_items = None
        self.data_provider = None
        self.z_noise = None
        self.D_real = None
        self.D_fake = None
        self.D_metric = None
        self.G_metric = None
        self.img_real = None
        self.img_fake = None
        self.gan_type = gan_type if gan_type in _available_gan_type else None
        self.label_smoothing = label_smoothing
        self.noisy_labels = noisy_labels
        self.noised_real = noised_real
        self.noise_intensity = noise_intensity
        self.tile_image_frequency = tile_image_frequency
        self.weight_clipping = weight_clipping
        self.experience_replay = experience_replay
        self.g_train_frequency = g_train_frequency
        self.d_train_frequency = d_train_frequency
        if self.experience_replay == True:
            make_dir_if_need('Replay')
        self.tile_images = []
        self.use_total_variation = use_total_variation
        self.generator_first = None
        self.cooldown_counter = 0
        self.beginning_repository = ReplayBuffer(max_size=250)
        self.latter_repository = ReplayBuffer(max_size=250)
        self.generator_worse_metric = None
        self.discriminator_worse_metric = None
        self.generator_best_metric = None
        self.discriminator_best_metric = None
        self.generator_best_epoch = None
        self.discriminator_best_metric = None
        self.noise_end_epoch = 20

    def on_training_start(self, training_context):
        self.training_items = training_context['training_items']
        self.data_provider = training_context['_dataloaders'].value_list[0]
        for k, training_item in self.training_items.items():
            if self.generator is not None and training_item.model.name == self.generator.name:
                training_item.training_context['gan_role'] = 'generator'
            elif isinstance(training_item, ImageGenerationModel) or training_item.model.name == 'generator':
                if self.generator is None:
                    self.generator = training_item.model
                    training_item.training_context['gan_role'] = 'generator'
            elif self.discriminator is not None and training_item.model.name == self.discriminator.name:
                training_item.training_context['gan_role'] = 'discriminator'
            elif isinstance(training_item, ImageClassificationModel) or training_item.model.name == 'discriminator':
                if self.discriminator is None:
                    self.discriminator = training_item.model
                    training_item.training_context['gan_role'] = 'discriminator'
        if self.training_items.value_list[0].training_context['gan_role'] == 'generator':
            self.generator_first = True
            print('generator first')
        else:
            self.generator_first = False
            print('discriminator first')

    def on_data_received(self, training_context):
        try:
            if training_context['gan_role'] == 'generator':
                self.z_noise = training_context['current_input']
                if self.D_real  is None:
                    self.img_real = training_context['current_target']
                    self.D_real = self.discriminator(self.img_real)
                self.img_fake = self.generator(self.z_noise)
                self.D_fake = self.discriminator(self.img_fake)


            elif training_context['gan_role'] == 'discriminator':
                # training_context['img_real']=training_context['current_input']

                curr_epochs = training_context['current_epoch']
                tot_epochs = training_context['total_epoch']
                self.img_real = training_context['current_input']
                self.img_real.requires_grad=True
                if self.z_noise is None:
                    noise_shape = self.generator.input_shape.tolist()
                    noise_shape.insert(0, self.img_real.size(0))
                    self.z_noise = to_tensor(np.random.standard_normal(noise_shape))
                if self.img_fake is None:
                    self.img_fake = to_tensor(to_numpy(self.generator(self.z_noise)))

                if self.experience_replay:
                    self.img_fake = self.beginning_repository.push_and_pop(self.img_fake)

                if self.noisy_labels and training_context['current_epoch'] < self.noise_end_epoch:
                    exchange_real = random_choice(self.img_real).clone()
                    exchange_fake = random_choice(self.img_fake).clone()
                    self.img_real[random.choice(range(self.img_real.size(0)))] = exchange_fake
                    self.img_fake[random.choice(range(self.img_fake.size(0)))] = exchange_real

                if self.noised_real and training_context['current_epoch'] < self.noise_end_epoch and random.randint(0,100) % 10 <training_context['current_epoch']:
                    self.img_real = (training_context['current_input'] + to_tensor( 0.2 * (1 - float(curr_epochs) / self.noise_end_epoch) * np.random.standard_normal( list(self.img_real.size())))).clamp_(-1, 1)

                self.D_real = self.discriminator(self.img_real)
                self.D_fake = self.discriminator(self.img_fake)
        except:
            PrintException()

    def post_loss_calculation(self, training_context):
        is_collect_data = training_context['is_collect_data']

        true_label = to_tensor(np.ones((self.D_real.size()), dtype=np.float32))
        false_label = to_tensor(np.zeros((self.D_real.size()), dtype=np.float32))

        if self.label_smoothing:
            if training_context['current_epoch'] < 20:
                true_label = to_tensor(np.random.randint(80, 100, (self.D_real.size())).astype(np.float32) / 100.0)
            elif training_context['current_epoch'] < 50:
                true_label = to_tensor(np.random.randint(85, 100, (self.D_real.size())).astype(np.float32) / 100.0)
            elif training_context['current_epoch'] < 200:
                true_label = to_tensor(np.random.randint(90, 100, (self.D_real.size())).astype(np.float32) / 100.0)
            else:
                pass
        # true_label.requires_grad=False
        # false_label.requires_grad=False

        if training_context['gan_role'] == 'generator':

            try:
                # self.D_real = self.discriminator(self.img_real)
                # self.generator.eval()
                # self.img_fake = to_tensor(to_numpy(self.generator(self.z_noise)))
                # self.generator.train()
                # self.D_fake = self.discriminator(self.img_fake)
                this_loss = 0

                if self.gan_type == 'gan':
                    adversarial_loss = torch.nn.BCELoss()
                    this_loss = adversarial_loss(self.D_fake, true_label)
                elif self.gan_type == 'dcgan':
                    adversarial_loss = torch.nn.BCELoss()
                    this_loss = adversarial_loss(self.D_fake, true_label)
                elif self.gan_type == 'wgan':
                    this_loss = -self.D_fake.mean()

                elif self.gan_type == 'wgan-gp':
                    this_loss = -self.D_fake.mean()

                elif self.gan_type == 'lsgan':  # least squared
                    this_loss = torch.mean((self.D_fake - 1) ** 2)
                elif self.gan_type == 'lsgan1':  # loss sensitive
                    this_loss = torch.mean((self.D_fake - 1) ** 2)
                elif self.gan_type == 'rasgan':
                    D_fake_logit = torch.sigmoid(self.D_fake - self.D_real.mean())
                    this_loss = binary_crossentropy(D_fake_logit, false_label + 1).mean()
                    self.G_metric = D_fake_logit
                    if 'D_fake_logit' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_fake_logit'] = []
                        training_context['metrics']['D_fake_logit'] = []
                    training_context['tmp_metrics']['D_fake_logit'].append(to_numpy(D_fake_logit).mean())  # adversarial_loss = torch.nn.BCEWithLogitsLoss()  # this_loss = adversarial_loss(self.D_fake - self.D_real.mean(0, keepdim=True),false_label+1)
                elif self.gan_type == 'ebgan':
                    pass

                training_context['current_loss'] = training_context['current_loss'] + this_loss
                if not self.gan_type == 'rasgan':
                    self.G_metric = self.D_fake
                    if 'D_fake' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_fake'] = []
                        training_context['metrics']['D_fake'] = []
                    training_context['tmp_metrics']['D_fake'].append(to_numpy(self.D_fake).mean())

                if is_collect_data:
                    if 'gan_g_loss' not in training_context['losses']:
                        training_context['losses']['gan_g_loss'] = []
                    training_context['losses']['gan_g_loss'].append(float(to_numpy(this_loss)))
            except:
                PrintException()



        elif training_context['gan_role'] == 'discriminator':
            try:
                if self.generator_first == False:
                    training_context['retain_graph'] = True

                if self.use_total_variation:
                    self.D_real = self.D_real.clamp(min=-1,max=1)
                    self.D_fake = self.D_fake.clamp(min=-1,max=1)
                this_loss = 0
                if self.gan_type == 'gan':
                    adversarial_loss = torch.nn.BCELoss()
                    real_loss = adversarial_loss(self.D_real, true_label)
                    fake_loss = adversarial_loss(self.D_fake, false_label)
                    this_loss = (real_loss + fake_loss).mean() / 2
                elif self.gan_type == 'dcgan':
                    adversarial_loss = torch.nn.BCELoss()
                    real_loss = adversarial_loss(self.D_real, true_label)
                    fake_loss = adversarial_loss(self.D_fake, false_label)
                    this_loss = (real_loss + fake_loss).mean() / 2
                elif self.gan_type == 'wgan':
                    this_loss = (-self.D_real.mean() + self.D_fake.mean()) / 2
                elif self.gan_type == 'wgan-gp':
                    def compute_gradient_penalty():
                        """Calculates the gradient penalty loss for WGAN GP"""
                        # Random weight term for interpolation between real and fake samples
                        alpha = to_tensor(np.random.random((self.img_real.size(0), 1, 1, 1)))
                        # Get random interpolation between real and fake samples
                        interpolates = (alpha * self.img_real + ((1 - alpha) * self.img_fake)).requires_grad_(True)
                        out = self.discriminator(interpolates)
                        fake = to_tensor(np.ones(out.size()))
                        # Get gradient w.r.t. interpolates
                        gradients = \
                        torch.autograd.grad(outputs=out, inputs=interpolates, grad_outputs=fake, create_graph=True,
                                            retain_graph=True, only_inputs=True, )[0]
                        gradients = gradients.view(gradients.size(0), -1)
                        gradient_penalty = ((gradients.norm(2, dim=1) - 1) ** 2).mean()
                        return gradient_penalty

                    gp = 10 * compute_gradient_penalty()
                    if is_collect_data:
                        if 'gradient_penalty' not in training_context['losses']:
                            training_context['losses']['gradient_penalty'] = []
                        training_context['losses']['gradient_penalty'].append(float(to_numpy(gp)))

                    this_loss = gp + (-self.D_real.mean() + self.D_fake.mean())

                elif self.gan_type == 'lsgan':
                    this_loss = 0.5 * (torch.mean((self.D_real - true_label) ** 2) + torch.mean(self.D_fake ** 2))
                elif self.gan_type == 'rasgan':
                    D_real_logit = torch.sigmoid(self.D_real - self.D_fake.mean())
                    D_fake_logit = torch.sigmoid(self.D_fake - self.D_real.mean())
                    this_loss = (binary_crossentropy(D_real_logit, true_label).mean() + binary_crossentropy( D_fake_logit, false_label).mean()) / 2
                    self.D_metric = D_real_logit
                    if 'D_real_logit' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_real_logit'] = []
                        training_context['metrics']['D_real_logit'] = []
                    training_context['tmp_metrics']['D_real_logit'].append(to_numpy(
                        D_real_logit).mean())  # adversarial_loss = torch.nn.BCEWithLogitsLoss()  # this_loss =(adversarial_loss(self.D_real - self.D_fake.mean(0, keepdim=True),true_label)+ adversarial_loss(self.D_fake - self.D_real.mean(0, keepdim=True),false_label))/2.0

                training_context['current_loss'] = training_context['current_loss'] + this_loss
                if not self.gan_type == 'rasgan':
                    self.D_metric = self.D_real
                    if 'D_real' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_real'] = []
                        training_context['metrics']['D_real'] = []
                    training_context['tmp_metrics']['D_real'].append(to_numpy(self.D_real).mean())

                if is_collect_data:
                    if 'gan_d_loss' not in training_context['losses']:
                        training_context['losses']['gan_d_loss'] = []
                    training_context['losses']['gan_d_loss'].append(float(to_numpy(this_loss)))
            except:
                PrintException()

    def on_optimization_step_end(self, training_context):
        model = training_context['current_model']
        is_collect_data = training_context['is_collect_data']

        if training_context['gan_role'] == 'generator':
            self.img_fake = to_tensor(to_numpy(self.img_fake))


        elif training_context['gan_role'] == 'discriminator':
            self.D_real= to_tensor(to_numpy(self.discriminator( training_context['current_input'])))
            if self.gan_type == 'wgan' or self.weight_clipping:
                for p in training_context['current_model'].parameters():
                    p.data.clamp_(-0.01, 0.01)

            # self.D_real = self.discriminator(self.img_real)  # self.D_fake = self.discriminator(self.img_fake)  # training_context['D_real'] = self.D_real  # training_context['D_fake'] = self.D_fake  # training_context['discriminator'] = model

    def on_batch_end(self, training_context):
        if training_context['gan_role'] == 'generator':
            if training_context['stop_update'] == 0 and self.g_train_frequency - 1 > 0 and training_context[
                'current_batch'] > 20:
                training_context['stop_update'] = self.g_train_frequency - 1
            elif 0 < self.g_train_frequency < 1 and training_context['stop_update'] != self.g_train_frequency:
                training_context['stop_update'] = self.g_train_frequency

            if (training_context['current_epoch'] * training_context['total_batch'] + training_context[
                'current_batch'] + 1) % self.tile_image_frequency == 0:
                for i in range(3):
                    train_data = self.data_provider.next()
                    input = None
                    target = None
                    if 'data_feed' in training_context and len(training_context['data_feed']) > 0:
                        data_feed = training_context['data_feed']
                        input = to_tensor(train_data[data_feed.get('input')]) if data_feed.get('input') >= 0 else None
                        # target = to_tensor(train_data[data_feed.get('target')]) if data_feed.get('target') >= 0
                        # else None
                        imgs = to_numpy(self.generator(input)).transpose([0, 2, 3, 1]) * 127.5 + 127.5
                        self.tile_images.append(imgs)

                # if self.tile_image_include_mask:
                #     tile_images_list.append(input*127.5+127.5)
                tile_rgb_images(*self.tile_images, save_path=os.path.join('Results', 'tile_image_{0}.png'), imshow=True)
                self.tile_images = []

        elif training_context['gan_role'] == 'discriminator':
            pass

    def on_epoch_end(self, training_context):
        pass
        # try:
        #     if training_context['current_epoch'] > 0:
        #         if (self.generator_first and training_context['gan_role'] == 'discriminator') or (
        #                 not self.generator_first and training_context['gan_role'] == 'generator'):
        #             role1 = self.training_items.value_list[0].training_context['gan_role']
        #             role2 = self.training_items.value_list[1].training_context['gan_role']
        #             grad1 = np.abs(np.array(
        #                 self.training_items.value_list[0].training_context['grads_state']['last_layer'][-3:])).mean()
        #             grad2 = np.abs(np.array(
        #                 self.training_items.value_list[1].training_context['grads_state']['last_layer'][-3:])).mean()
        #             metric1 = self.training_items.value_list[0].epoch_metric_history.value_list[0][-1]
        #             metric2 = self.training_items.value_list[1].epoch_metric_history.value_list[0][-1]
        #
        #             if training_context['current_epoch'] == 0:
        #                 if role1 == 'generator':
        #                     self.generator_worse_metric = np.array(
        #                         self.training_items.value_list[0].batch_metric_history.value_list[0][5:]).min(
        #                         initial=0.5)
        #                     self.discriminator_worse_metric = np.array(
        #                         self.training_items.value_list[1].batch_metric_history.value_list[0][5:]).max(
        #                         initial=0.5)
        #                 else:
        #                     self.discriminator_worse_metric = np.array(
        #                         self.training_items.value_list[0].batch_metric_history.value_list[0][5:]).max(
        #                         initial=0.5)
        #                     self.generator_worse_metric = np.array(
        #                         self.training_items.value_list[1].batch_metric_history.value_list[0][5:]).min(
        #                         initial=0.5)
        #                 self.generator_best_metric = self.generator_worse_metric
        #                 self.discriminator_best_metric = self.discriminator_worse_metric
        #
        #             else:
        #                 if role1 == 'generator':
        #                     if metric1 > self.generator_best_metric:
        #                         self.generator_best_metric = metric1
        #                         self.generator_best_epoch = training_context['current_epoch']
        #                     if metric2 < self.discriminator_best_metric:
        #                         self.discriminator_best_metric = metric2
        #                         self.discriminator_best_epoch = training_context['current_epoch']
        #                 else:
        #                     if metric2 > self.generator_best_metric:
        #                         self.generator_best_metric = metric2
        #                         self.generator_best_epoch = training_context['current_epoch']
        #                     if metric1 < self.discriminator_best_metric:
        #                         self.discriminator_best_metric = metric1
        #                         self.discriminator_best_epoch = training_context['current_epoch']
        #
        #             if grad1 < 5e-5 and grad2 < 5e-5 and self.discriminator_best_epoch < training_context[
        #                 'current_epoch'] - 3 and self.generator_best_epoch < training_context['current_epoch'] - 3:
        #                 generator_metric = metric1 if role1 == 'generator' else metric2
        #                 discriminator_metric = metric1 if role1 == 'discriminator' else metric2
        #                 if abs(self.generator_best_metric - generator_metric) > 0.2 and abs(
        #                         self.discriminator_best_metric - discriminator_metric) > 0.2:
        #                     self.training_items.value_list[0].optimizer.adjust_learning_rate(
        #                         self.training_items.value_list[0].optimizer.lr / 2, True)
        #                     self.training_items.value_list[1].optimizer.adjust_learning_rate(
        #                         self.training_items.value_list[1].optimizer.lr / 2, True)
        #                     self.noise_end_epoch = training_context['current_epoch'] + 10
        #                     self.experience_replay = False
        #                     self.noisy_labels = True
        #
        #             print(role1, grad1, metric1, role2, grad2, metric2)
        # except:
        #     PrintException()

            #     if training_context['optimizer'].lr>1e-6:  #         training_context['optimizer'].adjust_learning_rate(training_context['optimizer'].lr*0.5,True)  # elif training_context['current_epoch']>=1 and float(self.D_real.mean()) > 0.8 and float(self.D_fake.mean()) < 0.1 :  #     if self.discriminator is not None and model.name == self.discriminator.name:  #         training_context['optimizer'].adjust_learning_rate(training_context['optimizer'].lr / 2.0)


class CycleGanCallback(GanCallbacksBase):
    # Generators: G_A: A -> B; G_B: B -> A.
    # Discriminators: D_A: G_B(B) vs. A   ; D_B: G_A(A) vs. B
    def __init__(self, generatorA=None, generatorB=None, discriminatorA=None, discriminatorB=None, gan_type='cyclegan',
                 label_smoothing=False, noised_real=True, noise_intensity=0.05, weight_clipping=False,
                 tile_image_frequency=100, experience_replay=False, g_train_frequency=1, d_train_frequency=1, **kwargs):
        super(CycleGanCallback, self).__init__()
        if isinstance(generatorA, ImageGenerationModel):
            self.generatorA = generatorA.model
        if isinstance(generatorA, ImageGenerationModel):
            self.generatorB = generatorB.model
        if isinstance(discriminatorA, ImageClassificationModel):
            self.discriminatorA = discriminatorA.model
        if isinstance(discriminatorB, ImageClassificationModel):
            self.discriminatorB = discriminatorB.model
        self.data_provider = None
        self.z_noise = None
        self.D_realA = None
        self.D_fakeA = None
        self.D_realB = None
        self.D_fakeB = None
        self.D_metric = None
        self.G_metric = None
        self.realA = None
        self.realB = None
        self.fakeA = None  # B->A
        self.fakeB = None  # A->B
        self.fakeA_buffer = ReplayBuffer(1000)
        self.fakeB_buffer = ReplayBuffer(1000)
        self.gan_type = gan_type
        self.label_smoothing = label_smoothing
        self.noised_real = noised_real
        self.noise_intensity = noise_intensity
        self.tile_image_frequency = tile_image_frequency
        self.weight_clipping = weight_clipping
        self.experience_replay = experience_replay
        self.g_train_frequency = g_train_frequency
        self.d_train_frequency = d_train_frequency
        if self.experience_replay == True:
            make_dir_if_need('Replay')
        self.tile_images = []
        self.generator_first = None
        self.cooldown_counter = 0
        self.beginning_repository = []
        self.latter_repository = []

    def on_training_start(self, training_context):
        training_items = training_context['training_items']
        self.data_provider = training_context['_dataloaders'].value_list[0]

        conterparty = OrderedDict()
        conterparty['generatorA'] = None
        conterparty['generatorB'] = None
        conterparty['discriminatorA'] = None
        conterparty['discriminatorB'] = None

        for training_item in training_items:
            if isinstance(training_item, ImageGenerationModel):
                if self.generatorA.name == training_item.model.name:
                    conterparty['generatorA'] = training_item.model
                    training_context['gan_role'] = 'generatorA'
                elif self.generatorB.name == training_item.model.name:
                    conterparty['generatorB'] = training_item.model
                    training_context['gan_role'] = 'generatorB'
                elif self.generatorA is None and self.generatorB is None:
                    self.generatorA = training_item.model
                    conterparty['generatorA'] = training_item.model
                    training_context['gan_role'] = 'generatorA'
                elif self.generatorA is not None and self.generatorB is None:
                    self.generatorB = training_item.model
                    conterparty['generatorB'] = training_item.model
                    training_context['gan_role'] = 'generatorB'

            elif isinstance(training_item, ImageClassificationModel):
                if self.discriminatorA.name == training_item.model.name:
                    conterparty['discriminatorA'] = training_item.model
                    training_context['gan_role'] = 'discriminatorA'
                elif self.discriminatorB.name == training_item.model.name:
                    conterparty['discriminatorB'] = training_item.model
                    training_context['gan_role'] = 'discriminatorB'
                elif self.discriminatorA is None and self.discriminatorB is None:
                    self.discriminatorA = training_item.model
                    conterparty['discriminatorA'] = training_item.model
                    training_context['gan_role'] = 'discriminatorA'
                elif self.discriminatorA is not None and self.discriminatorB is None:
                    conterparty['discriminatorB'] = training_item.model
                    self.discriminatorB = training_item.model
                    training_context['gan_role'] = 'discriminatorB'

        if self.generatorA is not None and self.generatorB is None:
            self.generatorB = self.generatorA.copy()
            self.generatorB.training_context['gan_role'] = 'generatorB'
            conterparty['generatorB'] = self.generatorB
        if self.discriminatorA is not None and self.discriminatorB is None:
            self.discriminatorB = self.discriminatorA.copy()
            self.discriminatorB.training_context['gan_role'] = 'discriminatorB'
            conterparty['discriminatorB'] = self.discriminatorB

        training_context['training_items'] = conterparty
        self.generator_first = True

    def on_data_received(self, training_context):
        try:
            if training_context['gan_role'] == 'generatorA':
                self.realA = training_context['current_input']
                self.realB = training_context['current_target']

                if self.fakeA is None:
                    self.fakeA = to_tensor(to_numpy(self.generatorB(self.realB)))
                if self.fakeB is None:
                    self.fakeB = to_tensor(to_numpy(self.generatorA(self.realA)))
                self.D_realA = self.discriminatorA(self.realA)
                self.D_fakeA = self.discriminatorA(self.fakeA)
                self.D_realB = self.discriminatorB(self.realB)
                self.D_fakeB = self.discriminatorB(self.fakeB)

            elif training_context['gan_role'] == 'discriminatorA':
                self.D_realA = self.discriminatorA(self.realA)
                self.D_fakeA = self.discriminatorA(self.fakeA)
                self.D_realB = self.discriminatorB(self.realB)
                self.D_fakeB = self.discriminatorB(self.fakeB)

        except:
            PrintException()

    def post_loss_calculation(self, training_context):
        model = training_context['current_model']
        current_mode = None
        is_collect_data = training_context['is_collect_data']

        true_label = to_tensor(np.ones((self.D_real.size()), dtype=np.float32))
        false_label = to_tensor(np.zeros((self.D_real.size()), dtype=np.float32))

        if self.label_smoothing:
            if training_context['current_epoch'] < 20:
                true_label = to_tensor(np.random.randint(80, 100, (self.D_real.size())).astype(np.float32) / 100.0)
            elif training_context['current_epoch'] < 50:
                true_label = to_tensor(np.random.randint(85, 100, (self.D_real.size())).astype(np.float32) / 100.0)
            elif training_context['current_epoch'] < 200:
                true_label = to_tensor(np.random.randint(90, 100, (self.D_real.size())).astype(np.float32) / 100.0)
            else:
                pass
        # true_label.requires_grad=False
        # false_label.requires_grad=False

        if training_context['gan_role'] == 'generatorA' or training_context['gan_role'] == 'generatorB':
            try:

                this_loss = 0

                if self.gan_type == 'gan':
                    adversarial_loss = torch.nn.BCELoss()
                    this_loss = adversarial_loss(self.D_fake, true_label).mean()
                elif self.gan_type == 'dcgan':
                    adversarial_loss = torch.nn.BCELoss()
                    this_loss = adversarial_loss(self.D_fake, true_label).mean()
                elif self.gan_type == 'wgan':
                    this_loss = -self.D_fake.mean()

                elif self.gan_type == 'wgan-gp':
                    this_loss = -self.D_fake.mean()

                elif self.gan_type == 'lsgan':
                    this_loss = torch.mean((self.D_fake - 1) ** 2)
                elif self.gan_type == 'rasgan':
                    D_fake_logit = torch.sigmoid(self.D_fake - self.D_real.mean())
                    this_loss = binary_crossentropy(D_fake_logit, false_label + 1).mean()
                    self.G_metric = D_fake_logit
                    if 'D_fake_logit' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_fake_logit'] = []
                        training_context['metrics']['D_fake_logit'] = []
                    training_context['tmp_metrics']['D_fake_logit'].append(to_numpy(
                        D_fake_logit).mean())  # adversarial_loss = torch.nn.BCEWithLogitsLoss()  # this_loss = adversarial_loss(self.D_fake - self.D_real.mean(0, keepdim=True),false_label+1)
                elif self.gan_type == 'ebgan':
                    pass

                training_context['current_loss'] = training_context['current_loss'] + this_loss
                if not self.gan_type == 'rasgan':
                    self.G_metric = self.D_fake
                    if 'D_fake' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_fake'] = []
                        training_context['metrics']['D_fake'] = []
                    training_context['tmp_metrics']['D_fake'].append(to_numpy(self.D_fake).mean())

                if is_collect_data:
                    if 'gan_g_loss' not in training_context['losses']:
                        training_context['losses']['gan_g_loss'] = []
                    training_context['losses']['gan_g_loss'].append(float(to_numpy(this_loss)))
            except:
                PrintException()



        elif self.discriminator is not None and model.name == self.discriminator.name:
            try:
                self.discriminator = model
                if self.generator_first == False:
                    training_context['retain_graph'] = True

                self.D_real = self.discriminator(self.img_real)
                self.img_fake = to_tensor(to_numpy(self.generator(self.z_noise)))

                if self.experience_replay and training_context['current_epoch'] >= 2:
                    for i in range(2):
                        self.img_fake[random.choice(range(self.img_fake.size(0)))] = to_tensor(
                            random.choice(self.beginning_repository).copy())
                    for i in range(2):
                        self.img_fake[random.choice(range(self.img_fake.size(0)))] = to_tensor(
                            random.choice(self.latter_repository).copy())
                self.D_fake = self.discriminator(self.img_fake)
                this_loss = 0
                if self.gan_type == 'gan':
                    adversarial_loss = torch.nn.BCELoss()
                    real_loss = adversarial_loss(self.D_real, true_label)
                    fake_loss = adversarial_loss(self.D_fake, false_label)
                    this_loss = (real_loss + fake_loss).mean() / 2
                elif self.gan_type == 'dcgan':
                    adversarial_loss = torch.nn.BCELoss()
                    real_loss = adversarial_loss(self.D_real, true_label)
                    fake_loss = adversarial_loss(self.D_fake, false_label)
                    this_loss = (real_loss + fake_loss).mean() / 2
                elif self.gan_type == 'wgan':
                    this_loss = -self.D_real.mean() + self.D_fake.mean()
                elif self.gan_type == 'wgan-gp':
                    def compute_gradient_penalty():
                        """Calculates the gradient penalty loss for WGAN GP"""
                        # Random weight term for interpolation between real and fake samples
                        alpha = to_tensor(np.random.random((self.img_real.size(0), 1, 1, 1)))
                        # Get random interpolation between real and fake samples
                        interpolates = (alpha * self.img_real + ((1 - alpha) * self.img_fake)).requires_grad_(True)
                        out = self.discriminator(interpolates)
                        fake = to_tensor(np.ones(out.size()))
                        # Get gradient w.r.t. interpolates
                        gradients = \
                        torch.autograd.grad(outputs=out, inputs=interpolates, grad_outputs=fake, create_graph=True,
                                            retain_graph=True, only_inputs=True, )[0]
                        gradients = gradients.view(gradients.size(0), -1)
                        gradient_penalty = ((gradients.norm(2, dim=1) - 1) ** 2).mean()
                        return gradient_penalty

                    this_loss = 10 * compute_gradient_penalty() - self.D_real.mean() + self.D_fake.mean()

                elif self.gan_type == 'lsgan':
                    this_loss = 0.5 * (torch.mean((self.D_real - true_label) ** 2) + torch.mean(self.D_fake ** 2))
                elif self.gan_type == 'rasgan':
                    D_real_logit = torch.sigmoid(self.D_real - self.D_fake.mean())
                    D_fake_logit = torch.sigmoid(self.D_fake - self.D_real.mean())
                    this_loss = (binary_crossentropy(D_real_logit, true_label).mean() + binary_crossentropy(
                        D_fake_logit, false_label).mean()) / 2
                    self.D_metric = D_real_logit
                    if 'D_real_logit' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_real_logit'] = []
                        training_context['metrics']['D_real_logit'] = []
                    training_context['tmp_metrics']['D_real_logit'].append(to_numpy(
                        D_real_logit).mean())  # adversarial_loss = torch.nn.BCEWithLogitsLoss()  # this_loss =(adversarial_loss(self.D_real - self.D_fake.mean(0, keepdim=True),true_label)+ adversarial_loss(self.D_fake - self.D_real.mean(0, keepdim=True),false_label))/2.0

                training_context['current_loss'] = training_context['current_loss'] + this_loss
                if not self.gan_type == 'rasgan':
                    self.D_metric = self.D_real
                    if 'D_real' not in training_context['tmp_metrics']:
                        training_context['tmp_metrics']['D_real'] = []
                        training_context['metrics']['D_real'] = []
                    training_context['tmp_metrics']['D_real'].append(to_numpy(self.D_real).mean())

                if is_collect_data:
                    if 'gan_d_loss' not in training_context['losses']:
                        training_context['losses']['gan_d_loss'] = []
                    training_context['losses']['gan_d_loss'].append(float(to_numpy(this_loss)))
            except:
                PrintException()

    def on_optimization_step_end(self, training_context):
        model = training_context['current_model']
        is_collect_data = training_context['is_collect_data']

        if self.generator is not None and model.name == self.generator.name:
            self.generator = training_context['current_model']
            img_fake = to_numpy(self.img_fake)

            # replay
            if self.experience_replay and training_context['current_epoch'] == 0:
                self.beginning_repository.append(img_fake[random.choice(range(img_fake.shape[0]))])
                if (training_context['current_batch'] + 1) % 100 == 0:
                    np.save('Replay/beginning_repository.npy', self.beginning_repository)
            elif self.experience_replay and training_context['current_epoch'] > 0:
                self.latter_repository.append(img_fake[random.choice(range(img_fake.shape[0]))])
                if len(self.latter_repository) > 500:
                    self.latter_repository.pop(random.choice(range(len(self.latter_repository))))
                if (training_context['current_batch'] + 1) % 100 == 0:
                    np.save('Replay/latter_repository.npy', self.latter_repository)

            # training_context['img_fake'] = self.img_fake  # self.D_fake = self.discriminator(self.img_fake)  # training_context['D_fake'] = self.D_fake  #  # if self.gan_type == 'gan':  #     adversarial_loss = torch.nn.BCELoss()  #     this_loss = adversarial_loss(self.D_fake, true_label)  # elif self.gan_type == 'wgan':  #     this_loss = -self.D_fake.mean()


        elif self.discriminator is not None and model.name == self.discriminator.name:
            self.discriminator = training_context['current_model']

            if self.gan_type == 'wgan' or self.weight_clipping:
                for p in training_context['current_model'].parameters():
                    p.data.clamp_(-0.01, 0.01)

            # self.D_real = self.discriminator(self.img_real)  # self.D_fake = self.discriminator(self.img_fake)  # training_context['D_real'] = self.D_real  # training_context['D_fake'] = self.D_fake  # training_context['discriminator'] = model

    def on_batch_end(self, training_context):
        model = training_context['current_model']
        if self.generator is not None and model.name == self.generator.name:
            if training_context['stop_update'] == 0 and self.g_train_frequency - 1 > 0 and training_context[
                'current_batch'] > 20:
                training_context['stop_update'] = self.g_train_frequency - 1
            elif 0 < self.g_train_frequency < 1 and training_context['stop_update'] != self.g_train_frequency:
                training_context['stop_update'] = self.g_train_frequency
            # if training_context['current_epoch'] <10 and (training_context['current_epoch'] * training_context['total_batch'] + training_context[ 'current_batch'] + 1)%300==0:
            #         i = 0
            #         for name, param in self.generator.named_parameters():
            #             if 'bias' not in name:
            #                 param = param * to_tensor( np.greater(np.random.uniform(0, 1, list(param.size())), min(0.1 + 0.05 * i, 0.5)).astype( np.float32))
            #             i += 1
            #         print('generator random pruning')

            # if training_context['current_epoch']>=3  and self.temp_weight_constraint==True and self.cooldown_counter==0:
            #     if float(self.D_real.mean()) > 0.9 and float(self.D_fake.mean()) < 0.1:
            #         min_max_norm(self.generator,0,1,3)
            #         print('execute temp min_max_norm constraint to generator')

            if (training_context['current_epoch'] * training_context['total_batch'] + training_context[
                'current_batch'] + 1) % self.tile_image_frequency == 0:
                for i in range(3):
                    train_data = self.data_provider.next()
                    input = None
                    target = None
                    if 'data_feed' in training_context and len(training_context['data_feed']) > 0:
                        data_feed = training_context['data_feed']
                        input = to_tensor(train_data[data_feed.get('input')]) if data_feed.get('input') >= 0 else None
                        # target = to_tensor(train_data[data_feed.get('target')]) if data_feed.get('target') >= 0 else None
                        imgs = to_numpy(self.generator(input)).transpose([0, 2, 3, 1]) * 127.5 + 127.5
                        self.tile_images.append(imgs)

                # if self.tile_image_include_mask:
                #     tile_images_list.append(input*127.5+127.5)
                tile_rgb_images(*self.tile_images, save_path=os.path.join('Results', 'tile_image_{0}.png'), imshow=True)
                self.tile_images = []

        elif self.discriminator is not None and model.name == self.discriminator.name:
            # if training_context['current_epoch']>=1  and self.gan_type not in ('wgan','wgan-gp'):
            #     if float(self.D_real.mean())>0.8 and float(self.D_fake.mean())<0.2:
            #         self.noise_intensity = 0.5
            #         self.cooldown_counter = 100
            if training_context['stop_update'] == 0 and self.d_train_frequency - 1 > 0 and training_context[
                'current_batch'] > 20:
                training_context['stop_update'] = self.d_train_frequency - 1
            elif 0 < self.d_train_frequency < 1 and training_context['stop_update'] != self.d_train_frequency:
                training_context['stop_update'] = self.d_train_frequency

            if self.cooldown_counter > 0:  #
                self.cooldown_counter = self.cooldown_counter - 1
                if self.cooldown_counter == 0:
                    self.noise_intensity = 0.1

    def on_epoch_end(self, training_context):
        model = training_context['current_model']
        if self.discriminator is not None and model.name == self.discriminator.name:
            # if float(self.D_metric.mean()) > 0.8 and float(self.G_metric.mean()) < 0.2 and self.gan_type=='rasgan':
            #    i=0
            #    for name, param in model.named_parameters():
            #        if 'bias' not in name:
            #            param = param  *to_tensor(np.greater(np.random.uniform(0,1,list(param.size())),min(0.1+0.05*i,0.5)).astype(np.float32))
            #        i+=1
            #    print('discriminator random pruning')
            pass

        if (training_context['current_epoch'] + 1) % 20 == 0:
            if training_context['optimizer'].lr > 1e-6:
                training_context['optimizer'].adjust_learning_rate(training_context['optimizer'].lr * 0.5,
                                                                   True)  # elif training_context['current_epoch']>=1 and float(self.D_real.mean()) > 0.8 and float(self.D_fake.mean()) < 0.1 :  #     if self.discriminator is not None and model.name == self.discriminator.name:  #         training_context['optimizer'].adjust_learning_rate(training_context['optimizer'].lr / 2.0)








