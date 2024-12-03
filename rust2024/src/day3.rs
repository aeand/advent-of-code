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

pub fn day3b() {
  let input = std::fs::read_to_string("/home/antan/Projects/advent-of-code/rust2024/input/day3.txt").unwrap();
  let re = Regex::new(r"mul\([\d]+,[\d]+\)").unwrap();
  let regex = re.find_iter(&input);

  let mut indexes_of_dos: Vec<usize> = input.as_str().match_indices("do()").map(|a| a.0).collect();
  indexes_of_dos.reverse();
  let mut indexes_of_donts: Vec<usize> = input.as_str().match_indices("don't()").map(|a| a.0).collect();
  indexes_of_donts.reverse();

  let mut score = 0;
  let mut indexes_of_matches: Vec<usize> = vec![];
  let mut current_active_do = true;

  for r in regex {
    let index_of_r: Vec<usize> = input.as_str().match_indices(r.as_str()).map(|a| a.0).collect();
    indexes_of_matches.insert(0, index_of_r[0]);
    let a = indexes_of_dos.iter().enumerate().find(|s| *s.1 < index_of_r[0]);
    let b = indexes_of_donts.iter().enumerate().find(|s| *s.1 < index_of_r[0]);
    let c = indexes_of_matches.iter().enumerate().find(|s| *s.1 < index_of_r[0]);
    let mut latest_modifier: Vec<(&usize, bool)> = vec![];
    if !a.is_none() {
      latest_modifier.insert(0, (a.unwrap().1, true));
    }
    if !b.is_none() {
      latest_modifier.insert(0, (b.unwrap().1, false));
    }
    if !c.is_none() {
      latest_modifier.insert(0, (c.unwrap().1, current_active_do));
    }

    if latest_modifier.len() > 0 {
      latest_modifier.sort_by(|a, b| b.0.cmp(a.0));

      current_active_do = latest_modifier[0].1;
    }

    if current_active_do {
      let v: Vec<&str> = r.as_str().split(",").clone().collect();

      score +=
        v[0].replace("mul(", "").parse::<i32>().unwrap()
        * v[1].replace(")", "").parse::<i32>().unwrap();
    }
  }

  // 112272912 right on
  println!("Day 3 B: {}", score);
}