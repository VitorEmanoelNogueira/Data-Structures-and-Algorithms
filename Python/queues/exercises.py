import threading
import time

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.buffer[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    

# 1. Design a food ordering system where your python program will run two threads,
    # Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
    # Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print(f"Placing order for: {order}")
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        if order is not None:
            print(f"Now serving: {order}")
            time.sleep(2)
        else:
            break


# 2. Write a program to print binary numbers from 1 to 10 using Queue.
def binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for _ in range(n):
        front = numbers_queue.peek()
        print(front)
        numbers_queue.enqueue(f"{front}0")
        numbers_queue.enqueue(f"{front}1")

        numbers_queue.dequeue()



if __name__ == "__main__":
    # Exercise 1:
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders, ))
    t2 = threading.Thread(target=serve_orders)

    print("--------------------Exercise 1--------------------")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    # Exercise 2:
    print("--------------------Exercise 2--------------------")
    binary_numbers(10)