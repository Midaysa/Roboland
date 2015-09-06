import pprint, os


WIDTH = 10
HEIGHT = 10

class Robot():
    """ Robots gone wild! """
    
    def __init__(self, x, y, name, code):
        """ This method is called whenever a Robot instance is created """
        self.x = x
        self.y = y
        self.name = name
        self.code = code
        
    def __repr__(self):
        """ Print the robot's attributes """
        return "Name: " + str(self.name) + ", Coord x: " + str(self.x) + \
        ", Coord y: " + str(self.y) + ", Code: " +  str(self.code)
    
    def move(self, direction):
        """ Moves the robot in the given direction """
        direction = direction.lower()
        
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < HEIGHT:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < WIDTH:
            self.x += 1
        else: 
            print "CAUTION! The robot almost fall from the board"
            
    

# List comprehension to build the game board
board = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]


def print_board(board):
    """ Prints the board using python's pretty printing """
    pp = pprint.PrettyPrinter(indent = 2)
    pp.pprint(board)
    print 
    
def place(robot, board):
    """ Places the robot's code on the board in its x,y coordinate """
    board[robot.y][robot.x] = robot.code
    
def update_board(board, robot_list):
    """ Update robots positions """
    # clear every board's position
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[x][y] = 0
            
    # place every robot on the board
    for robot in robot_list:
        place(robot, board)
        


# Infinite game loop
robot1 = Robot(1,1,"Mida",1)
robot2 = Robot(1,2,"Piero",2)

while True:
    command = raw_input("Ingrese una accion: ")
    eval(command)
    robot_list = [robot1, robot2]
    update_board(board,robot_list)
    print_board(board)
