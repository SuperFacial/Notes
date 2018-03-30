### tf.shape(xxx) 和 xxx.get_shape()比较
# 1. 相同点：都可以得到tensor xxx 的尺寸
# 2. 不同点：tf.shape(xxx)中xxx数据的类型可以是tensor,list,array；
#    而xxx.get_shape()中的xxx的数据类型必须是tensor,且返回的是一个tuple.可以通过xxx.get_shape().as_list()得到一个list。
#    而且get方法不需要调用Session类方法，可以直接打印
import tensorflow as tf
import numpy as np
x=tf.truncated_normal([32,32,3],dtype=tf.float32)

sess=tf.Session()
print(sess.run(tf.shape(x))) # [32 32 3]
print(x.get_shape().as_list()) # [32,32,3]
