from lib.counter import * 

def test_if_count_initialised(): 
    my_counter = Counter() 
    assert my_counter.count == 0

def test_if_add_works(): 
    my_counter = Counter()
    my_counter.add(5)
    assert my_counter.count == 5


def test_if_report_works(): 
    my_counter = Counter()
    my_counter.add(5)
    assert my_counter.report() == "Counted to 5 so far."
