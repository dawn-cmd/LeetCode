/*
 * @lc app=leetcode.cn id=289 lang=rust
 *
 * [289] 生命游戏
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        // Iterate over each cell in the board
        for i in 0..board.len() {
            for j in 0..board[0].len() {
                // Update the cell's state based on the next state
                board[i][j] = Solution::next_state(board, &position::new(i as i32, j as i32));
            }
        }
        // Convert the updated states to the final state representation
        for i in 0..board.len() {
            for j in 0..board[0].len() {
                board[i][j] = board[i][j] & 1;
            }
        }
    }

    pub fn next_state(board: &mut Vec<Vec<i32>>, pos: &position) -> i32 {
        // Count the number of live neighbors
        let count_life = Solution::count_life(board, pos);

        // Determine the next state based on the current state and the number of live neighbors
        if (board[pos.x as usize][pos.y as usize] == 0
            || board[pos.x as usize][pos.y as usize] == 2)
            && count_life == 3
        {
            return 3; // Next state is live
        }
        if (board[pos.x as usize][pos.y as usize] == 1
            || board[pos.x as usize][pos.y as usize] == 3)
            && (count_life < 2 || count_life > 3)
        {
            return 2; // Next state is dead
        }
        board[pos.x as usize][pos.y as usize] & 1 // Next state is the same as the current state
    }

    pub fn count_life(board: &Vec<Vec<i32>>, pos: &position) -> i32 {
        let mut count = 0;
        // Iterate over the neighbors of the current position
        for neighbor in pos.neighbors() {
            // Check if the neighbor is valid and alive
            if neighbor.is_valid(board)
                && (board[neighbor.x as usize][neighbor.y as usize] == 1
                    || board[neighbor.x as usize][neighbor.y as usize] == 2)
            {
                count += 1; // Increment the count of live neighbors
            }
        }
        count
    }
}

struct position {
    x: i32,
    y: i32,
}

impl position {
    pub fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }

    pub fn neighbors(&self) -> Vec<position> {
        let mut neighbors = Vec::new();
        // Iterate over the neighboring positions
        for i in -1..=1 {
            for j in -1..=1 {
                if i == 0 && j == 0 {
                    continue; // Skip the current position
                }
                neighbors.push(position::new(self.x + i, self.y + j)); // Add the neighbor to the list
            }
        }
        neighbors
    }

    pub fn is_valid(&self, board: &Vec<Vec<i32>>) -> bool {
        // Check if the position is within the bounds of the board
        self.x >= 0 && self.x < board.len() as i32 && self.y >= 0 && self.y < board[0].len() as i32
    }
}
// @lc code=end
