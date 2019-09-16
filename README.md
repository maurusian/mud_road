# mud_road
Solution to a 10xrecruit Problem

The problem consists of the following: we have a map of a forest with differing depths of mud for each spot. A traveler goes from one side
of the forest to the other, with the goal of minimizing the maximum amount of mud they have to step into. We represent the forest 
with a nxm matrix A, where each element represents the depth of mud in some unit of measure. Our problem is therefore to find the cost of
path that minimizes the maximum amount of mud. More abstractly, the cost of a path on our map is calculated as the maximum cost on the
nodes representing that path, and our goal is to minimize the path cost. The exact path is irrelevant to our solution, only the minimal
cost.

The cost is always a positive value, and though only integers are chosen for this problem, real values would be equally suitable, though
less efficient in terms of memory storage.
The dimensions of the matrix A can go from 2 to 1000, while the cost value can be any integer from 1 to 1000000.

The solution we propose is to eliminate the most costly nodes, one by one, by replacing them with -1, and checking at each time if a 
passage is still open, the first node to block passage from one side of the forest to the other would have the minimum cost for crossing.

Given the potentially large values of n and m, an efficient algorithm has to be implemented, particularly for the tasks of finding the
largest value in the matrix, and for searching for passage.
