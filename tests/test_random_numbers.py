from random_numbers.numpy_rng import NumpyRNG
import numpy as np

def test_numpy_rng():
    rng = NumpyRNG(seed=42)
    samples = rng.normal(size=1000)
    
    # Test mean and standard deviation
    assert abs(np.mean(samples)) < 0.1  # Mean should be close to 0
    assert abs(np.std(samples) - 1) < 0.1  # Std should be close to 1

def test_numpy_rng_different_seeds():
    rng1 = NumpyRNG(seed=42)
    rng2 = NumpyRNG(seed=43)
    
    samples1 = rng1.normal(size=1000)
    samples2 = rng2.normal(size=1000)
    
    # The two sets of samples should not be the same
    assert not np.array_equal(samples1, samples2)