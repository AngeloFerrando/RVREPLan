(define (domain depot)
(:requirements :strips)
(:predicates
	 (facing_up ?x) (at ?x ?y) (on ?x ?y) (in ?x ?y) (lifting ?x ?y) (available ?x) (clear ?x)(place ?x) (locatable ?x) (depot ?x) (distributor ?x) (truck ?x) (hoist ?x) (surface ?x) (pallet ?x) (crate ?x) )

(:action unload
	:parameters
	(?x		
?y		
?z		
?p	)
:precondition
(and (hoist ?x) (crate ?y) (truck ?z) (place ?p) (at ?x ?p) (at ?z ?p) (available ?x) (in ?y ?z) )
:effect
(and (not (in ?y ?z)) (lifting ?x ?y) (not (facing_up ?y)) (not (available ?x)) )
))