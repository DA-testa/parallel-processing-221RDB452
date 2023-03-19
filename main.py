# python3
import heapq

def parallel_processing(n, m, data):
    # Initialize an empty heap with n threads
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    
    # Initialize the output list
    output = []
    
    # Process each job in the input data
    for i in range(m):
        # Get the next job time from the input data
        job_time = data[i]
        
        # Get the thread with the earliest finish time
        thread_time, thread_idx = heapq.heappop(threads)
        
        # Add the output pair for this job and thread
        output.append((thread_idx, thread_time))
        
        # Update the thread's finish time
        finish_time = thread_time + job_time
        heapq.heappush(threads, (finish_time, thread_idx))
    return output

def main():
    # Get input from the user
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    # Run the parallel processing algorithm
    result = parallel_processing(n, m, data)
    
    # Print the output pairs
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if __name__ == "__main__":
    main()

