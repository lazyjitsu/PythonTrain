import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

# target = $functionYouWantToRun
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)
if __name__ == "__main__":
    p1.start()
    p2.start()
    # make sure p1 & p2 finish before going to the print statement below else i think it runs async and u print finished before u started!
    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finsihed in {round(finish-start, 2)} second(s)')