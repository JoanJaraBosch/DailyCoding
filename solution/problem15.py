import random

def reservoir_sampling(stream):
    chosen_element = None
    i = 0

    for element in stream:
        i += 1
        # Replace the element with probability 1/i
        if random.randint(1, i) == 1:
            chosen_element = element

    return chosen_element

if __name__ == "__main__":
    # Example Usage:
    stream = [5, 10, 15, 20, 25, 30, 35]
    chosen = reservoir_sampling(stream)
    print(f"Randomly selected element: {chosen}")