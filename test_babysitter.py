from babysitter import *
import pytest

def test_hours_worked():
    start_time = 17 
    end_time = 18
    assert calc_hours_worked(start_time,end_time) == 1

def test_start_time():
    #tests start time before 5 should change 16 to 17
    start_time = 16 
    end_time = 18
    assert calc_hours_worked(start_time,end_time) == 1

def test_end_time():
    start_time = 23 
    end_time = 0
    assert calc_hours_worked(start_time,end_time) == 1
    

def test_exception_if_end_time_is_before_start_time():
    with pytest.raises(Exception) as err:
        start_time = 18
        end_time = 17
        calc_hours_worked(start_time,end_time)
    err.match("Shift end time is before the start time")

def test_start_time_before_midnight_end_time_after_midnight():
    start_time = 22
    end_time = 1
    assert calc_hours_worked(start_time,end_time) == 3


