fn main() {
    day1a();
}

fn day1a() {
    let result = std::fs::read_to_string("../input/day1.txt").unwrap();

    let input = result
        .split("\n")
        .clone();

    let mut list_one = std::vec![];
    let mut list_two = std::vec![];

    for row in input {
        let locations: Vec<&str> = row.split("   ").collect();

        let first: i32 = locations.first().unwrap().to_string().parse().unwrap();
        let second: i32 = locations.last().unwrap().to_string().parse().unwrap();

        list_one.insert(list_one.len(), first);
        list_two.insert(list_two.len(), second);
    }

    // sort lists
    list_one.sort();
    list_two.sort();

    let mut distance_counter: i32 = 0;
    for (index, element) in list_one.iter().enumerate() {
        // solve puzzle
        if element > &list_two[index] {
            distance_counter += element - list_two[index];
        }
        else {
            distance_counter += list_two[index] - element;
        }
    }

    // 29310557 too high
    // 1273683 too low
    // 1579939 right on
}