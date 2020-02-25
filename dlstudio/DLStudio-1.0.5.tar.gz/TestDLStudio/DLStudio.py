# -*- coding: utf-8 -*-

__version__   = '1.0.5'
__author__    = "Avinash Kak (kak@purdue.edu)"
__date__      = '2020-February-24'   
__url__       = 'https://engineering.purdue.edu/kak/distDLS/DLStudio-1.0.5.html'
__copyright__ = "(C) 2020 Avinash Kak. Python Software Foundation."

__doc__ = '''

DLStudio.py

Version: ''' + __version__ + '''
   
Author: Avinash Kak (kak@purdue.edu)

Date: ''' + __date__ + '''


@title
CHANGE LOG:

  Version 1.0.5:

    This version includes an inner class, SkipConnections, for
    experimenting with skip connections to improve the performance of a
    deep network.  The Examples subdirectory of the distribution includes a
    script, playing_with_skip_connections.py, that demonstrates how you can
    experiment with SkipConnections.  The network class used by
    SkipConnections is named BMEnet with an easy-to-use interface for
    experimenting with networks of arbitrary depth.

  Version 1.0.4:

    I have added one more inner class, AutogradCustomization, to the module
    that illustrates how to extend Autograd if you want to endow it with
    additional functionality. And, most importantly, this version fixes an
    important bug that caused wrong information to be written out to the
    disk when you tried to save the learned model at the end of a training
    session. I have also cleaned up the comment blocks in the
    implementation code.

  Version 1.0.3:

    This is the first public release version of this module.

@title
INTRODUCTION:

    Every design activity involves mixing and matching things and doing so
    repeatedly until you have achieved the desired results.  The same thing
    is true of modern deep learning networks.  When you are working with a
    new data domain, it is likely that you would want to experiment with
    different network layouts that you may have dreamed of yourself or that
    you may have seen somewhere in a publication or at some web site.

    The goal of this module is to make it easier to engage in this process.
    The idea is that you would drop in the module a new network and you
    would be able to see right away the results you would get with the new
    network.

    This module also allows you to specify a network with a configuration
    string.  The module parses the string and creates the network.  In
    upcoming revisions of this module, I am planning to add additional
    features to this approach in order to make it more general and more
    useful for production work.

    Starting with Version 1.0.5, you can now experiment with skip
    connections in a CNN to see how a deep network with this feature might
    yield improved classification results.  Deep networks suffer from the
    problem of vanishing gradients that degrades their performance.
    Vanishing gradients means that the gradients of the loss calculated in
    the early layers of a network become increasingly muted as the network
    becomes deeper.  An important mitigation strategy for addressing this
    problem consists of creating a CNN using blocks with skip connections.

    The code for using skip connections is in the inner class SkipConnections
    of the module.  And the network that allows you to construct a CNN with
    skip connections is named BMEnet.  As shown in the script
    playing_with_skip_connections.py in the Examples directory of the
    distribution, you can easily create a CNN with arbitrary depth just by
    using a constructor option "depth" for BMEnet. The basic block of the
    network constructed in this manner is called SkipBlock which, very much
    like the BasicBlock in ResNet-18, has a couple of convolutional layers
    whose output is combined with the input to the block.

    Note that the value given to the the "depth" constructor option for the
    BMEnet class does NOT translate directly into the actual depth of the
    CNN. [Again, see the script playing_with_skip_connections.py in the
    Examples directory for how to use this option.] The value of "depth" is
    translated into how many instances of SkipBlock to use for constructing
    the CNN.


@title
INSTALLATION:

    The DLStudio class was packaged using setuptools.  For
    installation, execute the following command in the source directory
    (this is the directory that contains the setup.py file after you have
    downloaded and uncompressed the package):
 
            sudo python setup.py install

    and/or, for the case of Python3, 

            sudo python3 setup.py install

    On Linux distributions, this will install the module file at a location
    that looks like

             /usr/local/lib/python2.7/dist-packages/

    and, for the case of Python3, at a location that looks like

             /usr/local/lib/python3.6/dist-packages/

    If you do not have root access, you have the option of working directly
    off the directory in which you downloaded the software by simply
    placing the following statements at the top of your scripts that use
    the DLStudio class:

            import sys
            sys.path.append( "pathname_to_DLStudio_directory" )

    To uninstall the module, simply delete the source directory, locate
    where the DLStudio module was installed with "locate
    DLStudio" and delete those files.  As mentioned above,
    the full pathname to the installed version is likely to look like
    /usr/local/lib/python2.7/dist-packages/DLStudio*

    If you want to carry out a non-standard install of the
    DLStudio module, look up the on-line information on
    Disutils by pointing your browser to

              http://docs.python.org/dist/dist.html

@title
USAGE:

    If you want to specify a network with just a configuration string,
    your usage of the module is going to look like:


        from DLStudio import *
        
        convo_layers_config = "1x[128,3,3,1]-MaxPool(2) 1x[16,5,5,1]-MaxPool(2)"
        fc_layers_config = [-1,1024,10]
        
        dls = DLStudio(   dataroot = "/home/kak/ImageDatasets/CIFAR-10/",
                          image_size = [32,32],
                          convo_layers_config = convo_layers_config,
                          fc_layers_config = fc_layers_config,
                          path_saved_model = "./saved_model",
                          momentum = 0.9,
                          learning_rate = 1e-3,
                          epochs = 2,
                          batch_size = 4,
                          classes = ('plane','car','bird','cat','deer',
                                     'dog','frog','horse','ship','truck'),
                          use_gpu = True,
                          debug_train = 0,
                          debug_test = 1,
                      )
        
        configs_for_all_convo_layers = dls.parse_config_string_for_convo_layers()
        convo_layers = dls.build_convo_layers2( configs_for_all_convo_layers )
        fc_layers = dls.build_fc_layers()
        model = dls.Net(convo_layers, fc_layers)
        dls.show_network_summary(model)
        dls.load_cifar_10_dataset()
        dls.run_code_for_training(model)
        dls.run_code_for_testing(model)
                

    or, if you would rather experiment with a drop-in network, your usage
    of the module is going to look something like:


        dls = DLStudio(   dataroot = "/home/kak/ImageDatasets/CIFAR-10/",
                          image_size = [32,32],
                          path_saved_model = "./saved_model",
                          momentum = 0.9,
                          learning_rate = 1e-3,
                          epochs = 2,
                          batch_size = 4,
                          classes = ('plane','car','bird','cat','deer',
                                     'dog','frog','horse','ship','truck'),
                          use_gpu = True,
                          debug_train = 0,
                          debug_test = 1,
                      )
        
        exp_seq = DLStudio.ExperimentsWithSequential( dl_studio = dls )   ## for your drop-in network
        exp_seq.load_cifar_10_dataset_with_augmentation()
        model = exp_seq.Net()
        dls.show_network_summary(model)
        exp_seq.run_code_for_training(model)
        exp_seq.run_code_for_testing(model)

        
    This assumes that you copy-and-pasted the network you want to
    experiment with in a class like ExperimentsWithSequential that is
    included in the module.


@title
CONSTRUCTOR PARAMETERS: 

    batch_size:  Carries the usual meaning in the neural network context.

    classes:  A list of the symbolic names for the classes.

    convo_layers_config: This parameter allows you to specify a convolutional network
                  with a configuration string.  Must be formatted as explained in the
                  comment block associated with the method
                  "parse_config_string_for_convo_layers()"

    dataroot: This points to where your dataset is located.

    debug_test: Setting it allow you to see images being used and their predicted
                 class labels every 2000 batch-based iterations of testing.

    debug_train: Does the same thing during training that debug_test does during
                 testing.

    epochs: Specifies the number of epochs to be used for training the network.

    fc_layers_config: This parameter allows you to specify the final
                 fully-connected portion of the network with just a list of
                 the number of nodes in each layer of this portion.  The
                 first entry in this list must be the number '-1', which
                 stands for the fact that the number of nodes in the first
                 layer will be determined by the final activation volume of
                 the convolutional portion of the network.

    image_size:  The heightxwidth size of the images in your dataset.

    learning_rate:  Again carries the usual meaning.

    momentum:  Carries the usual meaning and needed by the optimizer.

    path_saved_model: The path to where you want the trained model to be
                  saved in your disk so that it can be retrieved later
                  for inference.

    use_gpu: You must set it to True if you want the GPU to be used for training.


@title
PUBLIC METHODS:

    (1)  build_convo_layers()

         This method creates the convolutional layers from the parameters
         in the configuration string that was supplied through the
         constructor option 'convo_layers_config'.  The output produced by
         the call to 'parse_config_string_for_convo_layers()' is supplied
         as the argument to build_convo_layers().

    (2)  build_fc_layers()

         From the list of ints supplied through the constructor option
         'fc_layers_config', this method constructs the fully-connected
         portion of the overall network.

    (3)  check_a_sampling_of_images()        

         Displays the first batch_size number of images in your dataset.


    (4)  display_tensor_as_image()

         This method will display any tensor of shape (3,H,W), (1,H,W), or
         just (H,W) as an image. If any further data normalizations is
         needed for constructing a displayable image, the method takes care
         of that.  It has two input parameters: one for the tensor you want
         displayed as an image and the other for a title for the image
         display.  The latter parameter is default initialized to an empty
         string.

    (5)  load_cifar_10_dataset()

         This is just a convenience method that calls on Torchvision's
         functionality for creating a data loader.

    (6)  load_cifar_10_dataset_with_augmentation()             

         This convenience method also creates a data loader but it also
         includes the syntax for data augmentation.

    (7)  parse_config_string_for_convo_layers()

         As mentioned in the Introduction, DLStudio module allows you to
         specify a convolutional network with a string provided the string
         obeys the formatting convention described in the comment block of
         this method.  This method is for parsing such a string. The string
         itself is presented to the module through the constructor option
         'convo_layers_config'.

    (8)  run_code_for_testing()

         This is the method runs the trained model on the test data. Its
         output is a confusion matrix for the classes and the overall
         accuracy for each class.  The method has one input parameter which
         is set to the network to be tested.  This learnable parameters in
         the network are initialized with the disk-stored version of the
         trained model.

    (9)  run_code_for_training()

         This is the method that does all the training work. If a GPU was
         detected at the time an instance of the module was created, this
         method takes care of making the appropriate calls in order to
         transfer the tensors involved into the GPU memory.

    (10) save_model()

         Writes the model out to the disk at the location specified by the
         constructor option 'path_saved_model'.  Has one input parameter
         for the model that needs to be written out.

    (11) show_network_summary()

         Displays a print representation of your network and calls on the
         torchsummary module to print out the shape of the tensor at the
         output of each layer in the network. The method has one input
         parameter which is set to the network whose summary you want to
         see.


@title 
INNER CLASSES OF THE MODULE:

    The purpose of the following two inner classes is to demonstrate how
    you can create a custom class for your own network and test it within
    the framework provided by the DLStudio module.

    (1)  class ExperimentsWithSequential

         This class is my demonstration of experimenting with a network
         that I found on GitHub.  I copy-and-pasted it in this class to
         test its capabilities.  How to call on such a custom class is
         shown by the following script in the Examples directory:

                     playing_with_sequential.py

    (2)  class ExperimentsWithCIFAR

         This is very similar to the previous inner class, but uses a
         common example of a network for experimenting with the CIFAR-10
         dataset. Consisting of 32x32 images, this is a great dataset for
         creating classroom demonstrations of convolutional networks.
         As to how you should use this class is shown in the following
         script

                    playing_with_cifar10.py

         in the Examples directory of the distribution.

    (3)  class AutogradCustomization

         The purpose of this class is to illustrate how to extend Autograd
         with additional functionality. What's shown is an implementation of 
         the recommended approach at the following documentation page:

               https://pytorch.org/docs/stable/notes/extending.html

    (4)  class SkipConnections

         This class is for investigating the power of skip connections in
         deep networks.  Skip connections are used to mitigate a serious
         problem associated with deep networks --- the problem of vanishing
         gradients.  It has been argued theoretically and demonstrated
         empirically that as the depth of a neural network increases, the
         gradients of the loss become more and more muted for the early
         layers in the network.



@title 
THE Examples DIRECTORY:

    The Examples subdirectory in the distribution contains the following
    three scripts:

    (1)  playing_with_reconfig.py

         Shows how you can specify a convolution network with a
         configuration string.  The DLStudio module parses the string
         constructs the network.

    (2)  playing_with_sequential.py

         Shows you how you can call on a custom inner class of the
         'DLStudio' module that is meant to experiment with your own
         network.  The name of the inner class in this example script is
         ExperimentsWithSequential

    (3)  playing_with_cifar10.py

         This is very similar to the previous example script but is based
         on the inner class ExperimentsWithCIFAR which uses more common
         examples of networks for playing with the CIFAR-10 dataset.

    (4)  extending_autograd.py

         This provides a demonstration example of the recommended approach
         for giving additional functionality to Autograd --- as mentioned
         in the commented made above about the inner class
         AutogradCustomization.

    (5)  playing_with_skip_connections.py

         This script illustrates how to use the inner class BMEnet of the
         module for experimenting with skip connections in a CNN. As the
         script shows, the constructor of the BMEnet class comes with two
         options: skip_connections and depth.  By turning the first on and
         off, you can directly illustrate in a classroom setting the
         improvement you can get with skip connections.  And by giving an
         appropriate value to the "depth" option, you can show results for
         networks of different depths.


@title
BUGS:

    Please notify the author if you encounter any bugs.  When sending
    email, please place the string 'DLStudio' in the subject line to get
    past the author's spam filter.


@title
ABOUT THE AUTHOR:

    The author, Avinash Kak, is a professor of Electrical and Computer
    Engineering at Purdue University.  For all issues related to this
    module, contact the author at kak@purdue.edu If you send email, please
    place the string "DLStudio" in your subject line to get past the
    author's spam filter.

@title
COPYRIGHT:

    Python Software Foundation License

    Copyright 2020 Avinash Kak

@endofdocs
'''


import sys,os,os.path
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision                  
import torchvision.transforms as tvt
import torch.optim as optim
from torchsummary import summary           
import numpy as np
import re
import math
import random
import copy
import matplotlib.pyplot as plt

#______________________________  DLStudio Class Definition  ________________________________

class DLStudio(object):

    def __init__(self, *args, **kwargs ):
        if args:
            raise ValueError(  
                   '''DLStudio constructor can only be called with keyword arguments for 
                      the following keywords: epochs, learning_rate, batch_size, momentum,
                      convo_layers_config, image_size, dataroot, path_saved_model, classes, 
                      image_size, convo_layers_config, fc_layers_config, debug_train, use_gpu, and 
                      debug_test''')
        learning_rate = epochs = batch_size = convo_layers_config = momentum = None
        image_size = fc_layers_config = dataroot =  path_saved_model = classes = use_gpu = None
        debug_train  = debug_test = None
        if 'dataroot' in kwargs                      :   dataroot = kwargs.pop('dataroot')
        if 'learning_rate' in kwargs                 :   learning_rate = kwargs.pop('learning_rate')
        if 'momentum' in kwargs                      :   momentum = kwargs.pop('momentum')
        if 'epochs' in kwargs                        :   epochs = kwargs.pop('epochs')
        if 'batch_size' in kwargs                    :   batch_size = kwargs.pop('batch_size')
        if 'convo_layers_config' in kwargs           :   convo_layers_config = kwargs.pop('convo_layers_config')
        if 'image_size' in kwargs                    :   image_size = kwargs.pop('image_size')
        if 'fc_layers_config' in kwargs              :   fc_layers_config = kwargs.pop('fc_layers_config')
        if 'path_saved_model' in kwargs              :   path_saved_model = kwargs.pop('path_saved_model')
        if 'classes' in kwargs                       :   classes = kwargs.pop('classes') 
        if 'use_gpu' in kwargs                       :   use_gpu = kwargs.pop('use_gpu') 
        if 'debug_train' in kwargs                   :   debug_train = kwargs.pop('debug_train') 
        if 'debug_test' in kwargs                    :   debug_test = kwargs.pop('debug_test') 
        if len(kwargs) != 0: raise ValueError('''You have provided unrecognizable keyword args''')
        if dataroot:
            self.dataroot = dataroot
        if convo_layers_config:
            self.convo_layers_config = convo_layers_config
        if image_size:
            self.image_size = image_size
        if fc_layers_config:
            self.fc_layers_config = fc_layers_config
            if fc_layers_config[0] is not -1:
                raise Exception("""\n\n\nYour 'fc_layers_config' construction option is not correct. """
                                """The first element of the list of nodes in the fc layer must be -1 """
                                """because the input to fc will be set automatically to the size of """
                                """the final activation volume of the convolutional part of the network""")
        if  path_saved_model:
            self.path_saved_model = path_saved_model
        if classes:
            self.class_labels = classes
        if learning_rate:
            self.learning_rate = learning_rate
        else:
            self.learning_rate = 1e-6
        if momentum:
            self.momentum = momentum
        if epochs:
            self.epochs = epochs
        if batch_size:
            self.batch_size = batch_size
        if use_gpu is not None:
            self.use_gpu = use_gpu
            if use_gpu is True:
                if torch.cuda.is_available():
                    self.device = torch.device("cuda:0")
                else:
                    raise Exception("You requested GPU support, but there's no GPU on this machine")
            else:
                self.device = torch.device("cpu")
        if debug_train:                             
            self.debug_train = debug_train
        else:
            self.debug_train = 0
        if debug_test:                             
            self.debug_test = debug_test
        else:
            self.debug_test = 0
        self.debug_config = 0
#        self.device = torch.device("cuda:0" if torch.cuda.is_available() and self.use_gpu is False else "cpu")

    def parse_config_string_for_convo_layers(self):
        '''
        Each collection of 'n' otherwise identical layers in a convolutional network is 
        specified by a string that looks like:

                                 "nx[a,b,c,d]-MaxPool(k)"
        where 
                n      =  num of this type of convo layer
                a      =  number of out_channels                      [in_channels determined by prev layer] 
                b,c    =  kernel for this layer is of size (b,c)      [b along height, c along width]
                d      =  stride for convolutions
                k      =  maxpooling over kxk patches with stride of k

        Example:
                     "n1x[a1,b1,c1,d1]-MaxPool(k1)  n2x[a2,b2,c2,d2]-MaxPool(k2)"
        '''
        configuration = self.convo_layers_config
        configs = configuration.split()
        all_convo_layers = []
        image_size_after_layer = self.image_size
        for k,config in enumerate(configs):
            two_parts = config.split('-')
            how_many_conv_layers_with_this_config = int(two_parts[0][:config.index('x')])
            if self.debug_config:
                print("\n\nhow many convo layers with this config: %d" % how_many_conv_layers_with_this_config)
            maxpooling_size = int(re.findall(r'\d+', two_parts[1])[0])
            if self.debug_config:
                print("\nmax pooling size for all convo layers with this config: %d" % maxpooling_size)
            for conv_layer in range(how_many_conv_layers_with_this_config):            
                convo_layer = {'out_channels':None, 
                               'kernel_size':None, 
                               'convo_stride':None, 
                               'maxpool_size':None,
                               'maxpool_stride': None}
                kernel_params = two_parts[0][config.index('x')+1:][1:-1].split(',')
                if self.debug_config:
                    print("\nkernel_params: %s" % str(kernel_params))
                convo_layer['out_channels'] = int(kernel_params[0])
                convo_layer['kernel_size'] = (int(kernel_params[1]), int(kernel_params[2]))
                convo_layer['convo_stride'] =  int(kernel_params[3])
                image_size_after_layer = [x // convo_layer['convo_stride'] for x in image_size_after_layer]
                convo_layer['maxpool_size'] = maxpooling_size
                convo_layer['maxpool_stride'] = maxpooling_size
                image_size_after_layer = [x // convo_layer['maxpool_size'] for x in image_size_after_layer]
                all_convo_layers.append(convo_layer)
        configs_for_all_convo_layers = {i : all_convo_layers[i] for i in range(len(all_convo_layers))}
        if self.debug_config:
            print("\n\nAll convo layers: %s" % str(configs_for_all_convo_layers))
        last_convo_layer = configs_for_all_convo_layers[len(all_convo_layers)-1]
        out_nodes_final_layer = image_size_after_layer[0] * image_size_after_layer[1] * \
                                                                      last_convo_layer['out_channels']
        self.fc_layers_config[0] = out_nodes_final_layer
        self.configs_for_all_convo_layers = configs_for_all_convo_layers
        return configs_for_all_convo_layers


    def build_convo_layers(self, configs_for_all_convo_layers):
        conv_layers = nn.ModuleList()
        in_channels_for_next_layer = None
        for layer_index in configs_for_all_convo_layers:
            if self.debug_config:
                print("\n\n\nLayer index: %d" % layer_index)
            in_channels = 3 if layer_index == 0 else in_channels_for_next_layer
            out_channels = configs_for_all_convo_layers[layer_index]['out_channels']
            kernel_size = configs_for_all_convo_layers[layer_index]['kernel_size']
            padding = tuple((k-1) // 2 for k in kernel_size)
            stride       = configs_for_all_convo_layers[layer_index]['convo_stride']
            maxpool_size = configs_for_all_convo_layers[layer_index]['maxpool_size']
            if self.debug_config:
                print("\n     in_channels=%d   out_channels=%d    kernel_size=%s     stride=%s    \
                maxpool_size=%s" % (in_channels, out_channels, str(kernel_size), str(stride), 
                str(maxpool_size)))
            conv_layers.append( nn.Conv2d( in_channels,out_channels,kernel_size,stride=stride,padding=padding) )
            conv_layers.append( nn.MaxPool2d( maxpool_size ) )
            conv_layers.append( nn.ReLU() ),
            in_channels_for_next_layer = out_channels
        return conv_layers


    def build_fc_layers(self):
        fc_layers = nn.ModuleList()
        for layer_index in range(len(self.fc_layers_config) - 1):
            fc_layers.append( nn.Linear( self.fc_layers_config[layer_index], 
                                                                self.fc_layers_config[layer_index+1] ) )
        return fc_layers            


    def load_cifar_10_dataset(self):       
        '''
        We make sure that the transformation applied to the image end the images being normalized.
        Consider this call to normalize: "Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))".  The three
        numbers in the first tuple affect the means in the three color channels and the three 
        numbers in the second tuple affect the standard deviations.  In this case, we want the 
        image value in each channel to be changed to:

                 image_channel_val = (image_channel_val - mean) / std

        So with mean and std both set 0.5 for all three channels, if the image tensor originally 
        was between 0 and 1.0, after this normalization, the tensor will be between -1.0 and +1.0. 
        If needed we can do inverse normalization  by

                 image_channel_val  =   (image_channel_val * std) + mean
        '''
        ##   The call to ToTensor() converts the usual int range 0-255 for pixel values to 0-1.0 float vals
        ##   But then the call to Normalize() changes the range to -1.0-1.0 float vals.
        transform = tvt.Compose([tvt.ToTensor(),
                                 tvt.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])    ## accuracy: 51%
        ##  Define where the training and the test datasets are located:
        train_data_loc = torchvision.datasets.CIFAR10(root=self.dataroot, train=True,
                                                    download=True, transform=transform)
        test_data_loc = torchvision.datasets.CIFAR10(root=self.dataroot, train=False,
                                                    download=True, transform=transform)
        ##  Now create the data loaders:
        self.train_data_loader = torch.utils.data.DataLoader(train_data_loc,batch_size=self.batch_size,
                                                                            shuffle=True, num_workers=2)
        self.test_data_loader = torch.utils.data.DataLoader(test_data_loc,batch_size=self.batch_size,
                                                                           shuffle=False, num_workers=2)

    def load_cifar_10_dataset_with_augmentation(self):             
        '''
        In general, we want to do data augmentation for training:
        '''
        transform_train = tvt.Compose([
                                  tvt.RandomCrop(32, padding=4),
                                  tvt.RandomHorizontalFlip(),
                                  tvt.ToTensor(),
#                                  tvt.Normalize((0.20, 0.20, 0.20), (0.20, 0.20, 0.20))]) 
                                  tvt.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])        
        ##  Don't need any augmentation for the test data: 
        transform_test = tvt.Compose([
                               tvt.ToTensor(),
#                               tvt.Normalize((0.20, 0.20, 0.20), (0.20, 0.20, 0.20))])  
                               tvt.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        ##  Define where the training and the test datasets are located
        train_data_loc = torchvision.datasets.CIFAR10(
                        root=self.dataroot, train=True, download=True, transform=transform_train)
        test_data_loc = torchvision.datasets.CIFAR10(
                      root=self.dataroot, train=False, download=True, transform=transform_test)
        ##  Now create the data loaders:
        self.train_data_loader = torch.utils.data.DataLoader(train_data_loc, batch_size=self.batch_size, 
                                                                     shuffle=True, num_workers=2)
        self.test_data_loader = torch.utils.data.DataLoader(test_data_loc, batch_size=self.batch_size, 
                                                                 shuffle=False, num_workers=2)

    def imshow(self, img):
        '''
        called by display_tensor_as_image() for displaying the image
        '''
        img = img / 2 + 0.5     # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()


    class Net(nn.Module):
        def __init__(self, convo_layers, fc_layers):
            super(DLStudio.Net, self).__init__()
            self.my_modules_convo = convo_layers
            self.my_modules_fc = fc_layers
        def forward(self, x):
            for m in self.my_modules_convo:
                x = m(x)
            x = x.view(x.size(0), -1)
            for m in self.my_modules_fc:
                x = m(x)
            return x

    def show_network_summary(self, net):
        print("\n\n\nprinting out the model:")
        print(net)
        print("\n\n\na summary of input/output for the model:")
        summary(net, (3,self.image_size[0],self.image_size[1]),-1, device='cpu')


    def run_code_for_training(self, net):        
        filename_for_out = "performance_numbers_" + str(self.epochs) + ".txt"
        FILE = open(filename_for_out, 'w')
        net = copy.deepcopy(net)
        net = net.to(self.device)
        '''
        We will use torch.nn.CrossEntropyLoss for the loss function.  Assume that the vector
        x corresponds to the values at the 10 output nodes. We will interpret normalized versions
        of these values as  probabilities --- the normalization being as shown inside the square
        brackets below.  Let 'class' be the true class for the input --- remember 'class' in an
        integer index in range(10). If our classification was absolutely correct, the NORMALIZED
        value for x[class], with normalization being carried out by the ratio inside the square
        brackets, would be 1 and x would be zero at the other nine positions in the vector.
        In this case, the ratio inside the brackets shown below would be 1.0 and the log of
        that would be 0.  That is, when a correct classification decision is made, the value for 
        CrossEntropyLoss would be zero.  On other hand, when an incorrect decision is made
        and we examine the value of the same element x[class], it will DEFINITELY be less
        than 1 and possibly even 0. The closer x[class] is to zero, the larger the value for
        CrossEntropyLoss shown below.
                                                  _                      _                              
                                                 |     exp( x[class] )    |
              CrossEntropyLoss(x, class) = - log |  --------------------- |
                                                 |_  \sum_j exp( x[j] )  _|
                                                    
        Note that "exp( x[class])"  is always positive and, by normalizing it with the
        summation in the denominator, the quantity inside the square brackets is guaranteed
        to be in the range [0,1.0].  Since the log of a fraction is always negative, the
        value calculated for the CrossEntropyLoss when the label assigned to an input is
        'class' will always be a positive number in the range [0, +inf).  In summary, the loss
        is zero when the output classification is correct and some large positive number when
        the classification is wrong.
        '''
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(net.parameters(), lr=self.learning_rate, momentum=self.momentum)
        for epoch in range(self.epochs):  
            ##  We will use running_loss to accumulate the losses over 2000 batches in order
            ##  to present an averaged (over 2000) loss to the user.
            print("\n")
            running_loss = 0.0
            for i, data in enumerate(self.train_data_loader):
                inputs, labels = data
                if self.debug_train and i % 2000 == 1999:
                    print("\n\n[iter=%d:] Ground Truth:     " % (i+1) + 
                    ' '.join('%5s' % self.class_labels[labels[j]] for j in range(self.batch_size)))
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)
                ##  Since PyTorch likes to construct dynamic computational graphs, we need to
                ##  zero out the previously calculated gradients for the learnable parameters:
                optimizer.zero_grad()
                # Make the predictions with the model:
                outputs = net(inputs)
                loss = criterion(outputs, labels)
                if self.debug_train and i % 2000 == 1999:
                    _, predicted = torch.max(outputs.data, 1)
                    print("[iter=%d:] Predicted Labels: " % (i+1) + 
                     ' '.join('%5s' % self.class_labels[predicted[j]] for j in range(self.batch_size)))
                    self.display_tensor_as_image(torchvision.utils.make_grid(inputs, normalize=True), 
                                            "see terminal for TRAINING results at iter=%d" % (i+1))
                loss.backward()
                optimizer.step()
                ##  Present to the average value of the loss over the past 2000 batches:            
                running_loss += loss.item()
                if i % 2000 == 1999:    
#                    print("[epoch:%d, batch:%5d] loss: %.3f" % (epoch + 1, i + 1, running_loss / float(2000)))
                    avg_loss = running_loss / float(2000)
                    print("[epoch:%d, batch:%5d] loss: %.3f" % (epoch + 1, i + 1, avg_loss))
                    FILE.write("%.3f\n" % avg_loss)
                    FILE.flush()
                    running_loss = 0.0
        print("\nFinished Training\n")
        self.save_model(net)


    def display_tensor_as_image(self, tensor, title=""):
        '''
        This method converts the argument tensor into a photo image that you can display
        in your terminal screen. It can convert tensors of three different shapes
        into images: (3,H,W), (1,H,W), and (H,W), where H, for height, stands for the
        number of pixels in the vertical direction and W, for width, for the same
        along the horizontal direction.  When the first element of the shape is 3,
        that means that the tensor represents a color image in which each pixel in
        the (H,W) plane has three values for the three color channels.  On the other
        hand, when the first element is 1, that stands for a tensor that will be
        shown as a grayscale image.  And when the shape is just (H,W), that is
        automatically taken to be for a grayscale image.
        '''
        tensor_range = (torch.min(tensor).item(), torch.max(tensor).item())
        if tensor_range == (-1.0,1.0):
            ##  The tensors must be between 0.0 and 1.0 for the display:
            print("\n\n\nimage un-normalization called")
            tensor = tensor/2.0 + 0.5     # unnormalize
        plt.figure(title)
        ###  The call to plt.imshow() shown below needs a numpy array. We must also
        ###  transpose the array so that the number of channels (the same thing as the
        ###  number of color planes) is in the last element.  For a tensor, it would be in
        ###  the first element.
        if tensor.shape[0] == 3 and len(tensor.shape) == 3:
            plt.imshow( tensor.numpy().transpose(1,2,0) )
        ###  If the grayscale image was produced by calling torchvision.transform's
        ###  ".ToPILImage()", and the result converted to a tensor, the tensor shape will
        ###  again have three elements in it, however the first element that stands for
        ###  the number of channels will now be 1
        elif tensor.shape[0] == 1 and len(tensor.shape) == 3:
            tensor = tensor[0,:,:]
            plt.imshow( tensor.numpy(), cmap = 'gray' )
        ###  For any one color channel extracted from the tensor representation of a color
        ###  image, the shape of the tensor will be (W,H):
        elif len(tensor.shape) == 2:
            plt.imshow( tensor.numpy(), cmap = 'gray' )
        else:
            sys.exit("\n\n\ntensor for image is ill formed -- aborting")
        plt.show()


    def check_a_sampling_of_images(self):
        '''
        Displays the first batch_size number of images in your dataset.
        '''
        dataiter = iter(self.train_data_loader)
        images, labels = dataiter.next()
        # Since negative pixel values make no sense for display, setting the 'normalize' 
        # option to True will change the range back from (-1.0,1.0) to (0.0,1.0):
        self.display_tensor_as_image(torchvision.utils.make_grid(images, normalize=True))
        # Print class labels for the images shown:
        print(' '.join('%5s' % self.class_labels[labels[j]] for j in range(self.batch_size)))


    def save_model(self, model):
        '''
        Save the trained model to a disk file
        '''
        torch.save(model.state_dict(), self.path_saved_model)
    

    def run_code_for_testing(self, net):
        net.load_state_dict(torch.load(self.path_saved_model))
        ##  In what follows, in addition to determining the predicted label for each test
        ##  image, we will also compute some stats to measure the overall performance of
        ##  the trained network.  This we will do in two different ways: For each class,
        ##  we will measure how frequently the network predicts the correct labels.  In
        ##  we will compute the confusion matrix for the predictions.
        correct = 0
        total = 0
        confusion_matrix = torch.zeros(len(self.class_labels), len(self.class_labels))
        class_correct = [0] * len(self.class_labels)
        class_total = [0] * len(self.class_labels)
        with torch.no_grad():
            for i,data in enumerate(self.test_data_loader):
                ##  data is set to the images and the labels for one batch at a time:
                images, labels = data
                if self.debug_test and i % 1000 == 0:
                    print("\n\n[i=%d:] Ground Truth:     " %i + ' '.join('%5s' % self.class_labels[labels[j]] 
                                                                    for j in range(self.batch_size)))
                outputs = net(images)
                ##  max() returns two things: the max value and its index in the 10 element
                ##  output vector.  We are only interested in the index --- since that is 
                ##  essentially the predicted class label:
                _, predicted = torch.max(outputs.data, 1)
                if self.debug_test and i % 1000 == 0:
                    print("[i=%d:] Predicted Labels: " %i + ' '.join('%5s' % self.class_labels[predicted[j]]
                                                                    for j in range(self.batch_size)))
                    self.display_tensor_as_image(torchvision.utils.make_grid(images, normalize=True), 
                                                         "see terminal for test results at i=%d" % i)
                for label,prediction in zip(labels,predicted):
                        confusion_matrix[label][prediction] += 1
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
                ##  comp is a list of size batch_size of "True" and "False" vals
                comp = predicted == labels       
                for j in range(self.batch_size):
                    label = labels[j]
                    ##  The following works because, in a numeric context, the boolean value
                    ##  "False" is the same as number 0 and the boolean value True is the 
                    ##  same as number 1. For that reason "4 + True" will evaluate to 5 and
                    ##  "4 + False" will evaluate to 4.  Also, "1 == True" evaluates to "True"
                    ##  "1 == False" evaluates to "False".  However, note that "1 is True" 
                    ##  evaluates to "False" because the operator "is" does not provide a 
                    ##  numeric context for "True". And so on.  In the statement that follows,
                    ##  while  c[j].item() will either return "False" or "True", for the 
                    ##  addition operator, Python will use the values 0 and 1 instead.
                    class_correct[label] += comp[j].item()
                    class_total[label] += 1
        for j in range(len(self.class_labels)):
            print('Prediction accuracy for %5s : %2d %%' % (
                               self.class_labels[j], 100 * class_correct[j] / class_total[j]))
        print("\n\n\nOverall accuracy of the network on the 10000 test images: %d %%" % 
                                                               (100 * correct / float(total)))
        print("\n\nDisplaying the confusion matrix:\n")
        out_str = "         "
        for j in range(len(self.class_labels)):  out_str +=  "%7s" % self.class_labels[j]   
        print(out_str + "\n")
        for i,label in enumerate(self.class_labels):
            out_percents = [100 * confusion_matrix[i,j] / float(class_total[i]) 
                                                      for j in range(len(self.class_labels))]
            out_percents = ["%.2f" % item.item() for item in out_percents]
            out_str = "%6s:  " % self.class_labels[i]
            for j in range(len(self.class_labels)): out_str +=  "%7s" % out_percents[j]
            print(out_str)


    ##################  Start Definition of Inner Class ExperimentsWithSequential ##############

    class ExperimentsWithSequential(nn.Module):                                
        """
        Demonstrates how to use the torch.nn.Sequential container class
        """
        def __init__(self, dl_studio ):
            super(DLStudio.ExperimentsWithSequential, self).__init__()
            self.dl_studio = dl_studio

        def load_cifar_10_dataset(self):       
            self.dl_studio.load_cifar_10_dataset()

        def load_cifar_10_dataset_with_augmentation(self):             
            self.dl_studio.load_cifar_10_dataset_with_augmentation()

        class Net(nn.Module):
            """
            To see if the DLStudio class would work with any network that a user may want
            to experiment with, I copy-and-pasted the the network shown below from the following
            page by Zhenye at GitHub:
                         https://zhenye-na.github.io/2018/09/28/pytorch-cnn-cifar10.html
            """
            def __init__(self):
                super(DLStudio.ExperimentsWithSequential.Net, self).__init__()
                self.conv_seqn = nn.Sequential(
                    # Conv Layer block 1:
                    nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1),
                    nn.BatchNorm2d(32),
                    nn.ReLU(inplace=True),
                    nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
                    nn.ReLU(inplace=True),
                    nn.MaxPool2d(kernel_size=2, stride=2),
                    # Conv Layer block 2:
                    nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
                    nn.BatchNorm2d(128),
                    nn.ReLU(inplace=True),
                    nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
                    nn.ReLU(inplace=True),
                    nn.MaxPool2d(kernel_size=2, stride=2),
                    nn.Dropout2d(p=0.05),
                    # Conv Layer block 3:
                    nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),
                    nn.BatchNorm2d(256),
                    nn.ReLU(inplace=True),
                    nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),
                    nn.ReLU(inplace=True),
                    nn.MaxPool2d(kernel_size=2, stride=2),
                )
                self.fc_seqn = nn.Sequential(
                    nn.Dropout(p=0.1),
                    nn.Linear(4096, 1024),
                    nn.ReLU(inplace=True),
                    nn.Linear(1024, 512),
                    nn.ReLU(inplace=True),
                    nn.Dropout(p=0.1),
                    nn.Linear(512, 10)
                )
    
            def forward(self, x):
                x = self.conv_seqn(x)
                # flatten
                x = x.view(x.size(0), -1)
                x = self.fc_seqn(x)
                return x

        def run_code_for_training(self, net):        
            self.dl_studio.run_code_for_training(net)

        def save_model(self, model):
            '''
            Save the trained model to a disk file
            '''
            torch.save(model.state_dict(), self.dl_studio.path_saved_model)

        def run_code_for_testing(self, model):
            self.dl_studio.run_code_for_testing(model)


    ##################  Start Definition of Inner Class ExperimentsWithCIFAR ##############

    class ExperimentsWithCIFAR(nn.Module):              

        def __init__(self, dl_studio ):
            super(DLStudio.ExperimentsWithCIFAR, self).__init__()
            self.dl_studio = dl_studio

        def load_cifar_10_dataset(self):       
            self.dl_studio.load_cifar_10_dataset()

        def load_cifar_10_dataset_with_augmentation(self):             
            self.dl_studio.load_cifar_10_dataset_with_augmentation()

        ##  You can instantiate two different types when experimenting with the inner class
        ##  ExperimentsWithCIFAR.  The network shown below is from the PyTorch tutorial
        ##
        ##     https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
        ##
        class Net(nn.Module):
            def __init__(self):
                super(DLStudio.ExperimentsWithCIFAR.Net, self).__init__()
                self.conv1 = nn.Conv2d(3, 6, 5)
                self.pool = nn.MaxPool2d(2, 2)
                self.conv2 = nn.Conv2d(6, 16, 5)
                self.fc1 = nn.Linear(16 * 5 * 5, 120)
                self.fc2 = nn.Linear(120, 84)
                self.fc3 = nn.Linear(84, 10)
        
            def forward(self, x):
                x = self.pool(F.relu(self.conv1(x)))
                x = self.pool(F.relu(self.conv2(x)))
                x = x.view(-1, 16 * 5 * 5)
                x = F.relu(self.fc1(x))
                x = F.relu(self.fc2(x))
                x = self.fc3(x)
                return x

        ##  Instead of using the network shown above, you can also use the network shown below.
        ##  if you are playing with the ExperimentsWithCIFAR inner class. If that's what you
        ##  want to do, in the script "playing_with_cifar10.py" in the Examples directory,
        ##  you will need to replace the statement
        ##                          model = exp_cifar.Net()
        ##  by the statement
        ##                          model = exp_cifar.Net2()        
        ##
        class Net2(nn.Module):
            def __init__(self):
                """
                I created this network class just to see if it was possible to simply calculate
                the size of the first of the fully connected layers from strides in the convo
                layers up to that point and from the out_channels used in the top-most convo 
                layer.   In what you see below, I am keeping track of all the strides by pushing 
                them into the array 'strides'.  Subsequently, in the formula shown in line (A),
                I use the product of all strides and the number of out_channels for the topmost
                layer to compute the size of the first fully-connected layer.
                """
                super(DLStudio.ExperimentsWithCIFAR.Net2, self).__init__()
                self.relu = nn.ReLU()
                strides = []
                patch_size = 2
                ## conv1:
                out_ch, ker_size, conv_stride, pool_stride = 128,5,1,2
                self.conv1 = nn.Conv2d(3, out_ch, (ker_size,ker_size), padding=(ker_size-1)//2)     
                self.pool1 = nn.MaxPool2d(patch_size, pool_stride)                                      
                strides += (conv_stride, pool_stride)
                ## conv2:
                in_ch = out_ch
                out_ch, ker_size, conv_stride, pool_stride = 128,3,1,2
                self.conv2 = nn.Conv2d(in_ch, out_ch, ker_size, padding=(ker_size-1)//2)
                self.pool2 = nn.MaxPool2d(patch_size, pool_stride)                                      
                strides += (conv_stride, pool_stride)
                ## conv3:                   
                ## meant for repeated invocation, must have same in_ch, out_ch and strides of 1
                in_ch = out_ch
                out_ch, ker_size, conv_stride, pool_stride = in_ch,2,1,1
                self.conv3 = nn.Conv2d(in_ch, out_ch, ker_size, padding=1)
                self.pool3 = nn.MaxPool2d(patch_size, pool_stride)                                      
#                strides += (conv_stride, pool_stride)
                ## figure out the number of nodes needed for entry into fc:
                in_size_for_fc = out_ch * (32 // np.prod(strides)) ** 2                          ## (A)
                self.in_size_for_fc = in_size_for_fc
                self.fc1 = nn.Linear(in_size_for_fc, 150)
                self.fc2 = nn.Linear(150, 100)
                self.fc3 = nn.Linear(100, 10)
        
            def forward(self, x):
                ##  We know that forward() begins its with work x shaped as (4,3,32,32) where
                ##  4 is the batch size, 3 in_channels, and where the input image size is 32x32.
                x = self.relu(self.conv1(x))  
                x = self.pool1(x)             
                x = self.relu(self.conv2(x))
                x = self.pool2(x)             
                for _ in range(5):
                    x = self.pool3(self.relu(self.conv3(x)))
                x = x.view(-1, self.in_size_for_fc)
                x = self.relu(self.fc1( x ))
                x = self.relu(self.fc2( x ))
                x = self.fc3(x)
                return x

        def run_code_for_training(self, net):        
            self.dl_studio.run_code_for_training(net)
            
        def save_model(self, model):
            '''
            Save the trained model to a disk file
            '''
            torch.save(model.state_dict(), self.dl_studio.path_saved_model)

        def run_code_for_testing(self, model):
            self.dl_studio.run_code_for_testing(model)


    #################  Start Definition of Inner Class AutogradCustomization  #############

    class AutogradCustomization(nn.Module):             
        """
        This class illustrates how you can add additional functionality of Autograd by 
        following the instructions posted at
                   https://pytorch.org/docs/stable/notes/extending.html
        """

        def __init__(self, dl_studio, num_samples_per_class):
            super(DLStudio.AutogradCustomization, self).__init__()
            self.dl_studio = dl_studio
            self.num_samples_per_class = num_samples_per_class


        class DoSillyWithTensor(torch.autograd.Function):                  
            """        
            Extending Autograd requires that you define a new verb class, as I have with
            the class DoSillyWithTensor shown below, with definitions for two static
            methods, "forward()" and "backward()".  An instance constructed from this
            class is callable.  So when, in the "forward()" of the network, you pass a
            training sample through an instance of DoSillyWithTensor, it is subject to
            the code shown below in the "forward()"  of this class.
            """
            @staticmethod
            def forward(ctx, input):
                """
                The parameter 'input' is set to the training sample that is being 
                processed by an instance of DoSillyWithTensor in the "forward()" of a
                network.  We first make a deep copy of this tensor (which should be a 
                32-bit float) and then we subject the copy to a conversion to a one-byte 
                integer, which should cause a significant loss of information. We 
                calculate the difference between the original 32-bit float and the 8-bit 
                version and store it away in the context variable "ctx".
                """
                input_orig = input.clone().double()
                input = input.to(torch.uint8).double()
                diff = input_orig.sub(input)
                ctx.save_for_backward(diff)
                return input

            @staticmethod
            def backward(ctx, grad_output):
                """
                Whatever was stored in the context variable "ctx" during the forward pass
                can be retrieved in the backward pass as shown below.
                """
                diff, = ctx.saved_tensors
                grad_input = grad_output.clone()
                grad_input = grad_input + diff
                return grad_input
        
        def gen_training_data(self):        
            mean1,mean2   = [3.0,3.0], [5.0,5.0]
            covar1,covar2 = [[1.0,0.0], [0.0,1.0]], [[1.0,0.0], [0.0,1.0]]
            data1 = [(list(x),1) for x in np.random.multivariate_normal(mean1, covar1, 
                                                                     self.num_samples_per_class)]
            data2 = [(list(x),2) for x in np.random.multivariate_normal(mean2, covar2, 
                                                                     self.num_samples_per_class)]
            training_data = data1 + data2
            random.shuffle( training_data )
            self.training_data = training_data 

        def train_with_straight_autograd(self):
            dtype = torch.float
            D_in,H,D_out = 2,10,2
#           w1 = torch.randn(D_in, H, device="cpu", dtype=dtype, requires_grad=True)
#           w2 = torch.randn(H, D_out, device="cpu", dtype=dtype, requires_grad=True)
            w1 = torch.randn(D_in, H, device="cpu", dtype=dtype)
            w2 = torch.randn(H, D_out, device="cpu", dtype=dtype)
            w1 = w1.to(self.dl_studio.device)
            w2 = w2.to(self.dl_studio.device)
            w1.requires_grad_()
            w2.requires_grad_()
            Loss = []
            for epoch in range(self.dl_studio.epochs):
                for i,data in enumerate(self.training_data):
                    input, label = data
                    x,y = torch.as_tensor(np.array(input)), torch.as_tensor(np.array(label))
                    x,y = x.float(), y.float()
                    if self.dl_studio.use_gpu is True:
                        x,y = x.to(self.dl_studio.device), y.to(self.dl_studio.device)
                    y_pred = x.view(1,-1).mm(w1).clamp(min=0).mm(w2)
                    loss = (y_pred - y).pow(2).sum()
                    if i % 200 == 199:
                        Loss.append(loss.item())
                        print("epoch=%d i=%d" % (epoch,i), loss.item())
#                   w1.retain_grad()
#                   w2.retain_grad()
                    loss.backward()       
                    with torch.no_grad():
                        w1 -= self.dl_studio.learning_rate * w1.grad
                        w2 -= self.dl_studio.learning_rate * w2.grad
                        w1.grad.zero_()
                        w2.grad.zero_()
            print("\n\n\nLoss: %s" % str(Loss))
            import matplotlib.pyplot as plt
            plt.figure("Loss vs training (straight autograd)")
            plt.plot(Loss)
            plt.show()

        def train_with_extended_autograd(self):
            dtype = torch.float
            D_in,H,D_out = 2,10,2
#           w1 = torch.randn(D_in, H, device="cpu", dtype=dtype, requires_grad=True)
#           w2 = torch.randn(H, D_out, device="cpu", dtype=dtype, requires_grad=True)
            w1 = torch.randn(D_in, H, device="cpu", dtype=dtype)
            w2 = torch.randn(H, D_out, device="cpu", dtype=dtype)
            w1 = w1.to(self.dl_studio.device)
            w2 = w2.to(self.dl_studio.device)
            w1.requires_grad_()
            w2.requires_grad_()
            Loss = []
            for epoch in range(self.dl_studio.epochs):
                for i,data in enumerate(self.training_data):
                    ## Constructing an instance of DoSillyWithTensor. It is callable.
                    do_silly = DLStudio.AutogradCustomization.DoSillyWithTensor.apply      
                    input, label = data
                    x,y = torch.as_tensor(np.array(input)), torch.as_tensor(np.array(label))
                    ## Now process the training instance with the "do_silly" instance:
                    x = do_silly(x)                                 
                    x,y = x.float(), y.float()
                    x,y = x.to(self.dl_studio.device), y.to(self.dl_studio.device)
                    y_pred = x.view(1,-1).mm(w1).clamp(min=0).mm(w2)
                    loss = (y_pred - y).pow(2).sum()
                    if i % 200 == 199:
                        Loss.append(loss.item())
                        print("epoch=%d i=%d" % (epoch,i), loss.item())
#                   w1.retain_grad()
#                   w2.retain_grad()
                    loss.backward()       
                    with torch.no_grad():
                        w1 -= self.dl_studio.learning_rate * w1.grad
                        w2 -= self.dl_studio.learning_rate * w2.grad
                        w1.grad.zero_()
                        w2.grad.zero_()
            print("\n\n\nLoss: %s" % str(Loss))
            import matplotlib.pyplot as plt
            plt.figure("loss vs training (extended autograd)")
            plt.plot(Loss)
            plt.show()

   ###############  Start Definition of Inner Class SkipConnections  ##############

    class SkipConnections(nn.Module):             
        """
        This educational class is meant for illustrating the concepts related to the 
        use of skip connections in neural network.  It is now well known that deep
        networks are difficult to train because of the vanishing gradients problem.
        What that means is that as the depth of network increases, the loss gradients
        calculated for the early layers become more and more muted, which suppresses
        the learning of the parameters in those layers.  An important mitigation
        strategy for addressing this problem consists of creating a CNN using blocks
        with skip connections.

        With the code shown in this inner class of the module, you can now experiment
        with skip connections in a CNN to see how a deep network with this feature
        might improve the classification results.  As you will see in the code shown
        below, the network that allows you construct a CNN with skip connections is
        named BMEnet.  As shown in the script playing_with_skip_connections.py in the
        Examples directory of the distribution, you can easily create a CNN with
        arbitrary depth just by using the "depth" constructor option for the BMEnet
        class.  The basic block of the network constructed by BMEnet is called
        SkipBlock which, very much like the BasicBlock in ResNet-18, has a couple of
        convolutional layers whose output is combined with the input to the block.
    
        Note that the value given to the the "depth" constructor option for the
        BMEnet class does NOT translate directly into the actual depth of the
        CNN. [Again, see the script playing_with_skip_connections.py in the Examples
        directory for how to use this option.] The value of "depth" is translated
        into how many instances of SkipBlock to use for constructing the CNN.
        """

        def load_cifar_10_dataset(self):       
            self.dl_studio.load_cifar_10_dataset()

        def load_cifar_10_dataset_with_augmentation(self):             
            self.dl_studio.load_cifar_10_dataset_with_augmentation()

        def __init__(self, dl_studio):
            super(DLStudio.SkipConnections, self).__init__()
            self.dl_studio = dl_studio

        class SkipBlock(nn.Module):
            def __init__(self, in_ch, out_ch, downsample=False, skip_connections=True):
                super(DLStudio.SkipConnections.SkipBlock, self).__init__()
                self.downsample = downsample
                self.skip_connections = skip_connections
                self.in_ch = in_ch
                self.out_ch = out_ch
                self.convo = nn.Conv2d(in_ch, out_ch, 3, stride=1, padding=1)
                norm_layer = nn.BatchNorm2d
                self.bn = norm_layer(out_ch)
                if downsample:
                    self.downsampler = nn.Conv2d(in_ch, out_ch, 1, stride=2)

            def forward(self, x):
                identity = x                                     
                out = self.convo(x)                              
                out = self.bn(out)                              
                out = torch.nn.functional.relu(out)
                out = self.convo(x)                              
                out = self.bn(out)                              
                out = torch.nn.functional.relu(out)
                if self.downsample:
                    out = self.downsampler(out)
                    identity = self.downsampler(identity)
                if self.skip_connections:
                    if self.in_ch == self.out_ch:
                        out += identity                              
                    else:
                        out[:,:self.in_ch,:,:] += identity
                        out[:,self.in_ch:,:,:] += identity
                return out

        class BMEnet(nn.Module):
            def __init__(self, skip_connections=True, depth=32):
                super(DLStudio.SkipConnections.BMEnet, self).__init__()
                self.pool_count = 3
                self.depth = depth // 2
                self.conv = nn.Conv2d(3, 64, 3, padding=1)
                self.pool = nn.MaxPool2d(2, 2)
                self.skip64 = DLStudio.SkipConnections.SkipBlock(64, 64, skip_connections=skip_connections)
                self.skip64ds = DLStudio.SkipConnections.SkipBlock(64, 64, 
                                                           downsample=True, skip_connections=skip_connections)
                self.skip64to128 = DLStudio.SkipConnections.SkipBlock(64, 128, 
                                                                           skip_connections=skip_connections )
                self.skip128 = DLStudio.SkipConnections.SkipBlock(128, 128, skip_connections=skip_connections)
                self.skip128ds = DLStudio.SkipConnections.SkipBlock(128,128,
                                                              downsample=True, skip_connections=skip_connections)
                self.fc1 =  nn.Linear(128 * (32 // 2**self.pool_count)**2, 1000)
                self.fc2 =  nn.Linear(1000, 10)

            def forward(self, x):
                x = self.pool(torch.nn.functional.relu(self.conv(x)))          
                for _ in range(self.depth // 4):
                    x = self.skip64(x)                                               
                x = self.skip64ds(x)
                for _ in range(self.depth // 4):
                    x = self.skip64(x)                                               
                x = self.skip64to128(x)
                for _ in range(self.depth // 4):
                    x = self.skip128(x)                                               
                x = self.skip128ds(x)                                               
                for _ in range(self.depth // 4):
                    x = self.skip128(x)                                               
                x = x.view(-1, 128 * (32 // 2**self.pool_count)**2 )
                x = torch.nn.functional.relu(self.fc1(x))
                x = self.fc2(x)
                return x            

        def run_code_for_training(self, net):        
            self.dl_studio.run_code_for_training(net)
            
        def save_model(self, model):
            '''
            Save the trained model to a disk file
            '''
            torch.save(model.state_dict(), self.dl_studio.path_saved_model)

        def run_code_for_testing(self, model):
            self.dl_studio.run_code_for_testing(model)


    def plot_loss(self):
        plt.figure()
        plt.plot(self.LOSS)
        plt.show()




#_________________________  End of DLStudio Class Definition ___________________________

#______________________________    Test code follows    _________________________________

if __name__ == '__main__': 
    pass
