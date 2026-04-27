use ndarray::{ArrayView1, Array2};
use crate::means::{arithmetic_mean, geometric_mean};

pub fn carli_index(p1: ArrayView1<f64>, p0: ArrayView1<f64>) -> f64 {
    let relatives = calculate_relatives(p1, p0);
    arithmetic_mean(ArrayView1::from(&relatives))
}

pub fn jevons_index(p1: ArrayView1<f64>, p0: ArrayView1<f64>) -> f64 {
    
    let relatives = calculate_relatives(p1, p0);
    geometric_mean(ArrayView1::from(&relatives))
}

// TODO: This is just a placeholder
pub fn elementary_index(p1: ArrayView1<f64>, p0: ArrayView1<f64>, method: &str) -> Array2<f64> {
    Array2::from_elem((10, 10), 1.0)
}

fn calculate_relatives(p1: ArrayView1<f64>, p0: ArrayView1<f64>) -> Vec<f64> {
    p1.iter()
        .zip(p0.iter())
        .map(|(a, b)| a / b)
        .collect()
}
