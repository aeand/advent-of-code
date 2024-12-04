use std::collections::btree_map::Keys;

pub fn day4a() {
  let input = std::fs::read_to_string("/home/antan/Projects/advent-of-code/rust2024/input/day4.txt").unwrap();
  let size: usize = input.split("\n").count();
  let mut matches = 0;

  // horizontal
  matches += input.matches("XMAS").count() + input.matches("SAMX").count();

  // vertical
  let mut columns: String = "".to_string();
  for i in 0..size {
    for row in input.split("\n") {
      let chars: Vec<char> = row.chars().collect();
      columns = format!("{}{}", columns, chars[i].to_string());
    }
    columns = format!("{}{}", columns, "\n");
  }

  matches += columns.matches("XMAS").count() + columns.matches("SAMX").count();

  // diagonal
  let rows: Vec<&str> = input.split("\n").collect();
  let mut diagonals: String = "".to_string();

  // check top row, down right

  // loop len of row chars
  for i in 0..size {
    let mut stri = "".to_string();
    let x = i;
    let y = 0;

    // loop right down until out of bounds
    for j in 0..size {
      // if index is out of bounds, check string len
      if y+j > size-1 || x+j > size-1 {
        break;
      }

      // add 1 to coordinates to travel down right
      let ch: Vec<char> = rows[y+j].chars().collect();
      // add char to string
      stri = format!("{}{}", stri, ch[x+j].to_string());
    }

    // if len >= 4, add to total_string + \n
    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      diagonals = format!("{}{}", diagonals, stri);
    }
  }
  println!("points!: {}", diagonals.matches("XMAS").count() + diagonals.matches("SAMX").count());
  diagonals = "".to_string();

  // check top row, down left

  // loop len of row chars
  for i in (0..size).rev() {
    let mut stri = "".to_string();
    let x = i;
    let y = 0;

    // loop right down until out of bounds
    for j in 0..i {
      // if index is out of bounds, check string len
      if /* j-y < 0 || */ x-j > i {
        break;
      }

      // add 1 to coordinates to travel down right
      let ch: Vec<char> = rows[j-y].chars().collect();
      // add char to string
      stri = format!("{}{}", stri, ch[x-j].to_string());
    }

    // if len >= 4, add to total_string + \n
    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      diagonals = format!("{}{}", diagonals, stri);
    }
  }
  println!("points!: {}", diagonals.matches("XMAS").count() + diagonals.matches("SAMX").count());
  diagonals = "".to_string();

  // check left column down right
  /* // loop len of row chars
  for i in 0..size {
    let mut stri = "".to_string();
    let x = i;
    let y = 0;

    // loop right down until out of bounds
    for j in 0..size {
      // if index is out of bounds, check string len
      if y+j > size-1 || x+j > size-1 {
        break;
      }

      // add 1 to coordinates to travel down right
      let ch: Vec<char> = rows[y+j].chars().collect();
      // add char to string
      stri = format!("{}{}", stri, ch[x+j].to_string());
    }

    // if len >= 4, add to total_string + \n
    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      diagonals = format!("{}{}", diagonals, stri);
    }
  }
  println!("points!: {}", diagonals.matches("XMAS").count() + diagonals.matches("SAMX").count());
  diagonals = "".to_string(); */

  // check left column up right
  /* // loop len of row chars
  for i in 0..size {
    let mut stri = "".to_string();
    let x = i;
    let y = 0;

    // loop right down until out of bounds
    for j in 0..size {
      // if index is out of bounds, check string len
      if y+j > size-1 || x+j > size-1 {
        break;
      }

      // add 1 to coordinates to travel down right
      let ch: Vec<char> = rows[y+j].chars().collect();
      // add char to string
      stri = format!("{}{}", stri, ch[x+j].to_string());
    }

    // if len >= 4, add to total_string + \n
    if stri.len() >= 4 {
      stri = format!("{}{}", stri, "\n");
      diagonals = format!("{}{}", diagonals, stri);
    }
  }
  println!("points!: {}", diagonals.matches("XMAS").count() + diagonals.matches("SAMX").count());
  diagonals = "".to_string(); */

  // helper note!! remove diagonals = "" when done 

  println!("Day 4 A: {}", matches);
}