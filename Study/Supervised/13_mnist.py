import tensorflow as tf
import random
import matplotlib.pyplot as plt
tf.set_random_seed(777)

from tensorflow.examples.tutorials.mnist import input_data
#Check out http://www.tensorflow.org/get_started/mnist/beginners for
#more information about the mmist dataset
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

nb_classes = 10

#MNIST data image of shape 28 * 28 = 784
X = tf.placeholder(tf.float32, [None,784])
# 0-9 digits recognition = 10 classes
Y = tf.placeholder(tf.float32, [None, nb_classes])

W = tf.Variable(tf.random_normal([784, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bais')

#Hypothesis (softmax)
logit = tf.matmul(X, W)+b
Hypothesis = tf.nn.softmax(logit)

cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logit, labels=Y)
cost = tf.reduce_mean(cost_i)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

#Test model
is_correct = tf.equal(tf.arg_max(Hypothesis, 1), tf.arg_max(Y, 1))
#Calculate accuracy
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

#parameter
training_epochs = 15
batch_size = 100

with tf.Session() as sess:
    #Init
    sess.run(tf.global_variables_initializer())
    #training cycle
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            c, _ = sess.run([cost, optimizer], feed_dict={
                X: batch_xs, Y: batch_ys
            })
            avg_cost += c / total_batch

        print('Epoch:', '%04d' % (epoch+1),
              'cost =', '{:.9f}'.format(avg_cost))

    print("Learning finished")


    # Test the model using test sets
    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={
        X: mnist.test.images, Y: mnist.test.labels}))

    # Get one and predict
    r = random.randint(0, mnist.test.num_examples - 1)
    print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
    print("Prediction: ", sess.run(
        tf.argmax(Hypothesis, 1), feed_dict={X: mnist.test.images[r:r + 1]}))

    '''
    # don't know why this makes Travis Build error.
    plt.imshow(
    mnist.test.images[r:r + 1].reshape(28, 28),
    cmap='Greys',
    interpolation='nearest')
    plt.show()
    '''