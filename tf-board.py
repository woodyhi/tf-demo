import tensorflow as tf

sess = tf.Session()


a = tf.constant(10, name='a')
b = tf.constant(32, name='b')
c = tf.add(a, b, name='c')

file_writer = tf.summary.FileWriter('C:/Users/hp/PycharmProjects/tf-demo/logs', sess.graph)
sess.run(tf.global_variables_initializer())

# cmd-line
# tensorboard --logdir=C:/Users/hp/PycharmProjects/tf-demo/logs