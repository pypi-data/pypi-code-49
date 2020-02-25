from tensorboard.backend.event_processing import event_accumulator
from guang.Utils.plotly import Multiplots, Subplots
import numpy as np
from glob import glob


event_list = glob('./exp/train_nodev_csmsc_parallel_wavegan.v1/events.out.tfevents.*')

def show(event_list):
    ea=event_accumulator.EventAccumulator(event_list[0]) 
    ea.Reload()

    # for idx, i in enumerate(ea.scalars.Keys()):
    #     print(idx, i)

    val=ea.scalars.Items(ea.scalars.Keys()[11])

    print(len(val))
    steps, loss = {}, {}
    for idx, i in enumerate(ea.scalars.Keys()):
        items = ea.scalars.Items(i)
        steps.setdefault(i, [j.step for j in items])
        loss.setdefault(i, [j.value for j in items])

    # The following works only in jupyterlab
    fig = Multiplots()
    for i in ea.scalars.Keys():
        fig.plot(steps[i], (loss[i]), label=i)

    fig.x_label = 'steps'
    fig.y_label = 'loss'

    fig.show()

