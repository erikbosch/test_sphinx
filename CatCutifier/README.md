# Example for generated doc from C++

Loosely based on https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/

Look at `gen_doc.yml` to see how to generate. In short it is about

* Build the project
* Run doxygen
* Have a file that specifies where to include documentation, see `cat.rst`


# Open topics

`QT_AUTOBRIEF`and `JAVADOC_AUTOBRIEF`c an be used.

# Links

There seems to be two "general styles" C++ and Java. It can also be noted that Google does not seem to prescribe any doxygen compatible syntax. They do have however some guidelines at https://github.com/googleapis/google-cloud-cpp/blob/main/doc/cpp-style-guide.md where they seem to focus on documenting APIs.

* https://micro-os-plus.github.io/develop/doxygen-style-guide/
* https://www.doxygen.nl/manual/docblocks.html
* https://google.github.io/styleguide/cppguide.html#Function_Comments