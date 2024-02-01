from fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == 0 
    assert fibonacci(2) == 1 
    assert fibonacci(5) == 5 
    assert fibonacci(8) == 21 
    assert fibonacci(11) == 89 
    assert fibonacci(14) == 377
    assert fibonacci(17) == 1597 
    assert fibonacci(20) == 6765
   

