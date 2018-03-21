# On Time, Pie !

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d3d03cb6004147fb8017780cc91d5d56)](https://www.codacy.com/app/dusterherz/on-time-pie?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dusterherz/on-time-pie&amp;utm_campaign=Badge_Grade)

Never be late anymore for public transport with the help of python raspberry and navitia !

## What is "On Time, Pie !" ?

On Time, Pie is a project which run on a Raspberry Pi and Python. With the help of
Navitia and of a 7-digit screen, your RPI display the next line comming near your
bus stop or your metro station and in how many minutes it is comming. Be never
late anymore and see again your bus / train pass in front of you !

The project is currently in progress.

## WIP

See the Github project and issues to see the current progress of the project.

Progress Bar :
⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪ 50%

## Getting Started

### Hardware

You will need a 7 segment 4 display common cathode with 12 pins like [this one](https://www.amazon.com/uxcell%C2%AE-7-Segment-Digital-Display-Cathode/dp/B00W977X8O/), 8 x 100 Ohm resistors, some wires, and, of course, a raspberry pi connected on the internet !

You can follow [this tutorial](http://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python) made by @raspitv to connect your 4 digits - 7 segments diplay on your raspberry. The project use exactly the same pins, so no need to modify anything in the code !

### Setting up the Raspberry Pi

For this project your raspberry need the 3.6 version of Python. If you have raspbian installed on it, you can upgrade your version of python [following this tutorial](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f).

You will need also pipenv to run this and install all dependencies. If you don't have pipenv, your can follow [this official tutorial](https://docs.pipenv.org/install/#installing-pipenv) to install it. Then make ```pipenv install``` to install all dependencies and to create a virtualenv for this project.

To run the project, access to your virtualenv via ```pipenv shell``` and run the project with ```python run.py``` and voila, it's alive !

### Configure

WIP

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
