(define (domain satellite)
(:requirements :strips)
(:predicates
	 (on_board ?i ?s) (supports ?i ?m) (pointing ?s ?d) (power_avail ?s) (power_on ?i) (calibrated ?i) (have_image ?d ?m) (calibration_target ?i ?d)(satellite ?x) (direction ?x) (instrument ?x) (mode ?x) )

(:action calibrate_and_take_image
	:parameters
	(?s		
?d		
?i		
?m	)
:precondition
(and (satellite ?s) (direction ?d) (instrument ?i) (mode ?m) (on_board ?i ?s) (supports ?i ?m) (power_on ?i) (pointing ?s ?d) )
:effect
(and )
))