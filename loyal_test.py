import numpy as np
import tensorflow as tf

x_tensor = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
x_test=tf.placeholder(tf.float32,[None,4,4,3])




  # [2, 2, 3]

# Output depth
conv_ksize = 64

# Image Properties
image_width = 2
image_height = 2
color_channels = 3

# Convolution filter
filter_size_width = 5
filter_size_height = 5
filter_size=(5,5)
print(filter_size[1])
colo_channels=3


a=((1,2),(2,3))
a=list(a)
type(a)
a
a[0][0]


weight_shape=[filter_size[0],filter_size[1],colo_channels,conv_ksize]

# Input/Image
input = tf.placeholder(
    tf.float32,
    shape=[None, image_height, image_width, color_channels])

# Weight and bias
weight = tf.Variable(tf.truncated_normal(
    [filter_size, color_channels, conv_ksize]))
bias = tf.Variable(tf.zeros(conv_ksize))

# Apply Convolution
conv_layer = tf.nn.conv2d(input, weight, strides=[1, 2, 2, 1], padding='SAME')
# Add bias
conv_layer = tf.nn.bias_add(conv_layer, bias)
# Apply activation function
conv_layer = tf.nn.relu(conv_layer)

sess=tf.Session()
print(sess.run(tf.shape(tf.truncated_normal(weight_shape))[0]))
