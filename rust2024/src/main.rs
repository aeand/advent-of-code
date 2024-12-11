mod day1;
mod day2;
mod day3;
mod day4;
mod day5;

fn main() {
  let path: &str = "/home/antan/Projects/advent-of-code/rust2024/input/";
  day1::day1(&format!("{path}day1.txt"));
  day2::day2(&format!("{path}day2.txt"));
  day3::day3(&format!("{path}day3.txt"));
  day4::day4(&format!("{path}day4.txt"));
  day5::day5(&format!("{path}day5.txt"));
}