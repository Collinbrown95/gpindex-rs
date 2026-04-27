use pyo3::prelude::*;
use numpy::{PyReadonlyArray1, IntoPyArray};
use core_logic::means::{arithmetic_mean, geometric_mean};
use core_logic::elementary_indexes::{carli_index, jevons_index, elementary_index};

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

// ==========================================================
// ELEMENTARY INDEXES MODULE
// ==========================================================

#[pyfunction]
#[pyo3(name = "carli_index")]
fn py_carli_index(p1: PyReadonlyArray1<f64>, p0: PyReadonlyArray1<f64>) -> f64 {
    carli_index(p1.as_array(), p0.as_array())
}

#[pyfunction]
#[pyo3(name = "jevons_index")]
fn py_jevons_index(p1: PyReadonlyArray1<f64>, p0: PyReadonlyArray1<f64>) -> f64 {
    jevons_index(p1.as_array(), p0.as_array())
}

#[pyfunction]
#[pyo3(name = "elementary_index")]
fn py_elementary_index(
    py: Python<'_>, 
    p1: PyReadonlyArray1<f64>, 
    p0: PyReadonlyArray1<f64>
) -> PyResult<PyObject> {
    // 1. Call your core logic
    let res_array = elementary_index(p1.as_array(), p0.as_array(), "jevons");

    // 2. Convert to a generic Python Object
    // .to_object(py) handles the conversion from the NumPy type
    Ok(res_array.into_pyarray(py).to_object(py))
}
// ==========================================================
// MAIN MODULE
// ==========================================================

#[pymodule]
fn pygpindex(_py: Python<'_>, m: &PyModule) -> PyResult<()> {

    // ==========================================================
    // means module
    // ==========================================================
    let means_submodule = PyModule::new(_py, "means")?;
    means_submodule.add_function(wrap_pyfunction!(py_arithmetic_mean, means_submodule)?)?;
    means_submodule.add_function(wrap_pyfunction!(py_geometric_mean, means_submodule)?)?;
    m.add_submodule(means_submodule)?;

    // ==========================================================
    // elementary indexes module
    // ==========================================================
    let elementary_indexes_submodule = PyModule::new(_py, "elementary_indexes")?;
    elementary_indexes_submodule.add_function(wrap_pyfunction!(py_carli_index, elementary_indexes_submodule)?)?;
    elementary_indexes_submodule.add_function(wrap_pyfunction!(py_jevons_index, elementary_indexes_submodule)?)?;
    elementary_indexes_submodule.add_function(wrap_pyfunction!(py_elementary_index, elementary_indexes_submodule)?)?;
    m.add_submodule(elementary_indexes_submodule)?;
    Ok(())
}
