# General Purpose Indexes

> TODO

## Python Language Setup

> TODO

## R Language Setup

```R
# Create scaffolding
usethis::create_package("gpindexr")
rextendr::use_extendr()
```

**For release build**

```R
Sys.setenv(RUSTFLAGS = "-C target-cpu=native")
Sys.setenv(REXTENDR_BUILD_FLAGS = "--release")
devtools::document()
devtools::install(pkg = ".", args = "--preclean", quick = TRUE)
devtools::load_all()
```
