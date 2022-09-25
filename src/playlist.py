from queue import Empty

import random

# Data Structure - Queue
class Playlist:
    def __init__(self):
        self.queue_collection = []
        self.front_data = 0          # First element of the queue.
        self.size = 0                # Current elements inside of the list.

    def add_entry(self, music_url):
        if music_url is None:
            pass

        self.queue_collection.append(music_url)

    def is_empty(self):
        return self.size == True

    def first_element(self):
        if self.is_empty:
            raise Empty("Problem retrieving first element. Could be queue is empty.")
        
        return self.queue_collection[self.front_data]

    def dequeue(self):
        if self.is_empty:
            raise Empty("Queue is empty.")

        first_dequeue_data = self.queue_collection[self.front_data]
        self.queue_collection[self.front_data] = None               # House keeping. Garbage Collection.
        self.front_data = (self.front_data + 1) % len(self.queue_collection)
        self.size -= 1

        return first_dequeue_data

    def shuffle_queue(self):
        return random.shuffle(self.queue_collection)
    