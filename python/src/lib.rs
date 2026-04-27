use pyo3::prelude::*;
use numpy::PyReadonlyArray1;
use core_logic::means::{arithmetic_mean, geometric_mean};

// ==========================================================
// MEANS MODULE
// ==========================================================

#[pyfunction]
#[pyo3(name = "arithmetic_mean")] // This is the name Python will see
fn py_arithmetic_mean(data: PyReadonlyArray1<f64>) -> f64 {
    arithmetic_mean(data.as_array())
}

#[pyfunction]
#[pyo3(name = "geometric_mean")]
fn py_geometric_mean(data: PyReadonlyArray1<f64>) -> f64 {
    geometric_mean(data.as_array())
}

#[pymodule]
fn means(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(py_arithmetic_mean, m)?)?;
    m.add_function(wrap_pyfunction!(py_geometric_mean, m)?)?;
    Ok(())
}
