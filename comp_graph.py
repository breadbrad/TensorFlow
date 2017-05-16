import tensorflow as tf
hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()
print(sess.run(hello))

node1 = tf.constant(3.0, tf.float32) 
node2 = tf.constant(4.0) # implicit
node3 = tf.add(node1, node2)
print("node3: " , node3) # doesn't work 
#A session allows to execute graphs
sess = tf.Session()
print("sess.run(node3): ", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, feed_dict={a: [1,2], b: [3,4]}))
