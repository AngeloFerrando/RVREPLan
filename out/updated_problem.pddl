(define (problem stripssatx1)
(:domain satellite)
(:objects
	satellite0
	instrument0
	satellite1
	instrument1
	instrument2
	instrument3
	satellite2
	instrument4
	thermograph2
	spectrograph0
	infrared1
	infrared3
	groundstation3
	star1
	star2
	star0
	planet4
	planet5
	star6
	star7
	phenomenon8
	star9
	star10
)
(:init
  (not_calibrated instrument2)
  (calibration_target instrument3 star2)
  (direction star10)
  (instrument instrument2)
  (direction phenomenon8)
  (direction star2)
  (direction star7)
  (supports instrument0 infrared1)
  (power_on instrument2)
  (mode spectrograph0)
  (direction planet4)
  (mode thermograph2)
  (direction star9)
  (on_board instrument4 satellite2)
  (instrument instrument3)
  (on_board instrument3 satellite1)
  (power_avail satellite0)
  (pointing satellite0 phenomenon8)
  (instrument instrument0)
  (calibration_target instrument2 star2)
  (direction star6)
  (mode infrared3)
  (satellite satellite0)
  (calibration_target instrument4 star0)
  (supports instrument2 infrared1)
  (on_board instrument1 satellite1)
  (direction star0)
  (instrument instrument1)
  (satellite satellite2)
  (supports instrument1 infrared3)
  (satellite satellite1)
  (direction planet5)
  (orbit satellite2)
  (direction groundstation3)
  (pointing satellite1 star6)
  (supports instrument3 spectrograph0)
  (calibration_target instrument1 star2)
  (supports instrument3 infrared1)
  (not_calibrated instrument4)
  (pointing satellite2 star6)
  (orbit satellite0)
  (direction star1)
  (calibration_target instrument0 star1)
  (supports instrument2 infrared3)
  (orbit satellite1)
  (on_board instrument0 satellite0)
  (supports instrument4 infrared3)
  (supports instrument3 infrared3)
  (supports instrument2 thermograph2)
  (on_board instrument2 satellite1)
  (supports instrument0 spectrograph0)
  (power_on instrument4)
  (not_power_avail satellite1)
  (not_power_avail satellite2)
  (instrument instrument4)
  (mode infrared1)
)
(:goal (and
  (have_image phenomenon8 spectrograph0)
  (have_image planet4 thermograph2)
  (have_image star6 thermograph2)
  (have_image star7 infrared3)
  (have_image star9 infrared1)
  (have_image star10 infrared3)
  (have_image planet5 spectrograph0)
))
)