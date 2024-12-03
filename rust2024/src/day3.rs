use regex::Regex;

pub fn day3a() {
  let input = std::fs::read_to_string("/home/antan/Projects/advent-of-code/rust2024/input/day3.txt").unwrap();
  let re = Regex::new(r"mul\([\d]+,[\d]+\)").unwrap();
  let regex = re.find_iter(&input);

  let mut score = 0;
  for r in regex {
    let v: Vec<&str> = r.as_str().split(",").clone().collect();

    score +=
      v[0].replace("mul(", "").parse::<i32>().unwrap()
      * v[1].replace(")", "").parse::<i32>().unwrap();
  }

  // 175015740 right on
  println!("Day 3 A: {}", score);
}