use std::collections::HashSet;
use std::fs::File;
use std::io::prelude::*;

fn part1() -> std::io::Result<i32> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut x = 0;
    let mut y = 0;
    let mut visited = HashSet::new();
    visited.insert((x, y));

    for c in contents.chars() {
        if c == '^' {
            y -= 1;
        } else if c == 'v' {
            y += 1;
        } else if c == '<' {
            x -= 1;
        } else {
            x += 1;
        }

        visited.insert((x, y));
    }

    Ok(visited.len() as i32)
}

fn part2() -> std::io::Result<i32> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut x = 0;
    let mut y = 0;
    let mut rx = 0;
    let mut ry = 0;
    let mut visited = HashSet::new();
    visited.insert((x, y));

    for (i, c) in contents.chars().enumerate() {
        if i % 2 == 0 {
            if c == '^' {
                y -= 1;
            } else if c == 'v' {
                y += 1;
            } else if c == '<' {
                x -= 1;
            } else {
                x += 1;
            }
            visited.insert((x, y));
        } else {
            if c == '^' {
                ry -= 1;
            } else if c == 'v' {
                ry += 1;
            } else if c == '<' {
                rx -= 1;
            } else {
                rx += 1;
            }
            visited.insert((rx, ry));
        }
    }

    Ok(visited.len() as i32)
}

fn main() -> std::io::Result<()> {
    println!("{}", part1()?);
    println!("{}", part2()?);

    Ok(())
}
