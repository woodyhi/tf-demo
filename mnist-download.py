from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print("Training data size: ", mnist.train.num_examples)
print("Validating data size: ", mnist.validation.num_examples)
print("Testing data size: ", mnist.test.num_examples)

# import tensorflow as tf
#
# sess = tf.InteractiveSession()
#
# # 占位符
# x = tf.placeholder("float", shape=[None, 784])
# y_ = tf.placeholder("float", shape=[None, 10])
#
# # 变量
# W = tf.Variable(tf.zeros([784, 10]))
# b = tf.Variable(tf.zeros([10]))
# y = tf.nn.softmax(tf.matmul(x, W) + b)
#
# cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#
# file_writer = tf.summary.FileWriter('logs/', sess.graph)
#
# sess.run(tf.global_variables_initializer())
#
# for i in range(1000):
#     print("i = ", i)
#     batch_xs, batch_ys = mnist.train.next_batch(100)
#     sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#
# correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
# print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))