use std::cmp::min;
use std::fs::File;
use std::io::{prelude::*, BufReader};

fn part1() -> std::io::Result<i32> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut total_needed = 0;
    for line in reader.lines() {
        let dims = line
            .unwrap()
            .split("x")
            .collect::<Vec<&str>>()
            .into_iter()
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();

        let lw = dims[0] * dims[1];
        let wh = dims[1] * dims[2];
        let lh = dims[0] * dims[2];

        let smallest = min(min(lw, wh), lh);

        total_needed += 2 * lw + 2 * wh + 2 * lh + smallest;
    }

    Ok(total_needed)
}

fn part2() -> std::io::Result<i32> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut total_needed = 0;
    for line in reader.lines() {
        // let dim_str = line?;
        let mut dims = line
            .unwrap()
            .split("x")
            .collect::<Vec<&str>>()
            .into_iter()
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        dims.sort();

        let perim = 2 * dims[0] + 2*dims[1];
        let vol: i32 = dims.into_iter().product();

        total_needed += perim + vol;
    }

    Ok(total_needed)
}

fn main() -> std::io::Result<()> {
    println!("{}", part1()?);
    println!("{}", part2()?);

    Ok(())
}
