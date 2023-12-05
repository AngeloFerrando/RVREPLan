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
(and (not (at ?obj ?loc)) (in ?obj ?airplane) (not (balanced ?airplane)) )
)
(:action call_human
	:parameters
	(?human		
?truck		
?loc	)
:precondition
(and (human ?human) (truck ?truck) (location ?loc) (at ?human ?loc) (at ?truck ?loc) )
:effect
(and (not (at ?human ?loc)) (at ?human ?truck) )
)
(:action load_truck_human
	:parameters
	(?human		
?obj		
?truck		
?loc	)
:precondition
(and (package ?obj) (truck ?truck) (location ?loc) (at ?truck ?loc) (at ?obj ?loc) (human ?human) (at ?human ?truck) )
:effect
(and (not (at ?obj ?loc)) (in ?obj ?truck) (not (at ?human ?truck)) (at ?human ?loc) )
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
)
(:action unload_truck
	:parameters
	(?obj		
?truck		
?loc	)
:precondition
(and (package ?obj) (truck ?truck) (location ?loc) (at ?truck ?loc) (in ?obj ?truck) )
:effect
(and (not (in ?obj ?truck)) (at ?obj ?loc) )
)
(:action unload_truck_human
	:parameters
	(?human		
?obj		
?truck		
?loc	)
:precondition
(and (package ?obj) (truck ?truck) (location ?loc) (at ?truck ?loc) (in ?obj ?truck) (human ?human) (at ?human ?truck) )
:effect
(and (not (in ?obj ?truck)) (at ?obj ?loc) (not (at ?human ?truck)) (at ?human ?loc) )
)
(:action unload_airplane
	:parameters
	(?obj		
?airplane		
?loc	)
:precondition
(and (package ?obj) (airplane ?airplane) (location ?loc) (in ?obj ?airplane) (at ?airplane ?loc) )
:effect
(and (not (in ?obj ?airplane)) (at ?obj ?loc) )
)
(:action drive_truck
	:parameters
	(?truck		
?loc_from		
?loc_to		
?city	)
:precondition
(and (truck ?truck) (location ?loc_from) (location ?loc_to) (city ?city) (at ?truck ?loc_from) (in_city ?loc_from ?city) (in_city ?loc_to ?city) )
:effect
(and (not (at ?truck ?loc_from)) (at ?truck ?loc_to) )
)
(:action fly_airplane
	:parameters
	(?airplane		
?loc_from		
?loc_to	)
:precondition
(and (airplane ?airplane) (airport ?loc_from) (airport ?loc_to) (at ?airplane ?loc_from) (balanced ?airplane) )
:effect
(and (not (at ?airplane ?loc_from)) (at ?airplane ?loc_to) )
)
(:action balance_airplane
	:parameters
	(?airplane	)
:precondition
(and (airplane ?airplane) )
:effect
(and (balanced ?airplane) )
))