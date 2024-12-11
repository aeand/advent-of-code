mod day1;
mod day2;
mod day3;
mod day4;
mod day5;

fn main() {
  let path: &str = "/home/antan/Projects/advent-of-code/rust2024/input/";
  day1::day1a(&format!("{path}day1.txt"));
  day1::day1b(&format!("{path}day1.txt"));
  day2::day2a(&format!("{path}day2.txt"));
  day2::day2b(&format!("{path}day2.txt"));
  day3::day3a(&format!("{path}day3.txt"));
  day3::day3b(&format!("{path}day3.txt"));
  day4::day4a(&format!("{path}day4.txt"));
  day4::day4b(&format!("{path}day4.txt"));
  day5::day5a(&format!("{path}day5.txt"));
}