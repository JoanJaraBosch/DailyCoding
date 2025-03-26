import random

def estimate_pi(num_samples):
    inside_circle = 0  # Counter for points inside the circle

    for _ in range(num_samples):
        # Generate random point (x, y) where x, y are between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    # Estimate pi using the formula: pi ≈ 4 * (points_inside_circle / total_points)
    return 4 * inside_circle / num_samples

if __name__ == "__main__":
    # Example Usage:
    num_samples = 1000000  # Number of random points to sample
    estimated_pi = estimate_pi(num_samples)
    print(f"Estimated pi number: {estimated_pi:.3f}")