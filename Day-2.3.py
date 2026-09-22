import threading

balance = 0
lock = threading.Lock()

def add_money():
    global balance

    for _ in range(100000):
        with lock:
            balance += 1

t1 = threading.Thread(target=add_money)
t2 = threading.Thread(target=add_money)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance:", balance)