struct ToRref;
impl ToRref {
    pub fn process(&self, matrix: &mut Vec<Vec<f32>>) {
        self.sort_by_leading_number(matrix);
        let n = matrix.len();
        let m = matrix[0].len() - 1;
        let mut row_pointer = 0;
        for i in 0..m {
            let mut has_num = false;
            for j in row_pointer..n {
                if matrix[j][i] == 0.0 {
                    continue;
                }
                matrix.swap(j, row_pointer);
                has_num = true;
                break;
            }
            if !has_num {
                continue;
            }
            matrix[row_pointer] = self.row_multiply(&matrix[row_pointer], 1.0 / matrix[row_pointer][i]);
            // println!("{:?}", matrix);
            for j in 0..n {
                if j == row_pointer {continue;}
                matrix[j] = self.row_add(
                    &matrix[j], 
                    &self.row_multiply(
                        &matrix[row_pointer], 
                        -matrix[j][i]
                    )
                );
            }
            row_pointer += 1;
        }
    }
    fn sort_by_leading_number(&self, matrix: &mut Vec<Vec<f32>>) {
        matrix.sort_by_key(|row| row.iter().position(|&x| x != 0.0).unwrap_or(row.len()));
    }
    fn row_multiply(&self, row: &Vec<f32>, c: f32) -> Vec<f32> {
        let mut ans: Vec<f32> = (*row.clone()).to_vec();
        ans = ans.iter_mut().map(|x| {*x * c}).collect();
        ans
    }
    fn row_add(&self, row1: &Vec<f32>, row2: &Vec<f32>) -> Vec<f32> {
        let mut row1 = (*row1.clone()).to_vec();
        let row2 = (*row2.clone()).to_vec();
        row1.iter_mut().enumerate().map(|(i, x)|{*x + row2[i]}).collect()
    }
}
fn main() {
    let mut matrix = vec![vec![0.0, 1.0, -1.0, 4.0], 
    vec![2.0, 0.0, 6.0, 4.0], vec![3.0, 2.0, 2.0, -1.0]];
    ToRref.process(&mut matrix);
    println!("{:?}", matrix);
}
