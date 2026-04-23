use extendr_api::prelude::*;
// Use the double colon to tell Rust "the crate at the root"
use ::ndarray::ArrayView1; 
use core_logic::{calculate_average, calculate_geometric_mean};


#[extendr]
pub fn r_average(data: ArrayView1<f64>) -> f64 {
    calculate_average(data)
}

#[extendr]
pub fn r_geo_mean(data: ArrayView1<f64>) -> f64 {
    calculate_geometric_mean(data)
}

extendr_module! {
    mod gpindexr;
    fn r_average;
    fn r_geo_mean;
}
