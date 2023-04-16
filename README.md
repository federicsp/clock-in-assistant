# Clock-in Assistant

This script reminds the user to clock in at specific times during the day.
The script checks the current hour and plays an audio reminder at the following time intervals: 9am-10am, 1pm-2pm, 2pm-3pm, and 6pm-7pm.
The script asks if you have clocked in, and if you don't respond, it will ask again after 15 minutes.

# Table of Contents

- [Clock-in Assistant](#clock-in-reminder)
- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Usage](#usage)
- [Test](#test)

<!-- required -->
## Requirements

This project requires:

- Python 3.9+
- packages in `requirements.txt`


## Usage

To run the script:

1. Clone the repository
2. Install the requirements
3. Run the script with `python -m main`

## Test

The command `python3 -m pytest .` is used to run the pytest framework and execute all the tests present in the `test` folder.

