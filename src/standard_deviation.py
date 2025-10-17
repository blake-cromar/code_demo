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

def main():
    pass