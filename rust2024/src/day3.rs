use regex::Regex;

pub fn day3a() {
  let result = std::fs::read_to_string("/home/antan/Projects/advent-of-code/rust2024/input/day3.txt").unwrap();

  let re = Regex::new(r"mul\([\d]+,[\d]+\)");
  if re.is_err() {
    println!("fuck")
  }

  let apa = re.unwrap();

  let res = apa.find_iter(&result);

  let mut score = 0;
  for r in res {
    let v: Vec<&str> = r.as_str().split(",").clone().collect();

    let a: i32 = v[0].replace("mul(", "").parse().unwrap();
    let b: i32 = v[1].replace(")", "").parse().unwrap();
    score += a * b;
  }

  // 175015740 right on
  println!("Day 3 A: {}", score);
}