# mud_road
Solution to a 10xrecruit Problem

The problem consists of the following: we have a map of a forest with differing depths of mud for each spot. A traveler goes from one side
of the forest to the other, with the goal of minimizing the maximum amount of mud they have to step into. We represent the forest 
with a N x M matrix A, N being the number of rows and M the number of columns, where each matrix element a(i,j) represents the depth of mud in some unit of measure. A path is defined as a series of nodes with coordinates (i,j), such that the next node on the path is connected to the previous one, by adding 1 to i or j, or substracting 1 from one of them, but not both. In other words, for a given node (i,j), the next node can be either (i+1,j), (i,j+1), (i-1,j) or (i,j-1). This corresponds to going down, right, up or left on the matrix (or south, east, north, or west on the map) respectively, but not in a diagonal. A path starts at a node on the leftmost column of the matrix (j=0), and ends at a node on the rightmost side (j=M-1) The cost of a path is calculated as the maximum cost among the individual costs of the nodes representing that path, and our goal is to minimize the path cost. The exact path is irrelevant to our solution, only the minimal cost on the whole map.

The cost is always a positive value, and though only integers are chosen for this problem, real values would be equally suitable, though
less efficient in terms of memory storage. One can also argue that with a change of unit, we can, in most cases, convert the real value
costs into integer value costs, with a sufficiently good approximation. Furthermore, viewed from a purely mathematical point, the cost
configuration is unique by virtue of the relationship of matrix elements with each other, that is the order of the a(i,j) elements of the
matrix A, following the basic order law in the set of numbers (a-b negative => a<b and vice versa). The exact value of the a(i,j)'s is thus immaterial to the final solution whereby the optimal path has a particular cost a(i,j) located at row i and column j, as long as the relative order of the a(i,j)'s is preserved.

The problem description on 10xrecruit states that the dimensions of the matrix A can go from 2 to 1000, while the cost value can be any integer from 1 to 1000000. This is probably to test the efficiency of the algorithm within reasonable boundaries.

The basic solution we propose is to eliminate the most costly nodes, one by one, by replacing them with -1, and checking at each time if a 
passage is still open, the first node to block passage from one side of the forest to the other would have the minimum cost for crossing.

Given the potentially large values of N and M, an efficient algorithm has to be implemented, particularly for the tasks of finding the
largest value in the matrix, and for searching for passage.

To test the efficiency of the algorithm I implemented, I run a timed simulation of the problem a number of times (reps), for values of 
square matrix size that go from 2 to max_dim (determined by the user), and for random cost values going from 1 to max_value (also user
determined).

The first solution we implemented (will be detailed below), has a polynomial efficiency with a coefficient around 3,17 relative to the 
dimension of the square matrix.
