fn main() {
    let result = std::fs::read_to_string("input.txt").unwrap();
    let split = result.split("\n");
    split.clone().for_each(print);
    let lol = split.map(delete_first);
    lol.for_each(other_print);
}

fn delete_first(input: &str) -> String {
    if input.is_empty() {
        return String::new();
    }

    let first_char: char = input.chars().nth(0).unwrap();
    return input.replace(first_char, "");
}

fn print(text: &str) {
    println!("{text}");
}

fn other_print(text: String) {
    println!("{text}");
}