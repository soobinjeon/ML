import tensorflow as tf
import numpy as np

# Predicting animal type based on various features
xy = np.loadtxt('0_data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[0:80, 0:-1]
y_data = xy[0:80, [-1]]

x_test = xy[81:101, 0:-1]
y_test = xy[81:101, [-1]]

print(x_data.shape, y_data.shape)
print(x_test.shape, y_test.shape)


nb_classes = 7  # 0 ~ 6

X = tf.placeholder(tf.float32, [None, 16])
Y = tf.placeholder(tf.int32, [None, 1])  # 0 ~ 6

Y_one_hot = tf.one_hot(Y, nb_classes)  # one hot
print("one_hot", Y_one_hot)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])
print("reshape", Y_one_hot)


W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

#tf.nn.softmax computes softmax activations
# softmax = exp(Logits) / reduce_sum(exp(Logits), dim)
logit = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logit)

#Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logit, labels=Y_one_hot)
l2reg = 0.001 * tf.reduce_mean(tf.square(W))
cost = tf.reduce_mean(cost_i) + l2reg
optimize = tf.train.GradientDescentOptimizer(learning_rate=0.2).minimize(cost)

prediction = tf.arg_max(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.arg_max(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#Launch
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range (2000):
        feeds = {X: x_data, Y: y_data}
        sess.run(optimize, feed_dict=feeds)
        if step % 100 == 0:
            loss, acc = sess.run([cost, accuracy], feed_dict=feeds)
            print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(step, loss, acc))

    #Let's see if we can predict
    pred = sess.run(prediction, feed_dict={X: x_test})
    #Y_data: (N,1) = flatten => (N, ) matches pred.shape
    for p, y in zip(pred, y_test.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))
    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: x_test, Y: y_test}))