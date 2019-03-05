dewey
=====
Dewey makes life easier on the command line.


# TODO:
1. Update w/ proper docker syncing 
1. Add polytester
1. Integrate bootstrap script and NVM
1. Update w/ multiple codebases for dev & testing. One-command development.


## Installing

```bash
pip install git+https://git@github.com/sidebarchats/dewey.git#egg=dewey

# Find the path
source {path_to_lib}/bin/bootstrap_dewey.sh
```

## Using more broadly:

Dewey (0.2.8+) allows configuration of the namespace, for more general use, via the `DEWEY_NAMESPACE` environmental variable.  It defaults to `sidebar`.

Some examples:

```bash
$ d workon backend
> # sets up sidebar-backend environment

$ export DEWEY_NAMESPACE='myproj'
$ d workon foo
> # sets up myproj-foo environment


$ export DEWEY_NAMESPACE='NO_NAMESPACE'
$ d workon bar
> # sets up bar environment
```
