from threading import Thread
import threading


def print_numbers():
    for n in range(1, 26):
        print(f'Another Child {n}')


class ChildThread(Thread):
    def run(self):
        for n in range(1, 26):
            print(f'Child {n}')


print(threading.current_thread())
ct = ChildThread()
ct.start()

ct2 = Thread(target=print_numbers)
ct2.start()

print(f'Count = {threading.active_count()}')

for n in range(1, 26):
    print(f'Main {n}')

print("Waiting for child threads to stop")
ct2.join()  # Wait for ct2 to terminate
ct.join()   # wait for ct to terminate
print("The End!")
