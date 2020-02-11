#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import cv2
from matplotlib import pyplot
import numpy
import torch
import torchvision.transforms as T
from PIL import Image

# cv2.setNumThreads(0)

__author__ = 'Christian Heider Nielsen'

resize = T.Compose([T.ToPILImage(), T.Resize(40, interpolation=Image.CUBIC), T.ToTensor()])

# This is based on the code from gym.
screen_width = 600


def get_cart_location(env):
  world_width = env.x_threshold * 2
  scale = screen_width / world_width
  return int(env.state[0] * scale + screen_width / 2.0)  # MIDDLE OF CART


def get_screen(env, view_width=320):
  tp = (2, 0, 1)
  center = view_width // 2
  screen = env.render().transpose(tp)  # transpose into torch order (CHW)
  # Strip off the top and bottom of the screen
  screen = screen[:, center:view_width]  # center slice
  cart_location = get_cart_location(env)
  if cart_location < view_width // 2:
    slice_range = slice(view_width)
  elif cart_location > (screen_width - view_width // 2):
    slice_range = slice(-view_width, None)
  else:
    slice_range = slice(cart_location - view_width // 2, cart_location + view_width // 2)
  # Strip off the edges, so that we have a square image centered on a cart
  screen = screen[:, :, slice_range]
  # Convert to float, rescale, convert to torch tensor
  # (this doesn't require a copy)
  screen = numpy.ascontiguousarray(screen, dtype=numpy.float32) / 255  # RGB normalise
  return screen


def transform_screen(screen, device):
  screen = torch.from_numpy(screen)
  # Resize, and add a batch dimension (BCHW)
  return resize(screen).unsqueeze(0).to(get_torch_device())


def test_cnn_dqn_agent(config):
  import gym

  env = gym.make(config.ENVIRONMENT_NAME).unwrapped
  env.seed(config.SEED)

  is_ipython = 'inline' in matplotlib.get_backend()
  if is_ipython:
    pass

  pyplot.ion()

  episode_durations = []

  agent = DQNAgent(config)
  agent.build(env)

  episodes = tqdm(range(config.ROLLOUTS), leave=False, disable=False)
  for episode_i in episodes:
    episodes.set_description(f'Episode:{episode_i}')
    env.reset()
    last_screen = U.transform_screen(get_screen(env), agent.device)
    current_screen = U.transform_screen(get_screen(env), agent.device)
    state = current_screen - last_screen

    rollout = tqdm(count(), leave=False)
    for t in rollout:

      action, (_, signal, terminated, *_) = agent.step(state, env)

      last_screen = current_screen
      current_screen = U.transform_screen(get_screen(env), agent.device)

      successor_state = None
      if not terminated:
        successor_state = current_screen - last_screen

      if agent._signal_clipping:
        signal = numpy.clip(signal, -1.0, 1.0)

      agent._memory_buffer.add_transition(state, action, signal, successor_state, not terminated)

      agent.update()
      if terminated:
        episode_durations.append(t + 1)
        plot_durations(episode_durations=episode_durations)
        break

      state = successor_state

  env.render()
  env.close()
  pyplot.ioff()
  pyplot.show()


if __name__ == '__main__':
  import gym

  env = gym.make('CartPole-v0').unwrapped

  env.reset()
  pyplot.figure()
  pyplot.imshow(get_screen(env), interpolation='none')
  pyplot.title('Example extracted screen')
  pyplot.show()
  env.close()
