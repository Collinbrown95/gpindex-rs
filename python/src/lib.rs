use pyo3::prelude::*;
use numpy::PyReadonlyArray1;
use core_logic::{arithmetic_mean, geometric_mean};

#[pyfunction]
fn average(data: PyReadonlyArray1<f64>) -> f64 {
    arithmetic_mean(data.as_array())
}

#[pyfunction]
fn geo_mean(data: PyReadonlyArray1<f64>) -> f64 {
    geometric_mean(data.as_array())
}

#[pymodule]
fn my_rust_lib(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(average, m)?)?;
    m.add_function(wrap_pyfunction!(geo_mean, m)?)?;
    Ok(())
}
