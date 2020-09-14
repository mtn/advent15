use std::collections::HashMap;
use std::fs::File;
use std::io::{prelude::*, BufReader};

fn part1() -> std::io::Result<i32> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    const BAD_PAIRS: [(char, char); 4] = [('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')];
    let vowel_str = String::from("aeiou");

    let mut good_strings = 0;
    for line in reader.lines() {
        let line = line?;

        let mut vowel_count = 0;
        let mut repeated_letter = false;
        let mut bad_pair = false;
        for (a, b) in line.chars().zip(line.chars().skip(1)) {
            for (p1, p2) in BAD_PAIRS.iter() {
                if a == *p1 && b == *p2 {
                    bad_pair = true;
                    break;
                }
            }

            if bad_pair {
                break;
            }

            if a == b {
                repeated_letter = true;
            }

            if vowel_str.contains(a) {
                vowel_count += 1;
            }
        }

        if vowel_str.contains(line.chars().last().unwrap()) {
            vowel_count += 1;
        }

        if vowel_count >= 3 && !bad_pair && repeated_letter {
            // println!("{}", line);
            good_strings += 1;
        }
    }

    Ok(good_strings)
}

fn part2() -> std::io::Result<i32> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut good_strings = 0;
    let mut pair_inds: HashMap<(char, char), usize> = HashMap::new();
    for line in reader.lines() {
        let line = line?;

        let mut spaced_repeat = false;
        let mut repeating_pair = false;
        for (a, c) in line.chars().zip(line.chars().skip(2)) {
            if a == c {
                spaced_repeat = true;
            }
        }

        for (i, (a, b)) in line.chars().zip(line.chars().skip(1)).enumerate() {
            if pair_inds.contains_key(&(a, b)) {
                if pair_inds[&(a, b)] + 1 < i {
                    repeating_pair = true;
                }
            } else {
                pair_inds.insert((a, b), i);
            }
        }

        if spaced_repeat && repeating_pair {
            good_strings += 1;
        }
        pair_inds.drain();
    }

    Ok(good_strings)
}

fn main() -> std::io::Result<()> {
    println!("{}", part1()?);
    println!("{}", part2()?);

    Ok(())
}
