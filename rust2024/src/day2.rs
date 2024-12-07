pub fn day2a(path: &str) {
  let s = std::fs::read_to_string(path);
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
    let matching = list.iter().zip(&sorted_list).filter(|&(a, b)| a == b).count() == list.len();

    if matching {
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
      let matching = list.iter().zip(sorted_list).filter(|&(a, b)| *a == b).count() == list.len();

      if matching {
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

pub fn day2b(path: &str) {
  let s = std::fs::read_to_string(path);
  if s.is_err() {
    println!("input returned error");
    return;
  }

  let result = s.unwrap();
  let input = result
    .split("\n")
    .clone();

  let mut score = 0;

  for row in input {
    //println!("{}", row);
    let mut levels: Vec<i32> = row.split(" ").map(|s| s.parse().unwrap()).collect();

    let mut error_counter = 0;
    let mut direction = 0;

    // get general direction of levels
    for (i, level) in levels.iter().enumerate() {
      if i + 1 == levels.len() {
        break;
      }

      if levels[i + 1] < *level {
        direction -= 1;
      }
      else if levels[i + 1] > *level {
        direction += 1;
      }
    }

    if direction == 0 {
      continue;
    }

    let mut indexes_of_bad_levels: Vec<usize> = vec![];
    // check for errors in the levels
    if direction > 0 {
      for (i, level) in levels.iter().enumerate() {
        if i + 1 == levels.len() {
          break;
        }

        if levels[i+1] == *level {
          indexes_of_bad_levels.insert(0, i);
          continue;
        }
        else if levels[i+1] - *level > 3 || levels[i+1] - *level < 1 {
          indexes_of_bad_levels.insert(0, i);
          continue;
        }
      }
    }
    else {
      for (i, level) in levels.iter().enumerate() {
        if i + 1 == levels.len() {
          break;
        }

        if levels[i+1] == *level {
          indexes_of_bad_levels.insert(0, i);
          continue;
        }
        else if *level - levels[i+1] > 3 || *level - levels[i+1] < 1 {
          indexes_of_bad_levels.insert(0, i);
          continue;
        }
      }
    }

    //println!("{}", indexes_of_bad_levels.len());

    if indexes_of_bad_levels.len() == 1 {
      levels.remove(indexes_of_bad_levels[0]);
    }
    else if indexes_of_bad_levels.len() > 1 {
      error_counter = 10;
    }

    if direction > 0 {
      for (i, level) in levels.iter().enumerate() {
        if i + 1 == levels.len() {
          break;
        }

        if levels[i+1] == *level {
          error_counter += 1;
          continue;
        }
        else if levels[i+1] - *level > 3 || levels[i+1] - *level < 1 {
          error_counter += 1;
          continue;
        }
      }
    }
    else {
      for (i, level) in levels.iter().enumerate() {
        if i + 1 == levels.len() {
          break;
        }

        if levels[i+1] == *level {
          error_counter += 1;
          continue;
        }
        else if *level - levels[i+1] > 3 || *level - levels[i+1] < 1 {
          error_counter += 1;
          continue;
        }
      }
    }

    for level in levels {
      //print!("{} ", level);
    }
    //println!("");

    if error_counter < 2 {
      //println!("VALID");
      score += 1;
    }
  }

  // 680 too high
  // 374 too high
  println!("Day 2 B: {score}");
}