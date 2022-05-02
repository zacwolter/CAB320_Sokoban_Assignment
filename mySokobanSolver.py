
'''

    Sokoban assignment


The functions and classes defined in this module will be called by a marker script. 
You should complete the functions and classes according to their specified interfaces.

No partial marks will be awarded for functions that do not meet the specifications
of the interfaces.

You are NOT allowed to change the defined interfaces.
In other words, you must fully adhere to the specifications of the 
functions, their arguments and returned values.
Changing the interfacce of a function will likely result in a fail 
for the test of your code. This is not negotiable! 

You have to make sure that your code works with the files provided 
(search.py and sokoban.py) as your code will be tested 
with the original copies of these files. 

Last modified by 2022-03-27  by f.maire@qut.edu.au
- clarifiy some comments, rename some functions
  (and hopefully didn't introduce any bug!)

'''

# You have to make sure that your code works with 
# the files provided (search.py and sokoban.py) as your code will be tested 
# with these files
from logging import exception
import search 
import operator
import collections
import sokoban

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)
    
    '''
    return [(10471227, "Zac", "Wolter"), (10468439, "Max", "Spokes"), (10524304, "Sebastian", "Poh")]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def extract_taboo_locations(lines):
        '''
        Extract taboo cell positional information from the the list of string 'lines'.
        The list of string 'lines' represents the puzzle.
        This function returns the coordinates of all taboo cells in (column, row) format.
        '''
        split_lines = lines.split('\n')
        tb_cells = list(sokoban.find_2D_iterator(split_lines, "X"))
        tb_cells.sort()
        return tb_cells

def flood_fill_search(cells, y, x, newcolor):
    #will be used as auxilary function to make job easier
    #uses DFS algorithm for flood fill
    Row, Column = len(cells),len(cells[0])#get the size of the workspace area
    Q = collections.deque([(y,x)]) 
    color = ['@','.','$','*',' '] #all possible string values within the workspace
    seen = set()#create a set called seen to store cells already passed through
    while Q: #while there are still values in Q continue the loop 
        row, column = Q.popleft() #store the row column that was in the 1st position of Q whilst removing it from Q
        cells[row][column] = newcolor #whatever the row,column value was first in Q, take that index position in
        #the working cell area with the value to indicate that its inside the working area
        if (row,column) in seen:
            continue #self-explanatory if index/position of current cell being looked at has already been covered
        #skip it to reduce unnecessary computing time 
        seen.add((row,column))#add the row and column in the first Q array and add to seen set
        #as we have already seen it 
        for add_r,add_c in ((1, 0), (0, 1), (-1, 0), (0, -1)):#consider the cells above,below,right and left
            #of the current cell
            new_r=row+add_r #get the new row values of cells adjacent
            new_c=column+add_c #get new column values of cells adjacent
            if 0<=new_r<Row and 0<=new_c<Column and cells[new_r][new_c] in color:
                Q.append((new_r,new_c)) #if the new column or row values are within the bounds
                #of the working area and the values have a viable value therefore 
                #they will be appended to be looked at in the next loop 
    return cells

def taboo_cells(warehouse):
    '''  
    Identify the taboo cells of a warehouse. A "taboo cell" is by definition
    a cell inside a warehouse such that whenever a box get pushed on such 
    a cell then the puzzle becomes unsolvable. 
    
    Cells outside the warehouse are not taboo. It is a fail to tag an 
    outside cell as taboo.
    
    When determining the taboo cells, you must ignore all the existing boxes, 
    only consider the walls and the target  cells.  
    Use only the following rules to determine the taboo cells;
     Rule 1: if a cell is a corner and not a target, then it is a taboo cell.
     Rule 2: all the cells between two corners along a wall are taboo if none of 
             these cells is a target.
    
    @param warehouse: 
        a Warehouse object with the worker inside the warehouse

    @return
       A string representing the warehouse with only the wall cells marked with 
       a '#' and the taboo cells marked with a 'X'.  
       The returned string should NOT have marks for the worker, the targets,
       and the boxes.
    '''
    
    #The rules identified from research are:
    # Rule 1: if a cell is a corner and not a target, then it is a taboo cell.
    # Rule 2: all cells between two corners along a wall are taboo if none of 
    #         these cells is a target.

    # Gather all necessary information from the warehouse (walls and target locations)
    wall_locs = warehouse.walls
    target_locs = warehouse.targets
    num_rows = warehouse.nrows

    # Rule 1: Cells that are not targets and are surrounded by walls are taboo
    # Assumptions:
    #   1. Warehouse interior spaces do not start until row 1 and column 1, as row 0 is always the
    #      top wall row and column 0 if the leftmost wall row
    #   2. All empty spaces between the first wall instance and last wall instance are
    #      inside the warehouse, regardless of if there are extra walls in-between
    
    # Start by identifying all interior empty spaces (incl. targets just to be safe)
    tb_cells = []
    empty_spaces_inside = []

    flood_fill_test=[]
    cells = str(warehouse).split('\n')#make it into a list
    idx=0

    for strings in cells:
        cells[idx] = list(strings)
        idx += 1
    flood_fill_test = cells[:]
    for row_index, i in enumerate(cells):
        for col_index, a in enumerate(i):
            if a == "#":
                flood_fill_test[row_index][col_index] = 5 #now we have a list filled with 5's as walls
    starting_point = target_locs[0]     #we know that the target is always in the working zone, therefore take first 
    #target value therefore starting point is the index of the first target
    #flood_fill_test[starting_point[1]][starting_point[0]]=1
    flood_fill_results = flood_fill_search(flood_fill_test, starting_point[1], starting_point[0], 1)

    for i in range(num_rows - 1):
        if i == 0:
            continue
        current_row = i
        # walls_in_row = [(x,y) for (x,y) in wall_locs if x == i]
        # walls_in_row.sort()
        empty_spaces_inside_row = []
        for j in range(len(flood_fill_results[i])):
            if flood_fill_results[i][j] == 1:
                empty_spaces_inside_row.append((j, i))
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
        current_row = tb_cell[1]
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

    X, Y = zip(*warehouse.walls)
    x_size, y_size = 1+max(X), 1+max(Y)
    
    # max_index = -1
    # for i in range(max(Y)+1):
    #     if max_index < i:
    #             max_index = i
    #     elif max_index == i:
    #         continue
    #     for j in range(max(X)):
    #         print(str(i) + ", " + str(j))
            

    vis = [[" "] * x_size for y in range(y_size)]
    for (x,y) in warehouse.walls:
        vis[y][x] = "#"
    for (x,y) in tb_cells:
        vis[y][x] = "X"
    string_version = "\n".join(["".join(line) for line in vis])
    return string_version
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class SokobanPuzzle(search.Problem):
    '''
    An instance of the class 'SokobanPuzzle' represents a Sokoban puzzle.
    An instance contains information about the walls, the targets, the boxes
    and the worker.

    Your implementation should be fully compatible with the search functions of 
    the provided module 'search.py'. 
    
    '''

    #     Revisit the sliding puzzle and the pancake puzzle for inspiration!
    #
    #     Note that you will need to add several functions to 
    #     complete this class. For example, a 'result' method is needed
    #     to satisfy the interface of 'search.Problem'.
    #
    #     You are allowed (and encouraged) to use auxiliary functions and classes

    
    def __init__(self, warehouse):
        self.initial = tuple(warehouse.boxes), tuple(warehouse.worker)
        self.problem = warehouse
        self.taboo = extract_taboo_locations(taboo_cells(warehouse))

    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state.
        
        """
        # THIS IS WHERE WE NEED TO BE ABLE TO DEFINE ALL AVAILABLE ACTIONS IN A GIVEN STATE
        #   - check_elem_action_seq seems to be more about testing a long sequence of actions
        #     when combined if they're legal or not
        
        # First gain an understanding of the current state
        worker_loc = state[1]
        box_locs = state[0]
        wall_locs = self.problem.walls
        tb_cells = self.taboo

        # Next check where the worker can move and append it to the list of possible actions
        legal_moves = []    # list of legal actions

        # UP: Check if there is a wall or a box in the space above the worker
        boxes_above = [box for box in box_locs if box[0] == worker_loc[0] and box[1] == worker_loc[1] - 1]
        walls_above = [wall for wall in wall_locs if wall[0] == worker_loc[0] and wall[1] == worker_loc[1] - 1]
        if len(boxes_above) > 0:
            # There is a box above the worker, need to check if there are any boxes/walls above the box
            blocking_box_above = [box for box in box_locs if box[0] == boxes_above[0][0] and box[1] == boxes_above[0][1] - 1]
            blocking_wall_above = [wall for wall in wall_locs if wall[0] == boxes_above[0][0] if wall[1] == boxes_above[0][1] - 1]
            taboo_cell_above = [cell for cell in tb_cells if cell[0] == boxes_above[0][0] if cell[1] == boxes_above[0][1] - 1]
            # If there is no blocking box or wall or taboo cell in the space above, append "UP" as a legal move 
            if len(blocking_box_above) == 0 and len(blocking_wall_above) == 0 and len(taboo_cell_above) == 0:
                legal_moves.append("Up")
        elif len(walls_above) > 0:
            # There is a wall above the worker, therefore we cannot move Up
            pass
        else:
            # There is no wall or box above the player
            legal_moves.append("Up")

        # DOWN: Check if there is a wall or a box in the space below the worker
        boxes_below = [box for box in box_locs if box[0] == worker_loc[0] and box[1] == worker_loc[1] + 1]
        walls_below = [wall for wall in wall_locs if wall[0] == worker_loc[0] and wall[1] == worker_loc[1] + 1]
        if len(boxes_below) > 0:
            # There is a box below the worker, need to check if there are any boxes/walls below the box
            blocking_box_below = [box for box in box_locs if box[0] == boxes_below[0][0] and box[1] == boxes_below[0][1] + 1]
            blocking_wall_below = [wall for wall in wall_locs if wall[0] == boxes_below[0][0] if wall[1] == boxes_below[0][1] + 1]
            taboo_cell_below = [cell for cell in tb_cells if cell[0] == boxes_below[0][0] if cell[1] == boxes_below[0][1] + 1]
            # If there is no blocking box or wall in the space below, append "DOWN" as a legal move 
            if len(blocking_box_below) == 0 and len(blocking_wall_below) == 0 and len(taboo_cell_below) == 0:
                legal_moves.append("Down")
        elif len(walls_below) > 0:
            # There is a wall below the worker, therefore we cannot move down
            pass
        else:
            # There is no wall or box below the player
            legal_moves.append("Down")

        # LEFT: Check if there is a wall or a box in the space to the left of the worker
        boxes_left = [box for box in box_locs if box[0] == worker_loc[0] - 1 and box[1] == worker_loc[1]]
        walls_left = [wall for wall in wall_locs if wall[0] == worker_loc[0] - 1 and wall[1] == worker_loc[1]]
        if len(boxes_left) > 0:
            # There is a box to the left of the worker, need to check if there are any boxes/walls to the left of the box
            blocking_box_left = [box for box in box_locs if box[0] == boxes_left[0][0] - 1 and box[1] == boxes_left[0][1]]
            blocking_wall_left = [wall for wall in wall_locs if wall[0] == boxes_left[0][0] - 1 if wall[1] == boxes_left[0][1]]
            taboo_cell_left = [cell for cell in tb_cells if cell[0] == boxes_left[0][0] - 1 if cell[1] == boxes_left[0][1]]
            # If there is no blocking box or wall in the space to the left, append "LEFT" as a legal move 
            if len(blocking_box_left) == 0 and len(blocking_wall_left) == 0 and len(taboo_cell_left) == 0:
                legal_moves.append("Left")
        elif len(walls_left) > 0:
            # There is a wall below the worker, therefore we cannot move up
            pass
        else:
            # There is no wall or box below the player
            legal_moves.append("Left")

        # RIGHT: Check if there is a wall or a box in the space to the right of the worker
        boxes_right = [box for box in box_locs if box[0] == worker_loc[0] + 1 and box[1] == worker_loc[1]]
        walls_right = [wall for wall in wall_locs if wall[0] == worker_loc[0] + 1 and wall[1] == worker_loc[1]]
        if len(boxes_right) > 0:
            # There is a box to the right of the worker, need to check if there are any boxes/walls to the right of the box
            blocking_box_right = [(x,y) for (x,y) in box_locs if x == boxes_right[0][0] + 1 if boxes_right[0][1] == y]
            blocking_wall_right = [(x,y) for (x,y) in wall_locs if x == boxes_right[0][0] + 1 if boxes_right[0][1] == y]
            taboo_cell_right = [cell for cell in tb_cells if cell[0] == boxes_right[0][0] + 1 if cell[1] == boxes_right[0][1]]
            # If there is no blocking box or wall in the space to the right, append "RIGHT" as a legal move 
            if len(blocking_box_right) == 0 and len(blocking_wall_right) == 0 and len(taboo_cell_right) == 0:
                legal_moves.append("Right")
        elif len(walls_right) > 0:
            # There is a wall below the worker, therefore we cannot move up
            pass
        else:
            # There is no wall or box below the player
            legal_moves.append("Right")
        
        return legal_moves
        
        # REFER TO testing.py FOR TESTING OF THE ABOVE CODE (VERIFIED WORKS ON WAREHOUSE 3)

    def result(self, state, action):
        """
        Return the state of the warehouse after the given action is completed

        Simply need to check if we're moving just the worker or a box also (keep in mind the actions should
        theoretically be legal based on the above function that checks it)
        """
        worker_loc = state[1]
        box_locs = state[0]
        
        # Use action to determine which direction the worker is moving and check if any boxes are in the path
        if action == "Left":
            box_left = [(x,y) for (x,y) in box_locs if x == worker_loc[0] - 1 if worker_loc[1] == y]
            if len(box_left) > 0:
                # Since there is a box left the worker that needs to be moved, change the location of the box
                # by decreasing the row number (push it up one space)
                box_index = box_locs.index(box_left[0])
                box_locs_list = list(box_locs)
                box_locs_list[box_index] = (box_left[0][0] - 1, box_left[0][1])
                box_locs = tuple(box_locs_list)
            # Regardless of if there's a box, still move the worker's location up one space
            worker_loc = (worker_loc[0] - 1, worker_loc[1])
        elif action == "Right":
            box_right = [(x,y) for (x,y) in box_locs if x == worker_loc[0] + 1 if worker_loc[1] == y]
            if len(box_right) > 0:
                # Since there is a box right the worker that needs to be moved, change the location of the box
                # by decreasing the row number (push it down one space)
                box_index = box_locs.index(box_right[0])
                box_locs_list = list(box_locs)
                box_locs_list[box_index] = (box_right[0][0] + 1, box_right[0][1])
                box_locs = tuple(box_locs_list)
            # Regardless of if there's a box, still move the worker's location down one space
            worker_loc = (worker_loc[0] + 1, worker_loc[1])
        elif action == "Up":
            box_above = [(x,y) for (x,y) in box_locs if x == worker_loc[0] if worker_loc[1] - 1 == y]
            if len(box_above) > 0:
                # Since there is a box to the above of the worker that needs to be moved, change the location of the box
                # by decreasing the row number (push it down one space)
                box_index = box_locs.index(box_above[0])
                box_locs_list = list(box_locs)
                box_locs_list[box_index] = (box_above[0][0], box_above[0][1] - 1)
                box_locs = tuple(box_locs_list)
            # Regardless of if there's a box, still move the worker's location down one space
            worker_loc = (worker_loc[0], worker_loc[1] - 1)
        elif action == "Down":
            box_below = [(x,y) for (x,y) in box_locs if x == worker_loc[0] if worker_loc[1] + 1 == y]
            if len(box_below) > 0:
                # Since there is a box to the below of the worker that needs to be moved, change the location of the box
                # by decreasing the row number (push it down one space)
                box_index = box_locs.index(box_below[0])
                box_locs_list = list(box_locs)
                box_locs_list[box_index] = (box_below[0][0], box_below[0][1] + 1)
                box_locs = tuple(box_locs_list)
            # Regardless of if there's a box, still move the worker's location down one space
            worker_loc = (worker_loc[0], worker_loc[1] + 1)
        
        new_state = tuple(box_locs), tuple(worker_loc)
        return new_state
    
    def goal_test(self, state):
        """
        Make a comparison between the initialised goal state and the current state, taking no
        notice of the position of the worker, just the position of the boxes

        The legal move checking system will ensure that the worker is in a legal state
        """
        boxes = state[0]
        #boxes = ((2,3), (11,3))
        if (set(boxes).issubset(set(self.problem.targets))):
            return True
        return False


    def path_cost(self, c, state1, action, state2): 
        """
        Return the cost of using action to travel from state1 to state2, taking into consideration
        the weight of the box and knowing that the cost to move one space is 1.
        """
        # Determine what has moved between the two states (could be just worker, or worker and box)
        if state1[1] != state2[1]:
            c = c + 1
        if state1[0] != state2[0]:
            # Find the index of the box and add the weight of the box as part of the cost, using the index
            # to identify the cost of the box movement
            box_moved = [(x,y) for (x,y) in state2[0] if (x,y) not in state1[0]]
            box_index = state2[0].index(box_moved[0])
            c = c + self.problem.weights[box_index]
        return c

    def h(self, state):
        # Need to take into consideration the distance of the worker from the nearest box (manhattan)
        # So h(n) = something + dist(worker --> nearest box)
        total = 0
        
        # Iterate through the boxes, determining the closest box to the worker 
        """ (that isn't in a target) """
        worker_loc = state.state[1]
        box_locs = state.state[0]
        differences = []
        for (x,y) in box_locs:
            differences.append((abs(x - worker_loc[0]), abs(y - worker_loc[1])))
        worker_dist_to_nearest_box = min(differences)

        # Add the manhattan distance to the total
        total += (worker_dist_to_nearest_box[0] + worker_dist_to_nearest_box[1] - 1)

        # Iterating through the boxes in weight order, determine the minimum distance to an unclaimed target
        targets = self.problem.targets
        
        # Check if there are any weights, if not, don't take them into consideration
        weights = self.problem.weights
        if len(weights) == 0: # OR IF ALL WEIGHTS ARE EQUAL:
            for i in range(len(box_locs)):
                # Find manhattan distance to each unclaimed target and use smallest value
                unclaimed_targets = targets.copy()
                target_index = -1
                for i in range(len(box_locs)):
                    smallest_dist = (10000, 10000)
                    for target in unclaimed_targets:
                        target_index += 1
                        man_dist = tuple(map(operator.sub, box_locs[i], target))
                        man_dist = (abs(man_dist[0]), abs(man_dist[1]))
                        if man_dist < smallest_dist:
                            smallest_dist = man_dist
                    # Smallest distance has been found, add to get total manhattan steps
                    total += (smallest_dist[0] + smallest_dist[1])
                    # Remove claimed target
                    unclaimed_targets.remove(target)
        else:
            # Need to use index() to select each box in descending order by weight
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
                target_index = 10000
                for target in unclaimed_targets:
                    man_dist = tuple(map(operator.sub, current_box, target))
                    man_dist = (abs(man_dist[0]), abs(man_dist[1]))
                    if man_dist < smallest_dist:
                        smallest_dist = man_dist
                        target_index = unclaimed_targets.index(target)
                # Smallest distance has been found, add to get total manhattan steps
                total += (smallest_dist[0] + smallest_dist[1])
                # Remove claimed target
                unclaimed_targets.remove(unclaimed_targets[target_index])

        return total

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def check_elem_action_seq(warehouse, action_seq):
    '''
     check_elem_actions determines whether a sequence of actions are legal or not
     within a given warehouse. Actions are deemed illegal if they:

        -  Cause the worker to hit a wall
        -  Cause the worker to push a box into a wall
        -  Cause the worker to push a box into another box

    @param 
     warehouse: a valid Warehouse object

    @return
    
        If puzzle cannot be solved 
            return 'Impossible', None
        
        If a solution was found, 
            return S, C 
            where S is a list of actions that solves
            the given puzzle coded with 'Left', 'Right', 'Up', 'Down'
            For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
            If the puzzle is already in a goal state, simply return []
            C is the total cost of the action sequence C

    '''

    # Where does the action result in the worker being located?
    for action in action_seq:
        if action == 'Left': # Left move
            resultant_worker = (warehouse.worker[0] - 1, warehouse.worker[1]) 
        elif action == 'Right': # Right move
            resultant_worker = (warehouse.worker[0] + 1, warehouse.worker[1]) 
        elif action == 'Up': # Up move
            resultant_worker = (warehouse.worker[0], warehouse.worker[1] - 1)
        elif action == 'Down': # Down move
            resultant_worker = (warehouse.worker[0], warehouse.worker[1] + 1)
        else:
            exception("[check_elem_action_seq] Error parsing action")

        # Check if the action results in the worker hitting a wall (no box considered)
        if warehouse.walls.count(resultant_worker) > 0: # Worker's resultant location is the same as a wall location
            return "Impossible"
        # Check if the action pushes a box
        elif warehouse.boxes.count(resultant_worker) > 0: # Worker's resultant location is the same as a box location (AKA they have pushed a box)
            index_box = warehouse.boxes.index(resultant_worker)

            box_displacement = (resultant_worker[0] - warehouse.worker[0], resultant_worker[1] - warehouse.worker[1])

            resultant_box = (warehouse.boxes[index_box][0] + box_displacement[0], warehouse.boxes[index_box][1] + box_displacement[1])

            # Check if the action pushes a box into a wall
            if warehouse.walls.count(resultant_box) > 0: # Box's resultant location is the same as a wall location
                return "Impossible"
            # Check if the action pushes a box into another box
            elif warehouse.boxes.count(resultant_box) > 0: # Box's resultant location is the same as a wall location
                return "Impossible"
            else: # Action deemed legal so worker and box are moved
                warehouse.boxes[index_box] = resultant_box
                warehouse.worker = resultant_worker
        else: # Action deemed legal and worker is moved
            warehouse.worker = resultant_worker

    return warehouse.__str__()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def trace_path(node):
    path = []
    while node.parent:
        path.insert(0, node.action) # insert at index 0 (start)
        node = node.parent
    return path
    
def print_solution(goal_node):
    path = goal_node.path()
    print("Solution Steps:\n")
    for node in path:
        if node.action is not None:
            print("{0},".format(node.action))

def solve_weighted_sokoban(warehouse):
    '''
    This function analyses the given warehouse.
    It returns the two items. The first item is an action sequence solution. 
    The second item is the total cost of this action sequence.

    @param 
     warehouse: a valid Warehouse object

    @return

        If puzzle cannot be solved
            return 'Impossible', None

        If a solution was found,
            return S, C 
            where S is a list of actions that solves
            the given puzzle coded with 'Left', 'Right', 'Up', 'Down'
            For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
            If the puzzle is already in a goal state, simply return []
            C is the total cost of the action sequence C


    Method:
    - If boxes in targets return S = [], C = 0 
    - solve sokoban with problem class
        - call astar_graph_search
        - calculate path_cost
    - return S and C


    '''

    if warehouse.__str__().count(".") == 0: # boxes are already on targets
        return "Impossible", None
    else: # puzzle needs to be solved
        sp = SokobanPuzzle(warehouse)
        astar = search.astar_graph_search(sp)
        if astar == None:
            return "Impossible", None
        else:
            print_solution(astar)
            S = trace_path(astar)
            C = astar.path_cost
            return S, C




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

