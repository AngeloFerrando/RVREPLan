(define (domain remote-inspection)
(:requirements :typing)
(:types robot cell tank - object)

(:predicates
	(robot_at ?r - robot ?x - cell)
	(tank_at ?t - tank ?x - cell)
	(up ?x - cell ?y - cell)
	(down ?x - cell ?y - cell)
	(right ?x - cell ?y - cell)
	(left ?x - cell ?y - cell)
	(empty ?x - cell)
	(inspected ?t - tank)
	(radiation ?x - cell)
)

; Robot movements
(:action act_up
  :parameters (?r - robot ?x - cell ?y - cell)
  :precondition (and (robot_at ?r ?x) (up ?x ?y) (empty ?y) (not (radiation ?y)))
  :effect (and (robot_at ?r ?y) (not (robot_at ?r ?x))
               (empty ?x) (not (empty ?y))
            )
)

(:action act_down
  :parameters (?r - robot ?x - cell ?y - cell)
  :precondition (and (robot_at ?r ?x) (down ?x ?y) (empty ?y) (not (radiation ?y)))
  :effect (and (robot_at ?r ?y) (not (robot_at ?r ?x))
               (empty ?x) (not (empty ?y))
            )
)

(:action act_right
  :parameters (?r - robot ?x - cell ?y - cell)
  :precondition (and (robot_at ?r ?x) (right ?x ?y) (empty ?y) (not (radiation ?y)))
  :effect (and (robot_at ?r ?y) (not (robot_at ?r ?x))
               (empty ?x) (not (empty ?y))
	     )
)

(:action act_left
  :parameters (?r - robot ?x - cell ?y - cell)
  :precondition (and (robot_at ?r ?x) (left ?x ?y) (empty ?y) (not (radiation ?y)))
  :effect (and (robot_at ?r ?y) (not (robot_at ?r ?x))
               (empty ?x) (not (empty ?y))
            )
)

(:action act_inspect_up
  :parameters (?r - robot ?x - cell ?y - cell ?t - tank)
  :precondition (and (robot_at ?r ?x) (tank_at ?t ?y) (up ?x ?y) (not (inspected ?t)))
  :effect (and (inspected ?t)
            )
)

(:action act_inspect_down
  :parameters (?r - robot ?x - cell ?y - cell ?t - tank)
  :precondition (and (robot_at ?r ?x) (tank_at ?t ?y) (down ?x ?y) (not (inspected ?t)))
  :effect (and (inspected ?t)
            )
)

(:action act_inspect_right
  :parameters (?r - robot ?x - cell ?y - cell ?t - tank)
  :precondition (and (robot_at ?r ?x) (tank_at ?t ?y) (right ?x ?y) (not (inspected ?t)))
  :effect (and (inspected ?t)
            )
)

(:action act_inspect_left
  :parameters (?r - robot ?x - cell ?y - cell ?t - tank)
  :precondition (and (robot_at ?r ?x) (tank_at ?t ?y) (left ?x ?y) (not (inspected ?t)))
  :effect (and (inspected ?t)
            )
)

)
