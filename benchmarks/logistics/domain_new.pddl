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
)

 

(:action unload_truck
	:parameters
	(?obj		
?truck		
?loc	)
:precondition
(and (at ?truck ?loc) (package ?obj) (truck ?truck) (location ?loc) )
:effect
(and 
)
(:action load_truck
	:parameters
	(?obj		
?truck		
?loc	)
:precondition
(and 
:effect
(and ((not (in ?obj ?truck)) (in ?obj ?truck) ((not (at ?obj ?loc)) )
))