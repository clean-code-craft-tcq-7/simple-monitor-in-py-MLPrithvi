from Check_Battery_Condition import *

if __name__ == '__main__':
  assert(battery_is_ok(-1, 50) is False)
  assert(battery_is_ok(46, 60) is False)
  assert(battery_is_ok(1, 19) is False)
  assert(battery_is_ok(28, 81) is False)
  assert(battery_is_ok(10, 30) is False)
  assert(battery_is_ok(25, 70) is True)
  assert(battery_is_ok(50, 85) is False)
  assert(battery_is_ok(40, 90) is False)
  assert(battery_is_ok(70, 45) is False)
  assert(battery_is_ok(100, 100) is False)
  print("All Test Scenarios Covered")
