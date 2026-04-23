use extendr_api::prelude::*;
// Use the double colon to tell Rust "the crate at the root"
use ::ndarray::ArrayView1; 
use core_logic::calculate_average;

#[extendr]
pub fn r_average(data: ArrayView1<f64>) -> f64 {
    calculate_average(data)
}

extendr_module! {
    mod gpindexr;
    fn r_average;
}
