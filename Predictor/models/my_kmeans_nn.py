import tensorflow as tf
import numpy as np


class My_kmeans_nn():
    def __init__(self, n_clusters, iteration_n):
        self.n_clusters = n_clusters
        self.iteration_n = iteration_n
        self.centroids = None
        self.labels_ = None

    def fit(self, X):
        points = tf.constant(X)
        centroids = tf.constant(tf.slice(tf.compat.v1.random_shuffle(points), [0, 0], [self.n_clusters, -1]))
        # st()
        points_expanded = tf.expand_dims(points, 0)

        @tf.function
        def update_centroids(points_expanded, centroids):
            centroids_expanded = tf.expand_dims(centroids, 1)

            distances = tf.reduce_sum(tf.square(tf.subtract(points_expanded, centroids_expanded)), 2)
            assignments = tf.argmin(distances, 0)
            means = []
            for c in range(self.n_clusters):
                ruc = tf.reshape(tf.where(tf.equal(assignments, c)), [1,-1])
                ruc = tf.gather(points, ruc)
                ruc = tf.reduce_mean(ruc, axis=[1])
                means.append(ruc)
                new_centroids = tf.concat(means, 0)
                # st()
            return new_centroids, assignments

        for _ in range(self.iteration_n):
            self.centroids, self.labels_ = update_centroids(points_expanded, centroids)

    def predict(self, row):
        row = tf.constant(row)
        distances = []
        for c in self.centroids:
            distances.append(tf.math.reduce_sum((c-row)**2, axis=-1).numpy())
        # st()
        return distances.index(min(distances))
