def count(vector):
    """
    Count the number of elements in a vector.

    Parameters
    ----------
    vector : iterable
        A sequence of elements to count.

    Returns
    -------
    int
        The total number of elements in the vector.

    Notes
    -----
    Time complexity: O(n), where n is the number of elements in `vector`.

    Equation
    --------
    count = n
    """
    total = 0
    for _ in vector:
        total += 1
    return total

def sum(vector):
    """
    Compute the sum of all elements in a vector.

    Parameters
    ----------
    vector : iterable of numbers
        A sequence of numeric values.

    Returns
    -------
    float or int
        The sum of all elements in the vector.

    Notes
    -----
    Time complexity: O(n), where n is the number of elements in `vector`.

    Equation
    --------
    sum = x₁ + x₂ + ... + xₙ
    """
    total = 0
    for num in vector:
        total += num
    return total

def mean(vector):
    """
    Compute the arithmetic mean of a vector.

    Parameters
    ----------
    vector : iterable of numbers
        A sequence of numeric values.

    Returns
    -------
    float
        The mean (average) of the vector elements.

    Notes
    -----
    Time complexity: O(n), due to separate passes for sum and count.

    Equation
    --------
    mean = (x₁ + x₂ + ... + xₙ) / n
    """
    vector_sum = sum(vector)
    vector_count = count(vector)
    return vector_sum / vector_count

def standard_deviation(vector):
    """
    Compute the standard deviation of a vector.

    Parameters
    ----------
    vector : iterable of numbers
        A sequence of numeric values.

    Returns
    -------
    float
        The standard deviation of the vector elements.

    Notes
    -----
    Time complexity: O(n), where n is the number of elements in `vector`.

    Equation
    --------
    σ = sqrt( (1/n) * Σ(xᵢ - μ)² )
    where μ is the mean of the vector
    """
    vector_mean = mean(vector)
    squared_diffs = []
    for num in vector:
        diff = num - vector_mean
        squared_diff = diff ** 2
        squared_diffs.append(squared_diff)
    variance = mean(squared_diffs)
    return variance ** 0.5

def interval(standard_dev, mean_value, num_std_dev):
    """
    Calculate the interval around the mean for a given number of standard deviations.

    Parameters
    ----------
    standard_dev : float
        The standard deviation of the data.
    mean_value : float
        The mean of the data.
    num_std_dev : int
        The number of standard deviations to calculate the interval for.

    Returns
    -------
    tuple
        A tuple containing the lower and upper bounds of the interval.

    Notes
    -----
    Time complexity: O(1), as it involves basic arithmetic operations.

    Equation
    --------
    interval = (mean - num_std_dev * standard_dev, mean + num_std_dev * standard_dev)
    """
    lower_bound = mean_value - (num_std_dev * standard_dev)
    upper_bound = mean_value + (num_std_dev * standard_dev)
    return (lower_bound, upper_bound)

def analysis(standard_dev, mean_value):
    """
    Display the empirical rule intervals for a normal distribution.

    This block calculates and prints the ranges within which approximately 68%, 95%, and 99.7% 
    of data samples are expected to fall, assuming a normal distribution. It uses the mean and 
    standard deviation to compute intervals at 1, 2, and 3 standard deviations from the mean.

    Variables
    ---------
    standard_dev : float
        The standard deviation of the dataset.
    mean_value : float
        The mean of the dataset.

    Notes
    -----
    This applies the empirical rule:
    - 68% of data falls within ±1σ
    - 95% of data falls within ±2σ
    - 99.7% of data falls within ±3σ

    Output is rounded to one decimal place for readability.
    """
    
    standard_dev_1 = interval(standard_dev, mean_value, 1)
    standard_dev_2 = interval(standard_dev, mean_value, 2) 
    standard_dev_3 = interval(standard_dev, mean_value, 3)
    
    print(f"An estimated 68% of new data samples will fall between {round(standard_dev_1[0], 1)} and {round(standard_dev_1[1], 1)}")
    print(f"An estimated 95% of new data samples will fall between {round(standard_dev_2[0], 1)} and {round(standard_dev_2[1], 1)}")
    print(f"An estimated 99.7% of new data samples will fall between {round(standard_dev_3[0], 1)} and {round(standard_dev_3[1], 1)}")

def main():
    sample = [172, 178, 181, 169, 175, 183, 170, 177, 174, 180, 165, 179, 182, 176, 171, 173, 168, 185, 166, 184, 190, 167, 172, 175, 178, 169, 181, 174, 177, 173, 186, 170, 176, 179, 172, 171, 188, 167, 180, 185, 169, 174, 177, 182, 168, 183, 175, 170, 178, 176]

    # Display summary statistics
    print("\n--- Sample Statistics ---")
    print(f"Data (First 10 Samples): {sample[0:10]}")
    print(f"Count: {count(sample)}")
    print(f"Sum: {sum(sample)}")
    print(f"Mean: {mean(sample):.1f}")
    print(f"Standard Deviation: {standard_deviation(sample):.1f}")

    # Perform analysis
    print("\n--- Analysis ---")
    analysis(standard_deviation(sample), mean(sample))
    print()
    
if __name__ == "__main__":
    main()