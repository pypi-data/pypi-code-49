# Copyright 2020 Lorna Authors. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import collections

# Parameters for the entire model (stem, all blocks, and head)
GlobalParams = collections.namedtuple('GlobalParams', [
  "num_classes", "aux_logits", "transform_input",
  "blocks", "dropout_rate", "image_size"
])

# Change namedtuple defaults
GlobalParams.__new__.__defaults__ = (None,) * len(GlobalParams._fields)


########################################################################
############## HELPERS FUNCTIONS FOR LOADING MODEL PARAMS ##############
########################################################################


def googlenet_params(model_name):
  """ Map VGGNet model name to parameter coefficients. """
  params_dict = {
    # Coefficients: aux_logits, transform_input, blocks, image_size
    "googlenet": (False, True, None, 224),
  }
  return params_dict[model_name]


def googlenet(aux_logits, transform_input, blocks,
              image_size, dropout_rate=0.2, num_classes=1000):
  """ Creates a googlenet_pytorch model. """

  global_params = GlobalParams(
    aux_logits=aux_logits,
    transform_input=transform_input,
    blocks=blocks,
    image_size=image_size,
    dropout_rate=dropout_rate,
    num_classes=num_classes,
  )

  return global_params


def get_model_params(model_name):
  """ Get the block args and global params for a given model """
  if model_name.startswith('googlenet'):
    a, t, b, s = googlenet_params(model_name)
    # note: all models have drop connect rate = 0.2
    global_params = googlenet(aux_logits=a, transform_input=t, blocks=b, image_size=s)
  else:
    raise NotImplementedError(f"model name is not pre-defined: {model_name}.")

  return global_params
