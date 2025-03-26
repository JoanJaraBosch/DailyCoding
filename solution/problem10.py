import threading

def job_scheduler(f, n):
    timer = threading.Timer(n / 1000, f)  # Convert milliseconds to seconds
    timer.start()

# Example Usage:
def my_function():
    print("Function executed!")

if __name__ == "__main__":
    job_scheduler(my_function, 2000)  # Calls my_function after 2 seconds