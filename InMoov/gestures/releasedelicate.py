def releasedelicate():
  i01.startedGesture()
  i01.setHandSpeed("left", 0.60, 0.60, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 0.75, 0.75, 0.75, 0.95)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(20,98)
  i01.moveArm("left",30,72,64,10)
  i01.moveArm("right",0,91,28,17)
  i01.moveHand("left",101,74,66,58,44,180)
  i01.moveHand("right",86,51,133,162,153,180)
  i01.setHeadSpeed(1.0,1.0,1.0,1.0,1.0)
  sleep(1)
  i01.finishedGesture()

