.. Accelerate documentation master file, created by
   sphinx-quickstart on Thu Jan 16 15:50:30 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Architecture
============

This is an overview of the architecture.

.. uml::

   Alice -> Bob: Hi!
   Alice <- Bob: How are you?


Below is code to add a table

.. list-table:: My Table
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3

Below is an example showing some python code

.. code-block:: python

  pygments_style = 'sphinx'

Showing some Sphinx Needs items

.. arch:: Lane Detection Subsystem
   :id: A_001
   :status: open
   :fulfil: R_001, R_002
   :jira: 3

   Design the software architecture for the Lane Detection Subsystem, including data acquisition, processing, and corrective action modules.

   .. uml::

      @startuml
      class LaneDetection {
          + detectLaneMarkings()
          + applySteeringCorrection()
      }
      class CameraInput {
          + provideData()
      }
      class SteeringControl {
          + correctSteering()
      }
      LaneDetection --> CameraInput
      LaneDetection --> SteeringControl
      @enduml


.. needflow:: My first needflow
   :show_link_names:
   
End of document