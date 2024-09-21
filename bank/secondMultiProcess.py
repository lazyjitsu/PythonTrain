import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

processes = []
# the '_' means were not using the integer..it's a throw away variable
for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    #p.join()  we don't want to do join here, the 2nd p.start() wouldn't start and we're back to running it synchronously
    processes.append(p)  
    # so let load an array of processes and join themm after 

for process in processes:
    process.join()  
    # so this will make sure all processes 'join' aka ensuring they finish before going to next line of code!!!


finish = time.perf_counter()

    if __name__ == "__main__":

    print(f'Finsihed in {round(finish-start, 2)} second(s)')