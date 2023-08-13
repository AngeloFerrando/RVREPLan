(define (domain depot)
(:requirements :strips)
(:predicates
	 (at ?x ?y) (on ?x ?y) (in ?x ?y) (lifting ?x ?y) (available ?x) (clear ?x)(place ?x) (locatable ?x) (depot ?x) (distributor ?x) (truck ?x) (hoist ?x) (surface ?x) (pallet ?x) (crate ?x) )

(:action lift_and_load
	:parameters
	(?x		
?y		
?z		
?p		
?q	)
:precondition
(and (hoist ?x) (crate ?y) (surface ?z) (place ?p) (truck ?q) (at ?q ?p) (at ?x ?p) (available ?x) (at ?y ?p) (on ?y ?z) (clear ?y) )
:effect
(and (available ?x) )
))