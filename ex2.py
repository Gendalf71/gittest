import threading
 
total = 30 

def update_total(amount):
    global total
    if total > amount: 
        total -= amount
    print(total)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(target=update_total,
                                     args=(5,))
        my_thread.start()
