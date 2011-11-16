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

In black box testing, only the public API is ever called, since internal
interfaces would give access to internal machine state, and the goal is
typically to verify that a public API behaves according to its publically
documented specification.

The ``openstack-integration-tests`` Project
*******************************************

There was a proliferation of integration test suites in 2011, and at the
Essex design summit, a number of interested parties, including authors of
the various existing integration test suites -- met to discuss a plan
to consolidate similar test suites into a single project that everyone
could focus their efforts on. The resulting project is the
``openstack-integration-tests`` project. This project contains functional
and integration tests that are meant to be executed against a fully-deployed
OpenStack environment.

.. note

  You should join the OpenStack QA team on Launchpad to contribute
  to the ``openstack-integration-tests`` project.

Source Code Structure
~~~~~~~~~~~~~~~~~~~~~

The project source code is divided into a number of directories, containing
various stand-alone test suites as well as a number of scripts for running
whole suites or sets of individual test cases.

Architecture of Main Suite Runner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adding a New Integration Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
