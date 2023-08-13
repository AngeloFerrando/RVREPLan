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
  (instrument instrument3)
  (supports instrument1 infrared3)
  (on_board instrument4 satellite2)
  (satellite satellite2)
  (pointing satellite2 star10)
  (calibration_target instrument3 star2)
  (direction planet5)
  (satellite satellite0)
  (satellite satellite1)
  (on_board instrument2 satellite1)
  (direction planet4)
  (supports instrument0 spectrograph0)
  (pointing satellite1 star6)
  (supports instrument2 infrared1)
  (instrument instrument4)
  (instrument instrument1)
  (instrument instrument2)
  (calibration_target instrument0 star1)
  (mode thermograph2)
  (direction star7)
  (power_on instrument2)
  (power_on instrument0)
  (calibration_target instrument2 star2)
  (mode infrared3)
  (direction star1)
  (direction star6)
  (direction phenomenon8)
  (not_power_avail satellite1)
  (on_board instrument3 satellite1)
  (power_on instrument4)
  (supports instrument3 infrared3)
  (direction star0)
  (calibration_target instrument1 star2)
  (direction star9)
  (mode spectrograph0)
  (direction star2)
  (not_power_avail satellite0)
  (supports instrument0 infrared1)
  (not_power_avail satellite2)
  (pointing satellite0 phenomenon8)
  (orbit satellite0)
  (orbit satellite1)
  (direction star10)
  (have_image star6 thermograph2)
  (calibrated instrument2)
  (calibration_target instrument4 star0)
  (not_calibrated instrument4)
  (on_board instrument1 satellite1)
  (supports instrument3 infrared1)
  (calibrated instrument0)
  (supports instrument3 spectrograph0)
  (mode infrared1)
  (direction groundstation3)
  (instrument instrument0)
  (supports instrument2 thermograph2)
  (supports instrument4 infrared3)
  (not_orbit satellite2)
  (not_pointing satellite2 star6)
  (on_board instrument0 satellite0)
  (have_image phenomenon8 spectrograph0)
  (supports instrument2 infrared3)
)
(:goal (and
  (have_image star9 infrared1)
  (have_image planet4 thermograph2)
  (have_image star10 infrared3)
  (have_image star7 infrared3)
  (have_image planet5 spectrograph0)
))
)