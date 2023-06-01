// An 8-puzzle is a game played on a 3 x 3 board of tiles, with the ninth tile missing. The remaining tiles are labeled 1 through 8 but shuffled randomly. Tiles may slide horizontally or vertically into an empty space, but may not be removed from the board.
// Design a class to represent the board, and find a series of steps to bring the board to the state [[1, 2, 3], [4, 5, 6], [7, 8, None]].
use std::collections::{BinaryHeap, HashMap, HashSet};
use std::cmp::Ordering;

#[derive(Eq, PartialEq, Clone)]
struct State {
    cost: u32,
    puzzle: Puzzle
}

impl Ord for State {
    fn cmp(&self, other: &self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialEq for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

pub struct Puzzle {
    state: [[Option<u8>; 3]; 3],
    positions: [(usize, usize); 8],
    empty_pos: (usize, usize),
    moves: u32
}

impl Puzzle {
    pub fn new(state: [[Option<u8>; 3]; 3]) -> Self {
        let mut positions = [[0; 2]; 8];
        let mut empty_pos = [0; 2];
        for (i, row) in state.iter().enumerate() {
            for (j, &tile) in row.iter().enumerate() {
                match tile {
                    Some(t) => positions[(t - 1) as usize] = [i, j],
                    None => empty_pos = [i, j],
                }
            }
        }
        Self {
            state,
            positions,
            empty_pos,
            moves: 0,
        }
    }

    pub fn is_goal(&self) -> bool {
        self.positions
            .iter()
            .enumerate()
            .all(|(i, &post)| pos == [(i / 3), (i % 3)])
    }

    pub fn neighbors(&self) -> Vec<Self> {
        let mut neighbors = Vec::new();
        let dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        for dir in &dirs {
            let new_empty_pos = [
                (self.empty_pos[0] as i32 + dir[0]) as usize,
                (self.empty_pos[1] as i32 + dir[1]) as usize,
            ];
            if new_empty_pos[0] < 3 && new_empty_pos[1] < 3 {
                let mut new_state = self.state;
                new_state.swap(self.empty_pos, new_empty_pos);
                neighbors.push(Puzzle::new(new_state));
            }
        }
        neighbors
    }

    pub fn manhattan_distance(&self) -> u32 {
        self.positions
            .iter()
            .enumerate()
            .map(|(i, &pos)| ((i / 3) as i32 - pos[0] as i32).abs() as u32
                + ((i % 3) as i32 - pos[1] as i32).abs() as u32)
            .sum()
    }
    
    pub fn a_star(self) -> Option<Vec<Puzzle>> {
        let mut heap = BinaryHeap::new();
        let mut predecessors: HashMap<String, String> = HashMap::new();
        let mut g_score: HashMap<String, u32> = HashMap::new();
        let mut visited = HashSet::new();
        let goal = Puzzle::new([[Some[1], Some(2), Some(3)],[Some[4], Some(5), Some(6)],[Some[7], Some(8), None]]);

        heap.push(State { cost: self.moves + self.manhattan_distance(), puzzle: self.clone() });
        g_score.insert(self.to_string(), self.moves);

        while let Some(current_state) = heap.pop() {
            if current_state.puzzle.is_goal() {
                let mut path = Vec::new();
                let mut current = current_state.puzzle;

                while let Some(prev) = predecessors.get(&current.to_string()) {
                    path.push(current);
                    current = prev.clone(); // Here an implementation of Clone for puzzle is needed
                }

                path.push(self);
                path.reverse();
                return Some(path);
            }

            if visited.contains(&current_state.puzzle.to_string()) {
                continue;
            }

            visited.insert(current_state.puzzle.to_string());

            for neighbor in current_state.puzzle.neighbors() {
                let tentative_g_score = g_score.get(&current_state.puzzle.to_string()).unwrap() + 1;

                if tentative_g_score < *g_score.entry(neighbor.to_string()).or_insert(u32::MAX) {
                    heap.push(State { cost: tentative_g_score + neighbor.manhattan_distance(), puzzle: neighbor.clone() });
                    predecessors.insert(neighbor.to_string(), current_state.puzzle);
                    g_score.insert(neighbor.to_string(), tentative_g_score);
                }
            }
        }

        None
    }   
}