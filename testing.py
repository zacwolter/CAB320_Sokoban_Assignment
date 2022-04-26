"""
THIS FILE IS PURELY FOR TESTING PURPOSES ONLY

Author: Zac :)
"""

import operator

weights = None
box_locs = [(3,6), (4,7)]
worker_loc = (4,6)
wall_locs = [(1,6), (1,5), (1,7), (1,8), (2,8), (3,8), (4,8), (5,8), (5,7), (5,6), (5,5), (4,5), (3,5)]
targets = [(4, 2), (4, 4)]

# box_above = [(x,y) for (x,y) in box_locs if x == worker_loc[0] - 1 if worker_loc[1] == y]
# print(box_above)
# blocking_box = [(x,y) for (x,y) in box_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
# print(blocking_box)
# blocking_wall = [(x,y) for (x,y) in wall_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
# print(blocking_wall)
# box_below = [(x,y) for (x,y) in box_locs if x == worker_loc[0] + 1 if worker_loc[1] == y]
# print(box_below)

# Next check where the worker can move and append it to the list of possible actions
legal_moves = []    # list of legal actions

# UP: Check if there is a wall or a box in the space above the worker
box_above = [(x,y) for (x,y) in box_locs if x == worker_loc[0] - 1 if worker_loc[1] == y]
walls_above = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] - 1 if worker_loc[1] == y]
if len(box_above) > 0:
    # There is a box above the worker, need to check if there are any box/walls above the box
    blocking_box_above = [(x,y) for (x,y) in box_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
    blocking_wall_above = [(x,y) for (x,y) in wall_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
    # If there is no blocking box or wall in the space above, append "UP" as a legal move 
    # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
    if len(blocking_box_above) == 0 and len(blocking_wall_above) == 0:
        legal_moves.append("UP")
elif len(walls_above) > 0:
    # There is a wall above the worker, therefore we cannot move up
    pass
else:
    # There is no wall or box above the player (WILL NEED TO CHECK FOR TABOO SPACES)
    legal_moves.append("UP")

# DOWN: Check if there is a wall or a box in the space below the worker
box_below = [(x,y) for (x,y) in box_locs if x == worker_loc[0] + 1 if worker_loc[1] == y]
walls_below = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] + 1 if worker_loc[1] == y]
if len(box_below) > 0:
    # There is a box below the worker, need to check if there are any box/walls below the box
    blocking_box_below = [(x,y) for (x,y) in box_locs if x == box_below[0][0] + 1 if box_below[0][1] == y]
    blocking_wall_below = [(x,y) for (x,y) in wall_locs if x == box_below[0][0] + 1 if box_below[0][1] == y]
    # If there is no blocking box or wall in the space below, append "DOWN" as a legal move 
    # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
    if len(blocking_box_below) == 0 and len(blocking_wall_below) == 0:
        legal_moves.append("DOWN")
elif len(walls_below) > 0:
    # There is a wall below the worker, therefore we cannot move up
    pass
else:
    # There is no wall or box below the player (WILL NEED TO CHECK FOR TABOO SPACES)
    legal_moves.append("DOWN")

# LEFT: Check if there is a wall or a box in the space to the left of the worker
box_left = [(x,y) for (x,y) in box_locs if x == worker_loc[0] if worker_loc[1] - 1 == y]
walls_left = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] if worker_loc[1] - 1 == y]
if len(box_left) > 0:
    # There is a box to the left of the worker, need to check if there are any box/walls to the left of the box
    blocking_box_left = [(x,y) for (x,y) in box_locs if x == box_left[0][0] if box_left[0][1] - 1 == y]
    blocking_wall_left = [(x,y) for (x,y) in wall_locs if x == box_left[0][0] if box_left[0][1] - 1 == y]
    # If there is no blocking box or wall in the space to the left, append "LEFT" as a legal move 
    # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
    if len(blocking_box_left) == 0 and len(blocking_wall_left) == 0:
        legal_moves.append("LEFT")
elif len(walls_left) > 0:
    # There is a wall below the worker, therefore we cannot move up
    pass
else:
    # There is no wall or box below the player (WILL NEED TO CHECK FOR TABOO SPACES)
    legal_moves.append("LEFT")

# RIGHT: Check if there is a wall or a box in the space to the right of the worker
box_right = [(x,y) for (x,y) in box_locs if x == worker_loc[0] if worker_loc[1] + 1 == y]
walls_right = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] if worker_loc[1] + 1 == y]
if len(box_right) > 0:
    # There is a box to the right of the worker, need to check if there are any box/walls to the right of the box
    blocking_box_right = [(x,y) for (x,y) in box_locs if x == box_right[0][0] if box_right[0][1] + 1 == y]
    blocking_wall_right = [(x,y) for (x,y) in wall_locs if x == box_right[0][0] if box_right[0][1] + 1 == y]
    # If there is no blocking box or wall in the space to the right, append "RIGHT" as a legal move 
    # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
    if len(blocking_box_right) == 0 and len(blocking_wall_right) == 0:
        legal_moves.append("RIGHT")
elif len(walls_right) > 0:
    # There is a wall below the worker, therefore we cannot move up
    pass
else:
    # There is no wall or box below the player (WILL NEED TO CHECK FOR TABOO SPACES)
    legal_moves.append("RIGHT")

# print(legal_moves)

# print(box_locs)
# box_up_index = box_locs.index(box_above[0])
# print(box_up_index)
# box_locs[box_up_index] = (box_above[0][0] + 1, box_above[0][1])
# print(box_locs)
# print(worker_loc)
# worker_loc = (worker_loc[0] + 1, worker_loc[1])
# print(worker_loc)

total = 0
worker_dist_to_boxes = []
for (x,y) in box_locs:
    worker_dist_to_boxes.append((abs(x - worker_loc[0]), abs(y - worker_loc[1])))
closest_box_to_worker = min(worker_dist_to_boxes)
total += (closest_box_to_worker[0] + closest_box_to_worker[1])
print(total)

# # Need to use index() to select each box in descending order
weights_tracker = weights.copy()
unclaimed_targets = targets.copy()
for i in range(len(weights)):
    highest_weight = 0
    # Find current highest weight
    for weight in weights_tracker:
        if weight > highest_weight:
            highest_weight = weight
    # Get index of highest weight
    highest_weight_index = weights.index(highest_weight)
    # Remove weight from weights_tracker
    weights_tracker.remove(highest_weight)
    # Find the box with that index and then locate the closest unclaimed target
    current_box = box_locs[highest_weight_index]
    # Find manhattan distance to each unclaimed target and use smallest value
    smallest_dist = (10000, 10000)
    target_index = -1
    for target in unclaimed_targets:
        target_index += 1
        man_dist = tuple(map(operator.sub, current_box, target))
        man_dist = (abs(man_dist[0]), abs(man_dist[1]))
        if man_dist < smallest_dist:
            smallest_dist = man_dist
    # Smallest distance has been found, add to get total manhattan steps
    total += (smallest_dist[0] + smallest_dist[1])
    # Remove claimed target
    unclaimed_targets.remove(target)
    print(total)

# unclaimed_targets = targets.copy()
# target_index = -1
# for i in range(len(box_locs)):
#     smallest_dist = (10000, 10000)
#     for target in unclaimed_targets:
#         target_index += 1
#         man_dist = tuple(map(operator.sub, box_locs[i], target))
#         man_dist = (abs(man_dist[0]), abs(man_dist[1]))
#         if man_dist < smallest_dist:
#             smallest_dist = man_dist
#     # Smallest distance has been found, add to get total manhattan steps
#     total += (smallest_dist[0] + smallest_dist[1])
#     # Remove claimed target
#     unclaimed_targets.remove(target)
print(total)