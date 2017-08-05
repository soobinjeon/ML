import tensorflow as tf

ax = [[0,0,1],
      [0,0,1],
      [0,0,1]]

rm = tf.reduce_sum(ax)
rm1 = tf.reduce_sum(ax,axis=0)
rm2 = tf.reduce_sum(ax,axis=1)

sess = tf.Session()
print("\n axis \n", ax)
print("\n axis \n", sess.run(rm))
print("\n axis \n", sess.run(rm1))
print("\n axis \n", sess.run(rm2))

ax = [[[0,0,1],[0,0,1],[0,0,1]],
      [[0,1,0],[0,1,0],[0,1,0]]]

rm = tf.reduce_sum(ax)
rm1 = tf.reduce_sum(ax,axis=0)
rm2 = tf.reduce_sum(ax,axis=1)
rm3 = tf.reduce_sum(ax,axis=2)

sess = tf.Session()
print("\n axis \n", ax)
print("\n axis \n", sess.run(rm))
print("\n axis \n", sess.run(rm1))
print("\n axis \n", sess.run(rm2))
print("\n axis \n", sess.run(rm3))