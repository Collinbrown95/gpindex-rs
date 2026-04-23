use ndarray::ArrayView1;

/// Calculates the average of a 1D array view.
pub fn calculate_average(data: ArrayView1<f64>) -> f64 {
    if data.is_empty() { 0.0 } else { data.sum() / data.len() as f64 }
}

pub fn calculate_geometric_mean(data: ArrayView1<f64>) -> f64 {
    if data.is_empty() {
        return 0.0;
    }
    
    // 1. log(x) -> mapv applies the function to each element
    // 2. .sum()  -> adds them up
    let sum_logs: f64 = data.mapv(|x| x.ln()).sum();
    
    // 3. exp(sum / length)
    (sum_logs / data.len() as f64).exp()
}