from babysitter import *

def test_hours_worked():
    start_time = 17 
    end_time = 18
    assert hours_worked(start_time,end_time) == 1

def test_start_time():
    #tests start time before 5 should change 16 to 17
    start_time = 16 
    end_time = 18
    assert hours_worked(start_time,end_time) == 1

def test_end_time():
    start_time = 23 
    end_time = 0
    assert hours_worked(start_time,end_time) == 1

 
