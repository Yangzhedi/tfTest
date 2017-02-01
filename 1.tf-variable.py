import tensorflow as tf

# create a variable
w = tf.Variable([[0.5, 1.0]])
x = tf.Variable([[2.0],[1.0]])
y = tf.matmul(w, x)

# print y
print type(x)  # <class 'tensorflow.python.ops.variables.Variable'>


# variables have to be explicitly initialized before you can run Ops
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print y.eval()
    # print x.eval()
    # print w.eval()

# throw an error
# tf.Session().run(init_op)
# print y.eval()

# float32
# tf.zeros([3,4], int32)


tensor = tf.zeros([2,3], tf.float32)
