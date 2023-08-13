(define (domain logistics)
(:requirements :strips) 
 
(:predicates 	
  (package ?obj)
  (truck ?truck)
  (airplane ?airplane)
  (airport ?airport)
  (location ?loc)
  (in_city ?obj ?city)
  (city ?city)
  (at ?obj ?loc)
  (in ?obj ?obj)
  (human ?human)
)


(:action load_truck
	:parameters
	(?obj		
?truck		
?loc	)
:precondition
(and (package ?obj) (truck ?truck) (location ?loc) (at ?truck ?loc) (at ?obj ?loc) )
:effect
(and )
))