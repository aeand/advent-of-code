pub fn day4(path: &str) {
  day4a(path);
  day4b(path);
}

fn day4a(path: &str) {
  let input = std::fs::read_to_string(path).unwrap();
  let size: usize = input.split("\n").count();
  let mut matches = 0;

  // horizontal
  matches += input.matches("XMAS").count() + input.matches("SAMX").count();

  // vertical
  let mut columns: String = "".to_string();
  for i in 0..size {
    let mut rows_reverted: Vec<&str> = input.split("\n").collect();
    rows_reverted.reverse();
    for row in rows_reverted {
      let row_chars: Vec<char> = row.chars().collect();
      columns = format!("{}{}", columns, row_chars[i].to_string());
    }

    if !(i+1 == size) {
      columns = format!("{}{}", columns, "\n");
    }
  }

  matches += columns.matches("XMAS").count() + columns.matches("SAMX").count();

  // diagonal
  let mut diagonals: String = "".to_string();

  let rows: Vec<&str> = input.split("\n").collect();
  let size: usize = rows.len();
  diagonals = format!("{}{}", diagonals, check_top_diagonal(rows, size));

  let mut rows_reversed: Vec<&str> = input.split("\n").collect();
  rows_reversed.reverse();
  diagonals = format!("{}{}", diagonals, check_bottom_diagonal(rows_reversed, size));

  matches += diagonals.matches("XMAS").count() + diagonals.matches("SAMX").count();

  // 2688 too low
  // 2716 too lows
  // 2718 right on
  println!("Day 4 A: {}", matches);
}

fn check_top_diagonal(input: Vec<&str>, size: usize) -> String {
  let mut all_diagonals: String = "".to_string();

  for x in 0..size {
    let mut diagonal = "".to_string();

    for y in 0..size {
      if y > size-1 || x+y > size-1 {
        break;
      }

      let chars: Vec<char> = input[y].chars().collect();
      diagonal = format!("{}{}", diagonal, chars[x+y].to_string());
    }

    if diagonal.len() >= 4 {
      diagonal = format!("{}{}", diagonal, "\n");
      all_diagonals = format!("{}{}", all_diagonals, diagonal);
    }
  }

  for x in 0..size {
    let mut diagonal = "".to_string();
    for y in 0..x+1 {
      if x-y > x {
        break;
      }

      let chars: Vec<char> = input[y].chars().collect();
      diagonal = format!("{}{}", diagonal, chars[x-y].to_string());
    }

    if diagonal.len() >= 4 {
      diagonal = format!("{}{}", diagonal, "\n");
      all_diagonals = format!("{}{}", all_diagonals, diagonal);
    }
  }

  return all_diagonals;
}

fn check_bottom_diagonal(input: Vec<&str>, size: usize) -> String {
  let mut all_diagonals: String = "".to_string();

  for x in 1..size {
    let mut diagonal = "".to_string();

    for y in 0..size {
      if y > size-1 || x+y > size-1 {
        break;
      }

      let chars: Vec<char> = input[y].chars().collect();
      diagonal = format!("{}{}", diagonal, chars[x+y].to_string());
    }

    if diagonal.len() >= 4 {
      diagonal = format!("{}{}", diagonal, "\n");
      all_diagonals = format!("{}{}", all_diagonals, diagonal);
    }
  }

  for x in 0..size-1 {
    let mut diagonal = "".to_string();
    for y in 0..x+1 {
      if x-y > x {
        break;
      }

      let chars: Vec<char> = input[y].chars().collect();
      diagonal = format!("{}{}", diagonal, chars[x-y].to_string());
    }

    if diagonal.len() >= 4 {
      diagonal = format!("{}{}", diagonal, "\n");
      all_diagonals = format!("{}{}", all_diagonals, diagonal);
    }
  }

  return all_diagonals;
}

fn day4b(path: &str) {
  let input = std::fs::read_to_string(path).unwrap();

  let mut x_mas_counter = 0;

  let mut coordinate_system: Vec<(i32, i32, char)> = vec![];
  for (y, row) in input.split("\n").enumerate() {
    for (x, c) in row.chars().enumerate() {
      coordinate_system.insert(coordinate_system.len(), (x.try_into().unwrap(), y.try_into().unwrap(), c));
    }
  }

  let all_a: Vec<(i32, i32, char)> = coordinate_system.iter().map(|v| *v).filter(|v| v.2 == 'A').collect();

  for i in all_a.iter() {
    let top_left = coordinate_system.iter().find(|v| v.0 == i.0 - 1 && v.1 == i.1 - 1);
    let top_right = coordinate_system.iter().find(|v| v.0 == i.0 + 1 && v.1 == i.1 - 1);
    let bot_left = coordinate_system.iter().find(|v| v.0 == i.0 - 1 && v.1 == i.1 + 1);
    let bot_right = coordinate_system.iter().find(|v| v.0 == i.0 + 1 && v.1 == i.1 + 1);

    if top_left.is_none() || top_right.is_none() || bot_left.is_none() || bot_right.is_none() {
      continue;
    }

    let mut match_one: String = "".to_string();
    match_one.push(top_left.unwrap().2);
    match_one.push('A');
    match_one.push(bot_right.unwrap().2);

    let mut match_two: String = "".to_string();
    match_two.push(top_right.unwrap().2);
    match_two.push('A');
    match_two.push(bot_left.unwrap().2);

    if (match_one.matches("MAS").count() > 0 || match_one.matches("SAM").count() > 0) && (match_two.matches("MAS").count() > 0 || match_two.matches("SAM").count() > 0) {
      x_mas_counter += 1;
    }
  }

  // 2046 right on
  println!("Day 4 B: {}", x_mas_counter);
}