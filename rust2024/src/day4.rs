pub fn day4a() {
  let input = std::fs::read_to_string("/home/antan/Projects/advent-of-code/rust2024/input/day4.txt").unwrap();
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
      let chars: Vec<char> = row.chars().collect();
      columns = format!("{}{}", columns, chars[i].to_string());
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
  let mut result: String = "".to_string();

  for x in 0..size {
    let mut stri = "".to_string();

    for y in 0..size {
      if y > size-1 || x+y > size-1 {
        break;
      }

      let ch: Vec<char> = input[y].chars().collect();
      stri = format!("{}{}", stri, ch[x+y].to_string());
    }

    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      result = format!("{}{}", result, stri);
    }
  }

  for x in 0..size {
    let mut stri = "".to_string();
    for y in 0..x+1 {
      if x-y > x {
        break;
      }

      let ch: Vec<char> = input[y].chars().collect();
      stri = format!("{}{}", stri, ch[x-y].to_string());
    }

    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      result = format!("{}{}", result, stri);
    }
  }

  return result;
}

fn check_bottom_diagonal(input: Vec<&str>, size: usize) -> String {
  let mut result: String = "".to_string();

  for x in 1..size {
    let mut stri = "".to_string();

    for y in 0..size {
      if y > size-1 || x+y > size-1 {
        break;
      }

      let ch: Vec<char> = input[y].chars().collect();
      stri = format!("{}{}", stri, ch[x+y].to_string());
    }

    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      result = format!("{}{}", result, stri);
    }
  }

  for x in 0..size-1 {
    let mut stri = "".to_string();
    for y in 0..x+1 {
      if x-y > x {
        break;
      }

      let ch: Vec<char> = input[y].chars().collect();
      stri = format!("{}{}", stri, ch[x-y].to_string());
    }

    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      result = format!("{}{}", result, stri);
    }
  }

  return result;
}