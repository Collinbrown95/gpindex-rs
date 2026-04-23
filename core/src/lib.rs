use ndarray::ArrayView1;

/// Calculates the average of a 1D array view.
pub fn calculate_average(data: ArrayView1<f64>) -> f64 {
    if data.is_empty() { 0.0 } else { data.sum() / data.len() as f64 }
}
