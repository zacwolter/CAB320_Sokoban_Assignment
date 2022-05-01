"""
THIS FILE IS PURELY FOR TESTING PURPOSES ONLY

Author: Zac :)
"""

from mySokobanSolver import check_elem_action_seq
from sokoban import Warehouse
import operator

wh = Warehouse()
# forth test - complete legal solve
wh.load_warehouse("./warehouses/warehouse_143.txt")
answer = check_elem_action_seq(wh, ['Up', 'Right', 'Right', 'Down', 'Up', 'Left', 'Left',
                                    'Down', 'Right', 'Down', 'Right', 'Left', 'Up', 'Up',
                                    'Right', 'Down', 'Right', 'Down', 'Down', 'Left',
                                    'Up', 'Right', 'Up', 'Left', 'Down', 'Left', 'Up', 
                                    'Right', 'Up', 'Left'])
print('<<  check_elem_action_seq, test 4>>')
print(wh.__str__())

box_locs = [(3,6), (2,6)]
worker_loc = (4,6)
wall_locs = [(1,5), (1,6), (1,7), (1,8), (2,8), (3,8), (4,8), (5,8), (5,7), (5,6), (5,5), (4,5), (3,5)]
num_rows = 6
num_rows = 9



# weights = None
# box_locs = [(3,6), (4,7)]
# worker_loc = (4,6)
# wall_locs = [(1,6), (1,5), (1,7), (1,8), (2,8), (3,8), (4,8), (5,8), (5,7), (5,6), (5,5), (4,5), (3,5)]
# targets = [(4, 2), (4, 4)]
# box_above = [(x,y) for (x,y) in box_locs if x == worker_loc[0] - 1 if worker_loc[1] == y]
# print(box_above)
# blocking_box = [(x,y) for (x,y) in box_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
# print(blocking_box)
# blocking_wall = [(x,y) for (x,y) in wall_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
# print(blocking_wall)
# box_below = [(x,y) for (x,y) in box_locs if x == worker_loc[0] + 1 if worker_loc[1] == y]
# print(box_below)

# # Next check where the worker can move and append it to the list of possible actions
# legal_moves = []    # list of legal actions

# # UP: Check if there is a wall or a box in the space above the worker
# box_above = [(x,y) for (x,y) in box_locs if x == worker_loc[0] - 1 if worker_loc[1] == y]
# walls_above = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] - 1 if worker_loc[1] == y]
# if len(box_above) > 0:
#     # There is a box above the worker, need to check if there are any box/walls above the box
#     blocking_box_above = [(x,y) for (x,y) in box_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
#     blocking_wall_above = [(x,y) for (x,y) in wall_locs if x == box_above[0][0] - 1 if box_above[0][1] == y]
#     # If there is no blocking box or wall in the space above, append "UP" as a legal move 
#     # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
#     if len(blocking_box_above) == 0 and len(blocking_wall_above) == 0:
#         legal_moves.append("UP")
# elif len(walls_above) > 0:
#     # There is a wall above the worker, therefore we cannot move up
#     pass
# else:
#     # There is no wall or box above the player (WILL NEED TO CHECK FOR TABOO SPACES)
#     legal_moves.append("UP")

# # DOWN: Check if there is a wall or a box in the space below the worker
# box_below = [(x,y) for (x,y) in box_locs if x == worker_loc[0] + 1 if worker_loc[1] == y]
# walls_below = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] + 1 if worker_loc[1] == y]
# if len(box_below) > 0:
#     # There is a box below the worker, need to check if there are any box/walls below the box
#     blocking_box_below = [(x,y) for (x,y) in box_locs if x == box_below[0][0] + 1 if box_below[0][1] == y]
#     blocking_wall_below = [(x,y) for (x,y) in wall_locs if x == box_below[0][0] + 1 if box_below[0][1] == y]
#     # If there is no blocking box or wall in the space below, append "DOWN" as a legal move 
#     # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
#     if len(blocking_box_below) == 0 and len(blocking_wall_below) == 0:
#         legal_moves.append("DOWN")
# elif len(walls_below) > 0:
#     # There is a wall below the worker, therefore we cannot move up
#     pass
# else:
#     # There is no wall or box below the player (WILL NEED TO CHECK FOR TABOO SPACES)
#     legal_moves.append("DOWN")

# # LEFT: Check if there is a wall or a box in the space to the left of the worker
# box_left = [(x,y) for (x,y) in box_locs if x == worker_loc[0] if worker_loc[1] - 1 == y]
# walls_left = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] if worker_loc[1] - 1 == y]
# if len(box_left) > 0:
#     # There is a box to the left of the worker, need to check if there are any box/walls to the left of the box
#     blocking_box_left = [(x,y) for (x,y) in box_locs if x == box_left[0][0] if box_left[0][1] - 1 == y]
#     blocking_wall_left = [(x,y) for (x,y) in wall_locs if x == box_left[0][0] if box_left[0][1] - 1 == y]
#     # If there is no blocking box or wall in the space to the left, append "LEFT" as a legal move 
#     # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
#     if len(blocking_box_left) == 0 and len(blocking_wall_left) == 0:
#         legal_moves.append("LEFT")
# elif len(walls_left) > 0:
#     # There is a wall below the worker, therefore we cannot move up
#     pass
# else:
#     # There is no wall or box below the player (WILL NEED TO CHECK FOR TABOO SPACES)
#     legal_moves.append("LEFT")

# # RIGHT: Check if there is a wall or a box in the space to the right of the worker
# box_right = [(x,y) for (x,y) in box_locs if x == worker_loc[0] if worker_loc[1] + 1 == y]
# walls_right = [(x,y) for (x,y) in wall_locs if x == worker_loc[0] if worker_loc[1] + 1 == y]
# if len(box_right) > 0:
#     # There is a box to the right of the worker, need to check if there are any box/walls to the right of the box
#     blocking_box_right = [(x,y) for (x,y) in box_locs if x == box_right[0][0] if box_right[0][1] + 1 == y]
#     blocking_wall_right = [(x,y) for (x,y) in wall_locs if x == box_right[0][0] if box_right[0][1] + 1 == y]
#     # If there is no blocking box or wall in the space to the right, append "RIGHT" as a legal move 
#     # TO BE CHANGED ONCE TABOO CELLS ARE IMPLEMENTED, NEED TO CONSIDER THEM ALSO
#     if len(blocking_box_right) == 0 and len(blocking_wall_right) == 0:
#         legal_moves.append("RIGHT")
# elif len(walls_right) > 0:
#     # There is a wall below the worker, therefore we cannot move up
#     pass
# else:
#     # There is no wall or box below the player (WILL NEED TO CHECK FOR TABOO SPACES)
#     legal_moves.append("RIGHT")

# # print(legal_moves)

# # print(box_locs)
# # box_up_index = box_locs.index(box_above[0])
# # print(box_up_index)
# # box_locs[box_up_index] = (box_above[0][0] + 1, box_above[0][1])
# # print(box_locs)
# # print(worker_loc)
# # worker_loc = (worker_loc[0] + 1, worker_loc[1])
# # print(worker_loc)

# total = 0
# worker_dist_to_boxes = []
# for (x,y) in box_locs:
#     worker_dist_to_boxes.append((abs(x - worker_loc[0]), abs(y - worker_loc[1])))
# closest_box_to_worker = min(worker_dist_to_boxes)
# total += (closest_box_to_worker[0] + closest_box_to_worker[1])
# print(total)

# # # Need to use index() to select each box in descending order
# weights_tracker = weights.copy()
# unclaimed_targets = targets.copy()
# for i in range(len(weights)):
#     highest_weight = 0
#     # Find current highest weight
#     for weight in weights_tracker:
#         if weight > highest_weight:
#             highest_weight = weight
#     # Get index of highest weight
#     highest_weight_index = weights.index(highest_weight)
#     # Remove weight from weights_tracker
#     weights_tracker.remove(highest_weight)
#     # Find the box with that index and then locate the closest unclaimed target
#     current_box = box_locs[highest_weight_index]
#     # Find manhattan distance to each unclaimed target and use smallest value
#     smallest_dist = (10000, 10000)
#     target_index = -1
#     for target in unclaimed_targets:
#         target_index += 1
#         man_dist = tuple(map(operator.sub, current_box, target))
#         man_dist = (abs(man_dist[0]), abs(man_dist[1]))
#         if man_dist < smallest_dist:
#             smallest_dist = man_dist
#     # Smallest distance has been found, add to get total manhattan steps
#     total += (smallest_dist[0] + smallest_dist[1])
#     # Remove claimed target
#     unclaimed_targets.remove(target)
#     print(total)

# # unclaimed_targets = targets.copy()
# # target_index = -1
# # for i in range(len(box_locs)):
# #     smallest_dist = (10000, 10000)
# #     for target in unclaimed_targets:
# #         target_index += 1
# #         man_dist = tuple(map(operator.sub, box_locs[i], target))
# #         man_dist = (abs(man_dist[0]), abs(man_dist[1]))
# #         if man_dist < smallest_dist:
# #             smallest_dist = man_dist
# #     # Smallest distance has been found, add to get total manhattan steps
# #     total += (smallest_dist[0] + smallest_dist[1])
# #     # Remove claimed target
# #     unclaimed_targets.remove(target)
# print(total)
#print(legal_moves)

#print(box_locs)
#box_up_index = box_locs.index(box_above[0])
# print(box_up_index)
# box_locs[box_up_index] = (box_above[0][0] + 1, box_above[0][1])
# print(box_locs)
# print(worker_loc)
# worker_loc = (worker_loc[0] + 1, worker_loc[1])
# print(worker_loc)

wh = Warehouse()
wh.load_warehouse("./warehouses/warehouse_81.txt")
wall_locs = wh.walls

# wall_locs.append((1,3))
# wall_locs.sort()

num_cols = wh.ncols
target_locs = wh.targets

tb_cells = []
empty_spaces_inside = []
for i in range(num_cols - 1):
    if i == 0:
        continue
    current_row = i
    walls_in_row = [(x,y) for (x,y) in wall_locs if x == i]
    walls_in_row.sort()
    first_wall_in_row = walls_in_row[0]
    last_wall_in_row = walls_in_row[-1]
    empty_spaces_inside_row = [(current_row,y) for y in range(first_wall_in_row[1], last_wall_in_row[1]+1) 
                            if (current_row,y) not in walls_in_row]
    empty_spaces_inside.append(empty_spaces_inside_row)

# Now check Rule 1 - check if each free space is a corner and not a target
for row in empty_spaces_inside:
    for space in row:
        if space in target_locs:
            # Ignore targets, they cannot be taboo cells
            continue
        
        num_surrounding_walls = 0
        surrounding_sides = []
        # Check for at least two walls surrounding the current cell (above, below, left or right)
        # If surrounding cells are opposite sides and only two cells surrounding, then NOT taboo
        # ABOVE
        if (space[0]-1, space[1]) in wall_locs:
            num_surrounding_walls += 1
            surrounding_sides.append("ABOVE")
        # BELOW
        if (space[0]+1, space[1]) in wall_locs:
            num_surrounding_walls += 1
            surrounding_sides.append("BELOW")
        # LEFT
        if (space[0], space[1]-1) in wall_locs:
            num_surrounding_walls += 1
            surrounding_sides.append("LEFT")
        # RIGHT
        if (space[0], space[1]+1) in wall_locs:
            num_surrounding_walls += 1
            surrounding_sides.append("RIGHT")
        
        if num_surrounding_walls == 2:
            if "ABOVE" in surrounding_sides and "BELOW" in surrounding_sides:
                # IGNORE as box can pass through
                pass
            elif "LEFT" in surrounding_sides and "RIGHT" in surrounding_sides:
                # IGNORE as box can pass through
                pass
            else:
                tb_cells.append(space)
        elif num_surrounding_walls > 2:
            tb_cells.append(space)

# Now check Rule 2 - check all cells between two taboo cells along walls
# Starting vertically (column-wise)
tb_cell_tracker = tb_cells.copy()
current_col = 0
prev_col = 0
for tb_cell in tb_cell_tracker:
    prev_col = current_col
    current_col = tb_cell[0]
    if current_col == prev_col:
        continue
    tb_cell_same_col = [cell for cell in tb_cells if tb_cell[0] == cell[0]]

    if len(tb_cell_same_col) < 2:
        continue
    if len(tb_cell_same_col) == 2:
        # Check there are no walls between the two cells
        walls_between = [wall for wall in wall_locs if wall[0] == current_col and wall[1] > tb_cell_same_col[0][1]
                        and wall[1] < tb_cell_same_col[1][1]]
        if len(walls_between) == 0:
            # No walls found between the two cells
            # Now ensure that none of the in-between cells are a target
            cells_between = [(current_col, y) for y in range(tb_cell_same_col[0][1]+1, tb_cell_same_col[1][1])]
            target_found = False
            for cell in cells_between:
                if cell in target_locs:
                    target_found = True
            if target_found:
                # One fo the cells was a target, so ignore
                continue
            # Now ensure that all cells have at least one wall adjacent to them
            cells_checked_positive = 0
            for cell in cells_between:
                num_adj_cells = 0
                # ABOVE
                if (cell[0]-1, cell[1]) in wall_locs:
                    num_adj_cells += 1
                # BELOW
                if (cell[0]+1, cell[1]) in wall_locs:
                    num_adj_cells += 1
                # LEFT
                if (cell[0], cell[1]-1) in wall_locs:
                    num_adj_cells += 1
                # RIGHT
                if (cell[0], cell[1]+1) in wall_locs:
                    num_adj_cells += 1
                if num_adj_cells >= 1:
                    cells_checked_positive += 1
            if cells_checked_positive == len(cells_between):
                # Add all cells in cells_between to tb_cells
                for cell in cells_between:
                    tb_cells.append(cell)
                    tb_cells.sort()
    elif len(tb_cell_same_col) > 2:
        # Check through each adjacent pair of cells, ensuring that there are no walls between them
        for i in range(1, len(tb_cell_same_col)):
            # Check there are no walls between the two cells
            walls_between = [wall for wall in wall_locs if wall[0] == current_col and wall[1] > tb_cell_same_col[i-1][1]
                            and wall[1] < tb_cell_same_col[i][1]]
            if (len(walls_between)) == 0:
                # Check all cells between are adjacent to a wall
                # Now ensure that none of the in-between cells are a target
                cells_between = [(current_col, y) for y in range(tb_cell_same_col[i-1][1]+1, tb_cell_same_col[i][1])]
                target_found = False
                for cell in cells_between:
                    if cell in target_locs:
                        target_found = True
                if target_found:
                    # One fo the cells was a target, so ignore
                    continue
                # Now ensure that all cells have at least one wall adjacent to them
                cells_checked_positive = 0
                for cell in cells_between:
                    num_adj_cells = 0
                    # LEFT
                    if (cell[0]-1, cell[1]) in wall_locs:
                        num_adj_cells += 1
                    # RIGHT
                    if (cell[0]+1, cell[1]) in wall_locs:
                        num_adj_cells += 1
                    # ABOVE
                    if (cell[0], cell[1]-1) in wall_locs:
                        num_adj_cells += 1
                    # BELOW
                    if (cell[0], cell[1]+1) in wall_locs:
                        num_adj_cells += 1
                    if num_adj_cells >= 1:
                        cells_checked_positive += 1
                if cells_checked_positive == len(cells_between):
                    # Add all cells in cells_between to tb_cells
                    for cell in cells_between:
                        tb_cells.append(cell)
                        tb_cells.sort()

# Now working horizontally (row-wise)
current_row = 0
prev_row = 0
for tb_cell in tb_cell_tracker:
    prev_row = current_row
    current_row = tb_cell[0]
    if current_row == prev_row:
        continue
    tb_cell_same_row = [cell for cell in tb_cells if tb_cell[1] == cell[1]]

    if len(tb_cell_same_row) < 2:
        continue
    if tb_cell_same_row[0][0] == tb_cell_same_row[1][0] - 1:
        continue
    if len(tb_cell_same_row) == 2:
        # Check there are no walls between the two cells
        walls_between = [wall for wall in wall_locs if wall[1] == current_row and wall[0] > tb_cell_same_row[0][0]
                        and wall[0] < tb_cell_same_row[1][0]]
        if len(walls_between) == 0:
            # No walls found between the two cells
            # Now ensure that none of the in-between cells are a target
            cells_between = [(x, tb_cell_same_row[0][1]) for x in range(tb_cell_same_row[0][0]+1, tb_cell_same_row[1][0])]
            target_found = False
            for cell in cells_between:
                if cell in target_locs:
                    target_found = True
            if target_found:
                # One fo the cells was a target, so ignore
                continue
            # Now ensure that all cells have at least one wall adjacent to them
            cells_checked_positive = 0
            for cell in cells_between:
                num_adj_cells = 0
                # LEFT
                if (cell[0]-1, cell[1]) in wall_locs:
                    num_adj_cells += 1
                # RIGHT
                if (cell[0]+1, cell[1]) in wall_locs:
                    num_adj_cells += 1
                # ABOVE
                if (cell[0], cell[1]-1) in wall_locs:
                    num_adj_cells += 1
                # BELOW
                if (cell[0], cell[1]+1) in wall_locs:
                    num_adj_cells += 1
                if num_adj_cells >= 1:
                    cells_checked_positive += 1
            if cells_checked_positive == len(cells_between):
                # Add all cells in cells_between to tb_cells
                for cell in cells_between:
                    tb_cells.append(cell)
                    tb_cells.sort()
    elif len(tb_cell_same_row) > 2:
        # Check through each adjacent pair of cells, ensuring that there are no walls between them
        for i in range(1, len(tb_cell_same_row)):
            # Check there are no walls between the two cells
            walls_between = [wall for wall in wall_locs if wall[0] == current_row and wall[1] > tb_cell_same_row[i-1][1]
                            and wall[1] < tb_cell_same_row[i][1]]
            if (len(walls_between)) == 0:
                # Check all cells between are adjacent to a wall
                # Now ensure that none of the in-between cells are a target
                cells_between = [(current_row, y) for y in range(tb_cell_same_row[i-1][1]+1, tb_cell_same_row[i][1])]
                target_found = False
                for cell in cells_between:
                    if cell in target_locs:
                        target_found = True
                if target_found:
                    # One fo the cells was a target, so ignore
                    continue
                # Now ensure that all cells have at least one wall adjacent to them
                cells_checked_positive = 0
                for cell in cells_between:
                    num_adj_cells = 0
                    # LEFT
                    if (cell[0]-1, cell[1]) in wall_locs:
                        num_adj_cells += 1
                    # RIGHT
                    if (cell[0]+1, cell[1]) in wall_locs:
                        num_adj_cells += 1
                    # ABOVE
                    if (cell[0], cell[1]-1) in wall_locs:
                        num_adj_cells += 1
                    # BELOW
                    if (cell[0], cell[1]+1) in wall_locs:
                        num_adj_cells += 1
                    if num_adj_cells >= 1:
                        cells_checked_positive += 1
                if cells_checked_positive == len(cells_between):
                    # Add all cells in cells_between to tb_cells
                    for cell in cells_between:
                        tb_cells.append(cell)
                        tb_cells.sort()
        
    

print(tb_cells)
