# Testing out Sphinx

This repo is to test and show how Sphinx can be used.

Check out result [here](https://erikbosch.github.io/test_sphinx/proto/index.html).

# Setup Used

Basic steps required

```bash
python -m venv .venv
source .venv/bin/activate
pip install sphinx
```

This repo was created calling `sphinx-quickstart` as described in the user manual.

```bash
(.venv) erik@debian7:~/test_sphinx$ mkdir docs
(.venv) erik@debian7:~/test_sphinx$ cd docs
(.venv) erik@debian7:~/test_sphinx/docs$ sphinx-quickstart
Welcome to the Sphinx 8.1.3 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: 

The project name will occur in several places in the built documentation.
> Project name: Accelerate
> Author name(s): Accelerate Team
> Project release []: 

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: 

Creating file /home/erik/test_sphinx/docs/conf.py.
Creating file /home/erik/test_sphinx/docs/index.rst.
Creating file /home/erik/test_sphinx/docs/Makefile.
Creating file /home/erik/test_sphinx/docs/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /home/erik/test_sphinx/docs/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

The files have been modified to show a possible base structure. Files are then created like below:

```bash
(.venv) erik@debian7:~/test_sphinx/docs$ make html
Running Sphinx v8.1.3
loading translations [en]... done...
build succeeded, 2 warnings.

The HTML pages are in _build/html.
```

## PlantUML

You can easily add UML

`sudo apt install plantuml`

Follow https://github.com/sphinx-contrib/plantuml/blob/master/README.rst

`pip install sphinxcontrib-plantuml`


See example in architecture

## Themes

To make it look better. This is a quite common theme

https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/

Install by 

`pip install sphinx-rtd-theme`

Change `html_theme` in `conf.py`.

## Workflow

See https://coderefinery.github.io/documentation/gh_workflow/ for configuration

Result will be available in the `gh-pages` branch and deployed at https://erikbosch.github.io/test_sphinx/index.html

## Notes

There are more dependencies, check workflow.






