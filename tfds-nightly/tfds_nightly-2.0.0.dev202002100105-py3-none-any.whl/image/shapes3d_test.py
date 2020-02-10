# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Shapes3D dataset test."""
from tensorflow_datasets.image import shapes3d
import tensorflow_datasets.testing as tfds_test


class Shapes3dTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = shapes3d.Shapes3d
  SPLITS = {"train": 5}
  DL_EXTRACT_RESULT = "3dshapes.h5"


class Shapes3dS3Test(Shapes3dTest):
  VERSION = "experimental_latest"


if __name__ == "__main__":
  tfds_test.test_main()
