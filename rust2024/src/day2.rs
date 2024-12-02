pub fn day2a() {
  let s = std::fs::read_to_string("/home/antan/Projects/advent-of-code/rust2024/input/day2.txt");
  if s.is_err() {
    println!("input returned error");
    return;
  }

  let result = s.unwrap();
  let input = result
    .split("\n")
    .clone();

  let mut counter = 0;

  for row in input {
    let mut is_row_valid = true;
    let list: Vec<i32> = row.split(" ").map(|s| s.parse().unwrap()).collect();
    let mut sorted_list: Vec<i32> = list.clone();

    sorted_list.sort();

    let matching = list.iter().zip(&sorted_list).filter(|&(a, b)| a == b).count();

    if matching == list.len() {
      let mut previous_i = list[0];
      for (index, i) in list.iter().enumerate() {
        if index == 0 {
          continue;
        }

        if i - previous_i <= 3 && previous_i != *i {
          previous_i = *i;
        }
        else {
          is_row_valid = false;
        }
      }
    }
    else {
      sorted_list.reverse();
      let matching = list.iter().zip(sorted_list).filter(|&(a, b)| *a == b).count();

      if matching == list.len() {
        let mut previous_i = list[0];
        for (index, i) in list.iter().enumerate() {
          if index == 0 {
            continue;
          }

          if previous_i - i <= 3 && previous_i != *i {
            previous_i = *i;
          }
          else {
            is_row_valid = false;
          }
        }
      }
      else {
        is_row_valid = false;
      }
    }

    if is_row_valid {
      counter += 1;
    }
  }

  // 384 too high
  // 192 too low
  // 306 right on
  println!("Day 2 A: {counter}");
}

pub fn day2b() {
  let s = std::fs::read_to_string("/home/antan/Projects/advent-of-code/rust2024/input/day2.txt");
  if s.is_err() {
    println!("input returned error");
    return;
  }

  let result = s.unwrap();
  let input = result
    .split("\n")
    .clone();

  let mut counter = 0;

  for row in input {
    let mut is_row_valid = 0;
    let list: Vec<i32> = row.split(" ").map(|s| s.parse().unwrap()).collect();
    let mut sorted_list: Vec<i32> = list.clone();

    sorted_list.sort();

    let matching = list.iter().zip(&sorted_list).filter(|&(a, b)| a == b).count();

    if matching == list.len() || matching == list.len() - 1 {
      is_row_valid += list.len() - matching;

      let mut previous_i = list[0];
      for (index, i) in list.iter().enumerate() {
        if index == 0 {
          continue;
        }

        if i - previous_i <= 3 && previous_i != *i {
          previous_i = *i;
        }
        else {
          is_row_valid += 1;
        }
      }
    }
    else {
      sorted_list.reverse();
      let matching = list.iter().zip(sorted_list).filter(|&(a, b)| *a == b).count();

      if matching == list.len() || matching == list.len() - 1 {
        is_row_valid += list.len() - matching;

        if matching == list.len() {
          let mut previous_i = list[0];
          for (index, i) in list.iter().enumerate() {
            if index == 0 {
              continue;
            }

            if previous_i - i <= 3 && previous_i != *i {
              previous_i = *i;
            }
            else {
              is_row_valid += 1;
            }
          }
        }
        else {
          is_row_valid += 1;
        }
      }
    }

    if is_row_valid < 2 {
      counter += 1;
    }
  }

  // 680 too high
  println!("Day 2 A: {counter}");
}