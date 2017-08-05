import tensorflow as tf


filename_queue =  tf.train.string_input_producer(
    ['data_score_copy.csv'], shuffle=False, name='filename_queue'
)

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Default values, in case of empty columns, Also specifies the type of the
# decoded result
record_defaults = [[0.], [0.], [0.], [0.]]

xy = tf.decode_csv(value, record_defaults=record_defaults)

#collect batches of csv in
train_x_batch, train_y_batch = \
    tf.train.batch([xy[0:-1], xy[-1:]], batch_size=10)

#x_data = [[1,2], [2,3], [3,1], [4,3], [5,3]]
#y_data = [[0], [0], [0], [1], [1]]

# placeholders for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None,3])
Y = tf.placeholder(tf.float32, shape=[None,1])

W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#Hypothesis using sigmoid: tf.div(1., 1. + tf.exp(tf.matmul(X,W)))
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

#simplified cost/Loss function
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
#minimize
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Accuracy Computation
# True if hypothesis > 0.5 else false
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

#Launch the graph in a session
sess = tf.Session()

#Initializes global variables in the graph
sess.run(tf.global_variables_initializer())

# Start populating the filename queue
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for step in range(10001):
    x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
    hv, cost_val, _ = sess.run([hypothesis, cost, train], feed_dict={X: x_batch, Y: y_batch})
    if step % 1000 == 0:
        print("\nX_train\n",x_batch, "\nY_train\n",y_batch)
        print(step, "Cost: ", cost_val,"\nhypothesis:\n", hv)

#accuracy report
h, c, a = sess.run([hypothesis, predicted, accuracy],
                   feed_dict={X: x_batch, Y: y_batch})

print("\nHypothesis: ", h, "\nCorrect (Y): \n", c, "\nAccuracy: ", a)

coord.request_stop()
coord.join(threads)

