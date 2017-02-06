# coding:utf-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# from tensorflow.examples.tutorials.mnist import input_data
import input_data

print 'Download and Extract MNIST dataset'
mnist = input_data.read_data_sets('data/', one_hot=True)
# print
print 'type of "mnist" is %s' %(type(mnist))
print 'number of train data is %d' %(mnist.train.num_examples)
print 'number of test data is %d' %(mnist.test.num_examples)