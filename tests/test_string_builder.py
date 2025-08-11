from lib.string_builder import *

def test_if_str_init(): 
    my_str = StringBuilder()
    assert my_str.str == ""

def test_if_str_adds():
    my_str = StringBuilder()
    my_str.add("hello")
    assert my_str.str == "hello"
 

def test_if_str_size_correct():
    my_str = StringBuilder()
    my_str.add("hello")
    assert my_str.size() == 5


def test_if_str_reports_correctly(): 
    my_str = StringBuilder()
    my_str.add("hello")
    assert my_str.output() == "hello"



def test_if_str_reports_correctly_multi_words(): 
    my_str = StringBuilder()
    my_str.add("hello")
    my_str.add("bye")
    assert my_str.output() == "hellobye"


