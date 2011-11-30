:title: Integration Testing

Integration Testing
###################

Black Box vs White Box Testing
******************************

Two different types of integration tests are commonly referred to as
**black box testing** and **white box testing**.

White box testing refers to tests where the test runner can access
internal data structures (machine state) or algorithms in order to
verify a specification.

In black box testing, only the public API or other externally facing resources are ever called, since internal interfaces would give access to internal machine state, and the goal is typically to verify that a public API behaves according to its publically documented specification.

The ``Tempest`` Project
*******************************************

There was a proliferation of integration test suites in 2011, and at the
Essex design summit, a number of interested parties, including authors of
the various existing integration test suites -- met to discuss a plan
to consolidate similar test suites into a single project that everyone
could focus their efforts on. The resulting project is the
``Tempest`` project. This project contains functional and integration tests that are meant to be executed against a fully-deployed OpenStack environment.

.. note

  You should join the OpenStack QA team on Launchpad to contribute
  to the ``Tempest`` project.

Source Code Structure
~~~~~~~~~~~~~~~~~~~~~

The project source code is divided up in such a way that additional or
alternate functionality can easily be added to the framework. The current
directory structure is shown below.

* etc
* include
* kong
* tempest
    - common
    - services
    - tests
* tools

Of these, the include, kong, and tools directories are deprecated and will
soon be removed. Of the remaining directories, their purposes are:

* etc - a directory for text configuration files
* common - a set of reusable classes that provide additional functionality for testing and verification purposes
* services - code abstractions of an API. These clients provide access to the application under test in a simple and straightforward manner using domain specific terminology
* tests - a directory for the tests themselves. While this is currently a flat directory, the expectation is that subdirectories will be created to logically divide tests by project and logical functionality

Project Goals and Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When designing this framework, the primary focus were the following goals: ease of development, scalability, flexibility, and maintainability. This means that a test class can take action via the client without having to format and make a request. The client then becomes a middle man between the tests and a simple REST client. This separation of concerns has the benefit of not only x, but also reduces the refactoring impact when changes are made to the application under test.

To achieve the first goal, domain specific clients were developed. In doing so, several things were achieved. First, some of the complexity of testing APIs such as handling requests, authentication, and parsing of responses are already handled. An additional benefit is that in doing so, the structure and logic of the REST request itself is removed from the tests into a single location. This increases the maintainability of the code since when a change in logic or request structure occurs, only the client code needs to change.

Configuring Tempest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To make execution of Tempest flexible, values that will vary by environment are expected to be provided by an external data source, which is currently an external configuration file.

Additionally, Tempest takes into account that certain functionality may vary or not be usable based on the environment the tests are executed against. To avoid execution of tests that are not valid in a given environment, feature flags can also be set which will skip over executing tests that are not valid for the environment under test. For more detailed information, see the Temptest_README file and the example Tempest configuration file which are located in the /etc directory.

Running Tempest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests can be run using the Nose test runner. To run a test or a group of tests, execute the nosetests command with a specific test file or directory as a parameter. For example, running "nosetests tempest/tests" will run all tests in the tempest/tests directory.

Adding a New Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create new files/subdirectories for the functionality to be tested
* Add attributes to the test to describe its purpose
* Create an instance of the OpenStack manager class
* Pull test data from external sources if necessary
* Execute the desired scenario using service methods exposed via the clients or capabilities provided by common libraries
* Make any necessary assertions to verify the goal of the test has been met

In the development of tests, some patterns and practices have come into being:

* Individual tests should make no assumptions on the current state of the application. tests should either create their own resources or rely on provided known good values from external sources
* Tests should have a very clear focus. Trying to test too much in a single test makes the purpose of a test unclear.

Future Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Additional data sources for test data and configuration
* Parallel test execution
* Detailed logging
* Support for testing with XML requests/responses
* Improved reporting over the standard Nose xunit results
