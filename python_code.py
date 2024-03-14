import multiprocessing

def bds_worker(chunk, bds_result_queue):
    bds_parallel_sum = sum(chunk)
    bds_result_queue.put(bds_parallel_sum)

def main():
    bds_large_array = list(range(1, 100001))
    nprocs = multiprocessing.cpu_count()
    bds_chunk_size = len(bds_large_array) // nprocs
    bds_chunks = [bds_large_array[i:i + bds_chunk_size] for i in range(0, len(bds_large_array), bds_chunk_size)]

    bds_result_queue = multiprocessing.Queue()

    bds_processes = []

    for i in range(nprocs):
        process = multiprocessing.Process(target=bds_worker, args=(bds_chunks[i], bds_result_queue))
        bds_processes.append(process)
        process.start()

    for process in bds_processes:
        process.join()

    bds_results = []
    while not bds_result_queue.empty():
        bds_results.append(bds_result_queue.get())
    bds_total_sum = sum(bds_results)
    
    print(f"Total number of chunks {nprocs}")
    print(f"Chunk size per process {bds_chunk_size}")
    for i in range(nprocs):
        print(f"The process {i+1} has chunk sum as {bds_results[i]}")
    print("Total sum of chunks:", bds_total_sum)

if __name__ == "__main__":
    main()
