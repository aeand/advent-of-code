pub fn day2a(path: &str) {
  let result = std::fs::read_to_string(path).unwrap();
  let input = result.split("\n").clone();

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
  let result = std::fs::read_to_string(path).unwrap();
  let input = result.split("\n").clone();

  let mut safe_levels = 0;

  for row in input {
    let mut direction = 0;
    let mut is_unsafe = false;
    let mut incorrect_indexes: Vec<usize> = vec![];

    let mut levels: Vec<i32> = vec![];
    for a in row.split(" ") {
      levels.insert(levels.len(), a.parse::<i32>().unwrap());
    }

    for (i, level) in levels.iter().enumerate() {
      let j = (i+1).clamp(0, levels.len()-1);

      if level < &levels[j] {
        if direction != 0 && direction < 0 {
          is_unsafe = true;
          incorrect_indexes.insert(incorrect_indexes.len(), i);
        }

        if levels[j] - level > 3 {
          is_unsafe = true;
          incorrect_indexes.insert(incorrect_indexes.len(), i);
        }

        direction = (direction + 2).clamp(-1, 1);
      }
      else if level > &levels[j] {
        if direction != 0 && direction > 0 {
          is_unsafe = true;
          incorrect_indexes.insert(incorrect_indexes.len(), i);
        }

        if level - levels[j] > 3 {
          is_unsafe = true;
          incorrect_indexes.insert(incorrect_indexes.len(), i);
        }

        direction = (direction - 2).clamp(-1, 1);
      }
      else if i != j {
          is_unsafe = true;
          incorrect_indexes.insert(incorrect_indexes.len(), i);
      }
    }

    if is_unsafe {
      let mut unsafe_counter = 0;
      for ind in 0..row.chars().count() {
        println!("{ind}");

        is_unsafe = false;
        direction = 0;

        let mut levels_changed: Vec<i32> = vec![];
        for (index, a) in row.split(" ").enumerate() {
          if index != ind {
            levels_changed.insert(levels_changed.len(), a.parse().unwrap());
          }
        }

        for (i, level_changed) in levels_changed.iter().enumerate() {
          let j = (i+1).clamp(0, levels_changed.len()-1);

          if level_changed < &levels_changed[j] {
            if direction != 0 && direction < 0 {
              is_unsafe = true;
            }

            if levels_changed[j] - level_changed > 3 {
              is_unsafe = true;
            }

            direction = (direction + 2).clamp(-1, 1);
          }
          else if level_changed > &levels_changed[j] {
            if direction != 0 && direction > 0 {
              is_unsafe = true;
            }

            if level_changed - levels_changed[j] > 3 {
              is_unsafe = true;
            }

            direction = (direction - 2).clamp(-1, 1);
          }
          else if i != j {
            is_unsafe = true;
          }
        }

        if is_unsafe {
          unsafe_counter += 1;
        }
      }

      if unsafe_counter < row.chars().count() {
        is_unsafe = false;
      }
    }

    if is_unsafe {
      continue;
    }

    safe_levels += 1;
  }

  // 680 too high
  // 374 too high
  // 344 too low
  println!("Day 2 B: {safe_levels}");
}