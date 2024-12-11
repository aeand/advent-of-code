pub fn day5(path: &str) {
  day5a(path);
  day5b(path);
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
          break;
        }

        let b = a.unwrap().1.iter().find(|p: &&usize| *p == page);
        if b.is_none() {
          is_correct = false;
          break;
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
          break;
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

fn day5b(path: &str) {
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
  let mut incorrectly_ordered_updates: Vec<Vec<usize>> = vec![];
  for row in page_updates.split("\n") {
    let pages: Vec<usize> = row.split(",").map(|c| c.parse().unwrap()).collect();
    for (i, page) in pages.iter().enumerate() {
      let selected_page = page_ordering_table.iter().find(|p| p.0 == *page);

      for behind_index in (0..i).rev() {
        let a = page_ordering_table.iter().find(|p| p.0 == pages[behind_index]);
        if a.is_none() {
          is_correct = false;
          break;
        }

        let b = a.unwrap().1.iter().find(|p: &&usize| *p == page);
        if b.is_none() {
          is_correct = false;
          break;
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
          break;
        }
      }
    }

    if !is_correct {
      incorrectly_ordered_updates.insert(incorrectly_ordered_updates.len(), pages);
    }

    is_correct = true;
  }

  let mut result = 0;
  for mut update in incorrectly_ordered_updates {
    loop {
      let mut swapped = false;

      let mut i = 0;
      while i < update.len() {
        if i >= update.len()-1 { break; }

        let item_in_table = page_ordering_table.iter().find(|p| p.0 == update[i]);

        if item_in_table.is_none() {
          swapped = true;
          let value = update[i];
          update.remove(i);
          update.insert(i+1, value);
          break;
        }
        else {
          let is_next_val_in_items_list = item_in_table.unwrap().1.iter().find(|p| **p == update[i+1]); // xD
          if is_next_val_in_items_list.is_none() {
            swapped = true;
            let value = update[i];
            update.remove(i);
            update.insert(i+1, value);
            break;
          }
        }

        i += 1;
      }

      if !swapped { break; }
    }

    let index = (update.len() / 2) as f64 + 0.5;
    result += update[index as usize];
  }

  // 4884 right on
  println!("Day 5 B: {}", result);
}