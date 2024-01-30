struct ToRref;
impl ToRref {
    pub fn process(&self, matrix: &mut Vec<Vec<f32>>) {
        self.sort_by_leading_number(matrix);
        let n = matrix.len();
        let m = matrix[0].len() - 1;
        println!("n={}, m={}", n, m);
        let mut row_pointer = 0;
        for i in 0..m {
            if self.is_zero_col(matrix, row_pointer, i) {
                continue;
            }
            println!("{}, {}", row_pointer, i);
            self.get_first_row_with_leading_num(matrix, row_pointer, i);
            matrix[row_pointer] =
                self.row_multiply(&matrix[row_pointer], 1.0 / matrix[row_pointer][i]);
            self.gauss_elimination(matrix, row_pointer, i);
            row_pointer += 1;
            if row_pointer >= n {
                break;
            }
        }
        self.sort_by_leading_number(matrix);
    }
    fn is_zero_col(&self, matrix: &mut Vec<Vec<f32>>, row_pointer: usize, col: usize) -> bool {
        for i in row_pointer..matrix.len() {
            if matrix[i][col] != 0.0 {
                return false;
            }
        }
        true
    }
    fn get_first_row_with_leading_num(
        &self,
        matrix: &mut Vec<Vec<f32>>,
        row_pointer: usize,
        col: usize,
    ) {
        let n = matrix.len();
        for j in row_pointer..n {
            if matrix[j][col] == 0.0 {
                continue;
            }
            matrix.swap(j, row_pointer);
            break;
        }
    }
    fn gauss_elimination(&self, matrix: &mut Vec<Vec<f32>>, row_pointer: usize, col: usize) {
        for j in 0..matrix.len() {
            if j == row_pointer {
                continue;
            }
            matrix[j] = self.row_add(
                &matrix[j],
                &self.row_multiply(&matrix[row_pointer], -matrix[j][col]),
            );
        }
    }
    fn sort_by_leading_number(&self, matrix: &mut Vec<Vec<f32>>) {
        matrix.sort_by_key(|row| row.iter().position(|&x| x != 0.0).unwrap_or(row.len()));
    }
    fn row_multiply(&self, row: &Vec<f32>, c: f32) -> Vec<f32> {
        let mut ans: Vec<f32> = (*row.clone()).to_vec();
        ans = ans.iter_mut().map(|x| *x * c).collect();
        ans
    }
    fn row_add(&self, row1: &Vec<f32>, row2: &Vec<f32>) -> Vec<f32> {
        let mut row1 = (*row1.clone()).to_vec();
        let row2 = (*row2.clone()).to_vec();
        row1.iter_mut()
            .enumerate()
            .map(|(i, x)| *x + row2[i])
            .collect()
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() {
        let mut matrix = vec![vec![1.0, 2.0, 3.0], vec![2.0, 4.0, 6.0]];
        let expected = vec![vec![1.0, 2.0, 3.0], vec![0.0, 0.0, 0.0]];

        ToRref.process(&mut matrix);
        println!("{:?}", matrix);
        assert_eq!(matrix, expected);
    }
}
fn main() {
    let mut matrix = vec![
        vec![1.0, 1.0, 1.0, 1.0, 1.0],
        vec![3.0, 1.0, 1.0, 0.0, 3.0],
        vec![1.0, 1.0, 0.0, 1.0, 4.0],
    ];
    let mut matrix1 = vec![
        vec![1.0, 3.0, 1.0, 0.0],
        vec![2.0, 5.0, 0.0, 0.0],
        vec![-3.0, 3.0, 1.0, 0.0],
    ];
    ToRref.process(&mut matrix1);
    println!("{:?}", matrix1);
}
