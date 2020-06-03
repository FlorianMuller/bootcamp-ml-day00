import numpy as np


def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    if x.size == 0 or x.ndim != 1 or theta.size != 2 or theta.ndim != 1:
        return None
    return theta[0] + (theta[1] * x)


if __name__ == "__main__":
    x = np.arange(1, 6)

    # Example 1:
    theta1 = np.array([5, 0])
    print(simple_predict(x, theta1))
    # Ouput:
    # array([5., 5., 5., 5., 5.])
    # Do you understand why y_hat contains only 5's here

    # Example 2:
    theta2 = np.array([0, 1])
    print(simple_predict(x, theta2))
    # Output:
    # array([1., 2., 3., 4., 5.])
    # Do you understand why y_hat == x here?

    # Example 3:
    theta3 = np.array([5, 3])
    print(simple_predict(x, theta3))
    # Output:
    # array([ 8., 11., 14., 17., 20.])

    # Example 4:
    theta4 = np.array([-3, 1])
    print(simple_predict(x, theta4))
    # Output:
    # array([-2., -1., 0., 1., 2.])

    # Empty array
    print(simple_predict(x, np.array([])))
    print(simple_predict(np.array([]), theta4))

    # Bad dimension
    print(simple_predict(x, np.array([[1, 1], [2, 2]])))
    print(simple_predict(np.array([[1, 1], [2, 2]]), theta4))
