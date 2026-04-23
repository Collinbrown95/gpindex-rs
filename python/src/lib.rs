use pyo3::prelude::*;
use numpy::PyReadonlyArray1;
use core_logic::calculate_average;

#[pyfunction]
fn average(data: PyReadonlyArray1<f64>) -> f64 {
    calculate_average(data.as_array())
}

#[pymodule]
fn my_rust_lib(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(average, m)?)?;
    Ok(())
}
