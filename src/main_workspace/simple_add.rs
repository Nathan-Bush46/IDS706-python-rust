use std::time::Instant;

fn sum_of_squares(numbers: &[i32]) -> i64 {
    numbers.iter().map(|&x| (x as i64) * (x as i64)).sum()
}

fn main() {
    // Sample data
    let numbers: Vec<i32> = (1..1_000_000).collect();

    // Timing the function
    let start_time = Instant::now();
    let result = sum_of_squares(&numbers);
    let duration = start_time.elapsed();

    println!("Sum of squares: {}", result);
    println!("Time taken (seconds): {:.6}", duration.as_secs_f64());
}
