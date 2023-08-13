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
  (balanced ?airplane)
)


(:action load_airplane
	:parameters
	(?obj		
?airplane		
?loc	)
:precondition
(and (package ?obj) (airplane ?airplane) (location ?loc) (at ?obj ?loc) (at ?airplane ?loc) )
:effect
(and (in ?obj ?airplane) (not (balanced ?airplane)) (not (at ?obj ?loc)) )
))