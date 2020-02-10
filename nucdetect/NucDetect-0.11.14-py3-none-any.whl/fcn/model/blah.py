from tensorflow.keras import models
import os

from tensorflow.keras.utils import plot_model
LOAD_DIR = r"C:/tf_models"
m = models.load_model(os.path.join(LOAD_DIR, "nucleus_detector_unet_6x6_256x256_final_gpu.h5"))
# compile method actually creates the model in the graph.
m.compile(loss="binary_crossentropy",
          optimizer="Adam",
          metrics=["accuracy"])
plot_model(m, to_file='model_plot.png', show_shapes=True, show_layer_names=False)