def raiseleftarm():
  i01.startedGesture()
  i01.moveArm("left",53.00,57.00,37.00,31.00)
  i01.moveArm("right",5.00,90.00,30.00,12.00)
  i01.moveHand("left",0.00,0.00,0.00,0.00,0.00,11.00)
  i01.moveHand("right",0.00,0.00,0.00,0.00,0.00,90.00)
  i01.moveTorso(90.00,90.00,90.00)
  sleep(5)
  i01.finishedGesture()
  relax()
