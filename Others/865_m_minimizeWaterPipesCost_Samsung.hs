{-
A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.
For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:
A <--> B <--> C <--> plant
Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.
In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
-}

import Data.List (delete, minimumBy)
import Data.Ord (comparing)

type Node = String
type Cost = Int
type Edge = (Node, Node, Cost)
type Graph = [Edge]

prims :: [Node] -> Graph -> Graph
prims _ [] = []
prims nodes edges
    | null nodes = []
    | otherwise = minimumEdge : prims (delete y nodes) (delete minimumEdge edges)
    where
        edgesFromNodes = filter (\(x, _, _) -> x 'elem' nodes) edges
        minimumEdge@(_, y, _) = minimumBy (comparing (\(_, _, c) -> c)) edgesFromNodes

main :: IO ()
main = do
    let nodes = ["plant", "A", "B", "C"]
    let edges = [("plant", "A", 1), ("plant", "B", 5), ("plant", "C", 20), ("A", "C", 15), ("B", "C", 10)]
    print $ prims nodes edges