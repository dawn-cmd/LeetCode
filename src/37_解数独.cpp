#include <bits/stdc++.h>
using namespace std;
class Solution {
private:
    bool is_find = false;
    int lines[10][20];
    int columns[10][20];
    int blocks[10][10][20];
    long long steps = 0;

public:
    vector<vector<int>> convert(const vector<vector<char>> &board) {
        vector<vector<int>> ans(board.size());
        for (int i = 0; i < ans.size(); ++i) ans[i] = vector<int>(board[0].size());
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[i].size(); ++j) {
                ans[i][j] = (board[i][j] == '.') ? (-1) : (board[i][j] - '0');
            }
        }
        return ans;
    }
    vector<vector<char>> convertBack(const vector<vector<int>> &board) {
        vector<vector<char>> ans(board.size());
        for (int i = 0; i < board.size(); ++i) ans[i] = vector<char>(board[0].size());
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[i].size(); ++j) {
                ans[i][j] = (board[i][j] == -1) ? ('.') : ('0' + board[i][j]);
            }
        }
        return ans;
    }
    void dfs(vector<vector<int>> &board, int pos) {
        ++steps;
        if (pos == board.size() * board[0].size()) {
            is_find = true;
            return;
        }
        int x = pos / board[0].size();
        int y = pos % board[0].size();
        if (board[x][y] != -1) {
            dfs(board, pos + 1);
            return;
        }
        for (int i = 1; i < 10 && !is_find; ++i) {
            if (lines[x][i] || columns[y][i] || blocks[x / 3][y / 3][i]) continue;
            lines[x][i] = columns[y][i] = blocks[x / 3][y / 3][i] = 1;
            board[x][y] = i;
            dfs(board, pos + 1);
            lines[x][i] = columns[y][i] = blocks[x / 3][y / 3][i] = 0;
            if (!is_find) board[x][y] = -1;
        }
    }
    void solveSudoku(vector<vector<char>> &board) {
        vector<vector<int>> tmp = convert(board);
        memset(lines, 0, sizeof(lines));
        memset(columns, 0, sizeof(columns));
        memset(blocks, 0, sizeof(blocks));
        for (int i = 0; i < tmp.size(); ++i) {
            for (int j = 0; j < tmp[0].size(); ++j) {
                if (tmp[i][j] == -1) continue;
                lines[i][tmp[i][j]] = columns[j][tmp[i][j]] = blocks[i / 3][j / 3][tmp[i][j]] = 1;
            }
        }
        dfs(tmp, 0);
        board = convertBack(tmp);
        cout << "It takes " << steps << " steps to solve the problem." << '\n';
    }
};
int main() {
    vector<vector<char>> board{{'5', '3', '.', '.', '7', '.', '.', '.', '.'}, {'6', '.', '.', '1', '9', '5', '.', '.', '.'}, {'.', '9', '8', '.', '.', '.', '.', '6', '.'}, {'8', '.', '.', '.', '6', '.', '.', '.', '3'}, {'4', '.', '.', '8', '.', '3', '.', '.', '1'}, {'7', '.', '.', '.', '2', '.', '.', '.', '6'}, {'.', '6', '.', '.', '.', '.', '2', '8', '.'}, {'.', '.', '.', '4', '1', '9', '.', '.', '5'}, {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
    Solution().solveSudoku(board);
    for (int i = 0; i < board.size(); ++i) {
        for (int j = 0; j < board[0].size(); ++j) {
            cout << board[i][j] << ' ';
        }
        cout << endl;
    }
}
