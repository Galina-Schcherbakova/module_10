import time
import multiprocessing
import os


def read_info(name):
    all_data = []
    try:
        with open(name, 'r') as f:
            line = f.readline()
            while line:
                all_data.append(line)
                line = f.readline()
    except FileNotFoundError:
        print(f"Файл {name} не найден.")
    return len(all_data)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    for filename in filenames:
        with open(filename, 'w') as f:
            for _ in range(1000000):
                f.write("This is a line.\n")

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(time.strftime("%H:%M:%S", time.gmtime(end_time - start_time)), "(линейный)")

    # Многопроцессный вызов (раскомментировать, закомментировав линейный)
    # start_time = time.time()
    # with multiprocessing.Pool(processes=4) as pool:
    #    results = pool.map(read_info, filenames)
    # end_time = time.time()
    # print(time.strftime("%H:%M:%S", time.gmtime(end_time - start_time)), "(многопроцессный)")

    for filename in filenames:
        os.remove(filename)
