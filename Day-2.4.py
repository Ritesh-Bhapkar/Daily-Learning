import threading
import time

semaphore = threading.Semaphore(2)

def worker(name):
    print(f"{name} waiting")

    with semaphore:
        print(f"{name} entered")
        time.sleep(3)
        print(f"{name} leaving")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All done")





