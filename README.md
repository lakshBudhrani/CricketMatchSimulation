# CricketMatchSimulation

## Project Description

This project simulates a 4-innings Test cricket match on a ball-by-ball basis using VBA in Excel. The simulation involves two teams, "India" and "Australia," determined by a virtual toss. Key components include initializing teams, setting batting and bowling orders, generating individual ball outcomes, updating scorecards, and logging match results.

### Project Components

- **CricketMatchSimulation.xlsm**: Main simulation file that runs when you click the "Run Trial" button.
- **Python Files**: Scripts used for data extraction and probability distribution:
  - `data_extraction.py`
  - `info_extraction.py`
  - `overall_career_stats.py`
  - `prob_distribution.py`
- **Report_FinalProject.pdf**: Detailed report of the project, including data collection, theoretical framework, VBA implementation, and result analysis.

### Key Features

1. **Data Collection**: 
   - Utilized Cricsheet for ball-by-ball data from 845 Test matches in JSON format.
   - Extracted data using Python to obtain empirical probability distributions for each player at the Sydney Cricket Ground (SCG).
2. **Batting and Bowling Lineup**: 
   - Predetermined batting lineup based on the squad.
   - Assigned bowling probabilities based on personal experience.
3. **Simulation Implementation**: 
   - Developed in VBA to simulate each ball, update scorecards, and log match results.

### Note

To run the `CricketMatchSimulation.xlsm` file, you need to keep a file `BCNNvba.xla` in the same repository as the `CricketMatchSimulation.xlsm` file. This file is not included in the repository as it belongs to the author of the book *Discrete-Event System Simulation* and can be found on the author's website. The website link is not provided here as it frequently changes.

## Conclusion

The project demonstrates the use of VBA in simulating a cricket match, utilizing empirical probability distributions and providing a detailed analysis of the match outcomes.
