"""
Problems:
Airport with a runway system
- Reservation for future landing
- Reserve request specifies landing time t
- Add t to a set R if no other landings are scheduled within k minutes
- What landed before t?

Ideas:
- What landed before t?
    - Walk down tree to find desired time
    - Add in 1 for the nodes that are smaller
    - Add in the sub-tree size to the left of just compared node
"""