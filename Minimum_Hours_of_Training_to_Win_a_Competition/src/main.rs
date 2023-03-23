struct Solution {}
impl Solution {
    pub fn min_number_of_hours(
        initial_energy: i32,
        initial_experience: i32,
        energy: Vec<i32>,
        experience: Vec<i32>,
    ) -> i32 {
        let mut ans = 0;
        let mut cur_energy = initial_energy;
        let mut cur_experience = initial_experience;
        for i in 0..energy.len() {
            ans += 0.max(energy[i] + 1 - cur_energy);
            cur_energy = cur_energy.max(energy[i] + 1);
            ans += 0.max(experience[i] + 1 - cur_experience);
            cur_experience = cur_experience.max(experience[i] + 1);
            cur_energy -= energy[i];
            cur_experience += experience[i];
        }
        return ans;
    }
}
fn main() {
    println!(
        "{}",
        Solution::min_number_of_hours(5, 3, vec![1, 4, 3, 2], vec![2, 6, 3, 1]),
    );
}
