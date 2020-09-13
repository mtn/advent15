use md5;

fn part1(secret: &str) -> u64 {
    let secret = secret.to_owned();

    for i in 0..std::u64::MAX {
        let mut byte_str = secret.clone();
        byte_str.push_str(&i.to_string());
        let byte_str = byte_str.as_bytes();

        let hash = md5::compute(byte_str);

        if hash[0] as i32 + hash[1] as i32 + (hash[2] >> 4) as i32 == 0 {
            return i;
        }
    }

    panic!("Didn't find a number");
}

fn part2(secret: &str) -> u64 {
    let secret = secret.to_owned();

    for i in 0..std::u64::MAX {
        let mut byte_str = secret.clone();
        byte_str.push_str(&i.to_string());
        let byte_str = byte_str.as_bytes();

        let hash = md5::compute(byte_str);

        if hash[0] as i32 + hash[1] as i32 + hash[2] as i32 == 0 {
            return i;
        }
    }

    panic!("Didn't find a number");
}


fn main() -> std::io::Result<()> {
    const SECRET: &str = "yzbqklnj";

    println!("{}", part1(SECRET));
    println!("{}", part2(SECRET));

    Ok(())
}
