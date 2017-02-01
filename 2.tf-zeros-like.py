import tensorflow as tf

tensor = tf.zeros([2,3], tf.float32)


x = tf.Variable([[1,2,3],[4,5,6]])
y = tf.zeros_like(x)
w = tf.ones([2,3], tf.float32)

# constant 1-D Tensor populated with the value list
tensor_1d = tf.constant([1,2])

# constant 2-D Tensor populated with the scalar value -1
tensor_2d = tf.constant(-1, shape=[2,2])



# variables have to be explicitly initialized before you can run Ops
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print tensor.eval()
    print tensor_1d.eval()
    print tensor_2d.eval()

import numpy as np
a = np.zeros((3,3))
ta = tf.convert_to_tensor(a)

with tf.Session() as sess:
    print sess.run(ta)