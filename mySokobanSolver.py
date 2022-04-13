
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
import search 
import sokoban


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)
    
    '''
    return [(10471227, "Zac", "Wolter"), (00000000, "Max", "Spokes"), (00000000, "Sebastian", "Poh")]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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

    ###
    # First, understanding what cells are inside the factory:
    #   Check 1: If a cell is empty AND there has been at least 1 cell that denoted a wall before it,
    #            then it is inside the warehouse
    #   Issue 1: All cells outside the warehouse on the right side of the final wall piece will be 
    #            counted incorrectly as inside
    #       Example:
    #
    #           "      # # # #      "    ==     "x x x # # # # o o o"
    #
    #         Where "x" denotes outside and "o" denotes inside
    #
    #       BUT:
    #           When looking at the warehouse .txt files, it appears that no spaces are added after
    #           the final wall in a line like so:
    #
    #           "      # # # #"     ==   "x x x # # # #"
    #
    #           Which is correct in identifying what is outside the warehouse
    #   HENCE Issue 1 is resolved based on the assumption that this occurrence is consistent across all
    #         warehouse .txt files.
    #   
    # Next, understanding how to denote horizontally and vertically adjacent taboo cells
    #   - We know that all corners that are not targets are taboo cells, and any cells between two corners
    #     are also taboo cells if none of them are a target
    #   - To understand if a taboo cell is a corner, all four sides (top, bottom, left and right) need to be
    #     checked for existing walls... if a cell has at least two walls surrounding it, then it is a corner
    #       - It is NOT logical to assume that a cell that is adjacent to one wall is part of a set of cells
    #         between two corners because some walls are standalone or within the confines of the warehouse
    #   - To find other cells that are taboo (cells that are part of a set of cells between two corners where
    #     no target cells lie), simply find the enclosing walls (either vertically or horizontally) and check
    #     if any of the cells between the two walls are targets. If not, then all cells that are enclosed are
    #     classified as taboo
    ###
    sokoban.find_2D_iterator()

    raise NotImplementedError()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class SokobanPuzzle(search.Problem):
    '''
    An instance of the class 'SokobanPuzzle' represents a Sokoban puzzle.
    An instance contains information about the walls, the targets, the boxes
    and the worker.

    Your implementation should be fully compatible with the search functions of 
    the provided module 'search.py'. 
    
    '''
    
    #
    #         "INSERT YOUR CODE HERE"
    #
    #     Revisit the sliding puzzle and the pancake puzzle for inspiration!
    #
    #     Note that you will need to add several functions to 
    #     complete this class. For example, a 'result' method is needed
    #     to satisfy the interface of 'search.Problem'.
    #
    #     You are allowed (and encouraged) to use auxiliary functions and classes

    
    def __init__(self, warehouse):
        # NEED TO DEFINE A GOAL STATE
        #   - Could do this by using the warehouse's extract_locations method and 
        #     setting the cells where the worker and boxes are to be empty, as well
        #     as setting the target cells to be full... do we need to consider the
        #     position of the worker in the goal state???? I personally don't think so
        #     because what matters is getting the boxes to the targets, whilst the position
        #     of the worker only determines what legal moves are available
        raise NotImplementedError

    def actions(self, state):
        
        """
        Return the list of actions that can be executed in the given state.
        
        """
        # THIS IS WHERE WE NEED TO BE ABLE TO DEFINE ALL AVAILABLE ACTIONS IN A GIVEN STATE
        #   - check_elem_action_seq seems to be more about testing a long sequence of actions
        #     when combined if they're legal or not
        raise NotImplementedError

    def result(self, state, action):
        """
        Return the state of the warehouse after the given action is completed (HECK)

        Looks like we will have to implement a separate function/class to do this complex
        step...
        """
        raise NotImplementedError
    
    def goal_test(self, state):
        """
        Make a comparison between the initialised goal state and the current state, taking no
        notice of the position of the worker, just the position of the boxes

        The legal move checking system will ensure that the worker is in a legal state
        """
        raise NotImplementedError

    def path_cost(self, c, state1, action, state2):
        """
        Return the cost of using action to travel from state1 to state2, taking into consideration
        the weight of the box and knowing that the cost to move one space is 1.
        """
        raise NotImplementedError
    
    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value.
        
        IT SEEMS LIKE THIS MIGHT BE THE HEURISTIC WE'RE IMPLEMENTING???
        """
        raise NotImplementedError

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def check_elem_action_seq(warehouse, action_seq):
    '''
    
    Determine if the sequence of actions listed in 'action_seq' is legal or not.
    
    Important notes:
      - a legal sequence of actions does not necessarily solve the puzzle.
      - an action is legal even if it pushes a box onto a taboo cell.
        
    @param warehouse: a valid Warehouse object

    @param action_seq: a sequence of legal actions.
           For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
           
    @return
        The string 'Impossible', if one of the action was not valid.
           For example, if the agent tries to push two boxes at the same time,
                        or push a box into a wall.
        Otherwise, if all actions were successful, return                 
               A string representing the state of the puzzle after applying
               the sequence of actions.  This must be the same string as the
               string returned by the method  Warehouse.__str__()
    '''
    
    ##         "INSERT YOUR CODE HERE"
    
    raise NotImplementedError()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

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

    '''
    
    raise NotImplementedError()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

