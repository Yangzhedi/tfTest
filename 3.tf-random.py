import tensorflow as tf

norm = tf.random_normal([2,3 ], mean=-1, stddev=4)

# shuffle the first dimension of a tensor
c = tf.constant([[1, 2], [3, 4], [5, 6]])
shuff = tf.random_shuffle(c)


# Each time we run these ops, different results are generated
sess = tf.Session()
print sess.run(norm)
print sess.run(shuff)
