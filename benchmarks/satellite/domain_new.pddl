(define (domain satellite)
(:requirements :strips)
(:predicates
	 (orbit ?s) (on_board ?i ?s) (supports ?i ?m) (pointing ?s ?d) (power_avail ?s) (power_on ?i) (calibrated ?i) (have_image ?d ?m) (calibration_target ?i ?d)(satellite ?x) (direction ?x) (instrument ?x) (mode ?x) )

(:action turn_to
	:parameters
	(?s		
?d_new		
?d_prev	)
:precondition
(and (satellite ?s) (direction ?d_new) (direction ?d_prev) (pointing ?s ?d_prev) )
:effect
(and (not (pointing ?s ?d_prev)) (not (orbit ?s)) (pointing ?s ?d_new) )
))