use std::fs::File;
use std::io::prelude::*;

fn part1() -> std::io::Result<i32> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut floor: i32 = 0;
    for (_, c) in contents.chars().enumerate() {
        if c == '(' {
            floor += 1;
        } else {
            floor -= 1;
        }
    }

    Ok(floor)
}

fn part2() -> std::io::Result<i32> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut floor: i32 = 0;
    for (i, c) in contents.chars().enumerate() {
        if c == '(' {
            floor += 1;
        } else {
            floor -= 1;
        }

        if floor == -1 {
            return Ok((i + 1) as i32);
        }
    }

    panic!("Didn't ever reach a negative floor")
}

fn main() -> std::io::Result<()> {
    println!("{}", part1()?);
    println!("{}", part2()?);

    Ok(())
}
