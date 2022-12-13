from Check_Battery_Condition import *

if __name__ == '__main__':
  assert(battery_is_ok(-1, 50, 0.7) is False)
  assert(battery_is_ok(46, 60, 0.25) is False)
  assert(battery_is_ok(1, 19, 0.4) is False)
  assert(battery_is_ok(28, 81, 0.3) is False)
  assert(battery_is_ok(10, 30, 0.81) is False)
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(40, 90, .9) is False)
  assert(battery_is_ok(70, 45, 1) is False)
  assert(battery_is_ok(100, 100, 2) is False)
  print("All Test Scenarios Covered")
