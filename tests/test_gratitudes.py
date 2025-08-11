from lib.gratitudes import *

def test_if_gratitudes_init():
    my_grat = Gratitudes()
    assert my_grat.gratitudes == []

def test_if_gratitudes_add(): 
    my_grat = Gratitudes()
    my_grat.add("health")
    assert my_grat.gratitudes == ["health"]
    
def test_if_gratitude_formats_multiple(): 
    my_grat = Gratitudes()
    my_grat.add("health")
    my_grat.add("family")
    assert my_grat.format() == "Be grateful for: health, family"
    