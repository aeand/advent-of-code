pub fn day5(path: &str) {
  day5a(path);
}

fn day5a(path: &str) {
  let input = std::fs::read_to_string(path).unwrap();

  let mut divided_input = input.split("\n\n");
  let page_ordering_rules = divided_input.nth(0).unwrap();
  let page_updates = divided_input.last().unwrap();

  let mut page_ordering_table: Vec<(usize, Vec<usize>)> = vec![];
  for row in page_ordering_rules.split("\n") {
    page_ordering_table.insert(0, (row.split("|").nth(0).unwrap().parse().unwrap(), vec![]));
  }

  for row in page_ordering_rules.split("\n") {
    let key: usize = row.split("|").nth(0).unwrap().parse().unwrap();
    let value: usize = row.split("|").last().unwrap().parse().unwrap();
    let page_position = page_ordering_table.iter().position(|i| i.0 == key).unwrap();
    page_ordering_table[page_position].1.insert(0, value);
  }

  let mut is_correct = true;
  let mut result = 0;
  for row in page_updates.split("\n") {
    let pages: Vec<usize> = row.split(",").map(|c| c.parse().unwrap()).collect();
    for (i, page) in pages.iter().enumerate() {
      let selected_page = page_ordering_table.iter().find(|p| p.0 == *page);

      for behind_index in (0..i).rev() {
        let a = page_ordering_table.iter().find(|p| p.0 == pages[behind_index]);
        if a.is_none() {
          is_correct = false;
        }

        let b = a.unwrap().1.iter().find(|p: &&usize| *p == page);
        if b.is_none() {
          is_correct = false;
        }
      }

      for forward_index in i+1..row.split(",").count() {
        if selected_page.is_none() && i == row.split(",").count()-1 {
          break;
        }
        else if selected_page.is_none() {
          is_correct = false;
          break;
        }

        let b = selected_page.unwrap().1.iter().find(|p| **p == pages[forward_index]);
        if b.is_none() {
          is_correct = false;
        }
      }
    }

    if is_correct {
      let index = (pages.len() / 2) as f64 + 0.5;
      result += pages[index as usize];
    }

    is_correct = true;
  }

  // 6041 right on
  println!("Day 5 A: {}", result);
}