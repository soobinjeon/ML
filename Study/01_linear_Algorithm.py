import tensorflow as tf
import matplotlib.pyplot as plt

x_data = [1, 2, 3]
y_data = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name='weight')

hypo = x_data * W

cost = tf.reduce_mean(tf.square(hypo - y_data))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

#Launch the graph in a session.
sess = tf.Session();

sess.run(tf.global_variables_initializer())

for step in range(21):
    print(step, sess.run(W))
    sess.run(train)