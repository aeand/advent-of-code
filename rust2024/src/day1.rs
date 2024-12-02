pub fn day1a() {
  let result = std::fs::read_to_string("../input/day1.txt").unwrap();
  let input = result
      .split("\n")
      .clone();

  let mut list_one: Vec<i32> = std::vec![];
  let mut list_two: Vec<i32> = std::vec![];

  for row in input {
      let locations: Vec<&str> = row.split("   ").collect();
      list_one.insert(
          0,
          locations.first().unwrap().to_string().parse().unwrap(),
      );
      list_two.insert(
          list_two.len(),
          locations.last().unwrap().to_string().parse().unwrap(),
      );
  }

  list_one.sort();
  list_two.sort();

  let mut distance: i32 = 0;
  for (i, el) in list_one.iter().enumerate() {
      if el > &list_two[i] {
          distance += el - list_two[i];
      }
      else {
          distance += list_two[i] - el;
      }
  }

  println!("Day 1 A: {}", distance);

  // 29310557 too high
  // 1273683 too low
  // 1579939 right on
}

pub fn day1b() {
  let result = std::fs::read_to_string("../input/day1.txt").unwrap();
  let input = result
      .split("\n")
      .clone();

  let mut list_one: Vec<i32> = std::vec![];
  let mut list_two: Vec<i32> = std::vec![];

  for row in input {
      let locations: Vec<&str> = row.split("   ").collect();
      list_one.insert(
          0,
          locations.first().unwrap().to_string().parse().unwrap(),
      );
      list_two.insert(
          0,
          locations.last().unwrap().to_string().parse().unwrap(),
      );
  }

  let mut similarity_score: i32 = 0;
  for i in list_one {
      let mut counter = 0;

      for j in &list_two {
          if i == *j {
              counter += 1;
          }
      }

      similarity_score += i * counter;
  }

  println!("Day 1 B: {}", similarity_score);
  // 20351745 right on
}