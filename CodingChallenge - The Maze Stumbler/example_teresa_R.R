
#
# ::author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg
#
# ::descript:  Simple example code for the EMBL Coding Club Summer Challenge 2017,
#              showing how to load and visualize a maze, as well as a very
#              primitive "Teresa bot" based on random decisions.
#
# ::warning:   This code may contain small bugs and poorly styled R code; I have
#              almost no experience with R, so this is a bit cobbled together. ;p
#


#### Prep ####

# Set the working directory (if necessary)
#setwd("/path/to/your/codingClubChallengeDirectory")


#### Loading a Maze ####

# Load the maze and store it in a matrix, which is the ideal object
# for storing large grids of simple numbers like this. Note that
# the transpose `t(maze)` is necessary to get the correct orientation.
path <- "maze_small_0.txt"
maze <- read.table(file=path, sep=',')
maze <- as.matrix(t(maze))


#### Displaying the Maze ####

# Note that the matrix needs to be transposed and reversed for the maze 
# to be plotted in the correct orientation.
x11(width=9, height=9)  # Adjust window size
image( t(apply(maze,1,rev)), col=grey(c(0,1)), axes=FALSE, asp=1)


#### Stumbling Teresa ####

# This is a very simple implementation of the "maze walker" Teresa.
# Here, she simply moves in a random direction at every step. 
# If that direction happens to be a wall, she stops and tries again. 
# With this approach, she will (eventually) get to the exit, but it 
# will take a long time, especially for larger mazes...
# Can you improve Teresa's algorithm?

# Teresa's initial position is at the entrance (top left)
# Note: the position is given as (x,y), where x counts from left to
#       right and y counts from top to bottom.
teresa <- c(2,1)


#### Update Function ####

# Define a function that updates Teresa's position
update_position <- function(position, maze){
  
    # Randomly decide one of the four directions
    directions <- list(c(-1,0), c(1,0), c(0,-1), c(0,1))
    move <- directions[[sample(1:4, 1)]]
          
    # Just in case Teresa is still standing at the entrance,
    # prevent her from moving back out of the maze
    if(all(position == c(2,1)) & (move[2] == -1)){
        move <- c(0,0)
    }

    # Check if there is a wall in the direction of movement
    else if(maze[position[1]+move[1],position[2]+move[2]] == 0){
        move <- c(0,0)
    }
    
    # Apply the movement to the position
    new_position <- c(position[1]+move[1], position[2]+move[2])

    # Return the updated position
    return(new_position)
}


#### Execution ####

# Prepare the initial state
exit_found <- FALSE
max_steps  <- 100000
explored <- matrix(0, dim(maze)[1], dim(maze)[2])  # To keep track of Teresa's path
explored[teresa[1],teresa[2]] <- 1
step_index <- 2

# Loop through updates of the position
while(exit_found==FALSE){
  
    # Update
    teresa <- update_position(teresa, maze)

    # Keep track of the movement
    explored[teresa[1],teresa[2]] <- 1
    step_index = step_index + 1

    # Check if the exit was found
    if( all(teresa==c(dim(maze)[1]-1,dim(maze)[2])) ){
        print("I've found the exit!")
        exit_found <- TRUE
    }
        
    # After 100000 steps, give up
    else if(step_index==max_steps+1){
        print("I'm tired - I give up!")
        break
    }
}


#### Plotting ####

# Display the explored area
x11(width=9, height=9)  # Adjust window size
image( t(apply(maze,1,rev)), col=grey(c(0,1)), axes=FALSE, asp=1)  # Plot the maze
image( t(apply(explored,1,rev)), col=c(rgb(0,0,0,0),rgb(1,0,0,1)), axes=FALSE, asp=1, add=T) # Overlay the explored parts (with transparent walls)



