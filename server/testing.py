#!/usr/bin/env python
# coding: utf-8

# In[25]:


import tensorflow as tf
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import  shuffle
from sklearn.model_selection import train_test_split
tf.reset_default_graph()


# In[26]:


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # y labels are oh-encoded


# In[27]:


n_input = 784   # input layer (28x28 pixels)
n_output = 10   # output layer (0-9 digits)


# In[28]:


# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# import matplotlib.pyplot as plt
# image_index = 1233 # You may select anything up to 60,000
# print(y_train[image_index]) # The label is 8
# plt.imshow(x_train[image_index], cmap='Greys')


# In[38]:


n_test = mnist.test.num_examples # 10,000


# In[30]:


n_input = 784   # input layer (28x28 pixels)
n_hidden1 = 512 # 1st hidden layer
n_hidden2 = 256 # 2nd hidden layer
n_hidden3 = 128 # 3rd hidden layer
n_output = 10   # output layer (0-9 digits)


# In[31]:


X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_output])
keep_prob = tf.placeholder(tf.float32) 


# In[32]:


weights = {
    'w1': tf.Variable(tf.truncated_normal([n_input, n_hidden1], stddev=0.1)),
    'w2': tf.Variable(tf.truncated_normal([n_hidden1, n_hidden2], stddev=0.1)),
    'w3': tf.Variable(tf.truncated_normal([n_hidden2, n_hidden3], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([n_hidden3, n_output], stddev=0.1)),
}


# In[33]:


biases = {
    'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden1])),
    'b2': tf.Variable(tf.constant(0.1, shape=[n_hidden2])),
    'b3': tf.Variable(tf.constant(0.1, shape=[n_hidden3])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
}


# In[34]:


layer_1 = tf.add(tf.matmul(X, weights['w1']), biases['b1'])
layer_2 = tf.add(tf.matmul(layer_1, weights['w2']), biases['b2'])
layer_3 = tf.add(tf.matmul(layer_2, weights['w3']), biases['b3'])
layer_drop = tf.nn.dropout(layer_3, keep_prob)
output_layer = tf.matmul(layer_3, weights['out']) + biases['out']


# In[35]:


saver = tf.train.Saver()


# In[41]:


mnist.test.images


# In[36]:


with tf.Session() as sess:
  
    saver.restore(sess, "model.ckpt")
    print("Model restored.")
    correct_pred = tf.equal(tf.argmax(output_layer, 1), tf.argmax(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    test_accuracy = sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels, keep_prob:1.0})
    print("\nAccuracy on test set:", test_accuracy)
    os.system("git clone https://github.com/VatsalSoni301/temporary.git")
    os.system("touch temporary/acc.txt")
    file = open("temporary/acc.txt","w")
    file.write(str(test_accuracy))
    file.close()
    os.chdir("/home/vatsal/Documents/IIIT/Sem-2/IAS/Hackathon/temporary")
    os.system("git add . & git commit -m 'Accuracy updated' & git push https://'VatsalSoni301':'vatsal123soni'@github.com/VatsalSoni301/temporary.git")
    
#     pred_y = sess.run(y, feed_dict={x: X_test})

    
#     correct_prediction = tf.equal(tf.argmax(pred_y,1), tf.argmax(Y_test,1))
#     accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#     print("Accuracy:",sess.run(accuracy))

