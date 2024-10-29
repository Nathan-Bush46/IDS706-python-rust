# Rust-Python

[![Docker Image CI Main](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/main.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/main.yml)

[![Docker Image CI Lint](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/lint.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/lint.yml)

[![Docker Image CI Test](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/test.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/test.yml)

[![Docker Image CI Format](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/format.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/format.yml)

[![Docker Image CI Install](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/install.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-rust/actions/workflows/install.yml)


## Explanation of Repository 

Example of Rust vs Python script (not using numpy) speed compersion for sum_of_squares.

See [src/main_workspace](src/main_workspace) for python and rust script/binary

## Performance comparison
* Python 
   * Sum of squares: 333332833333500000
   * Time taken (seconds): 0.06199383735656738
* Rust
   * Sum of squares: 333332833333500000
   * Time taken (seconds): 0.006056

As you can see in this simple demo, Rust is about ten times faster then python (base libs only). Note: this testing is not perfect as the system load and memory may be different for each run.

## Set up instructions using VS code + Docker: 
### Docker
1. For Windows, Mac, and maybe Linux, you download Docker Desktop. links can be found [here](https://docs.docker.com/engine/install/). Follow set up instructions and start the application.

2. In vs code add Dev Containers and Docker extensions 

3. clone repo, restart vs code, and open repo in vs code.

4. should see a pop up to (re)open in devcontainer. Click it and let it run. It takes a bit of time for the first run but is much faster after that. hit enter to install rust when prometed, restart terminal. Done.

#### Alternatives to Docker
If you choose not to run docker, use a python virtual environment (and rust) to prevent conflict with local packages and run the makefile.
 
## Testing

### makefile  
* install

* testing:

    tests all "\*test\*.py" files in src/test/ using py.test then tests all files using py.test --nbval-lax

* lint

* format

* all 

### VS code testing  
1. Can also use the VS-code testing menu in the same way.

## Things included are:

* [`Makefile`](Makefile)

* `Pylint` and `Ruff` for lintning

* `.devcontainer` with [`Dockerfile`](/.devcontainer/Dockerfile), [`postinstall.sh`](/.devcontainer/postinstall.sh), and [`devcontainer.json`](/.devcontainer/devcontainer.json)`

*  [`settings.json`](.vscode/settings.json) for testing

*  A base set of libraries in [`requirements.txt`](requirements.txt)
