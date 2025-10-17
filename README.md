![Python version](https://img.shields.io/badge/python-3.9.6-blue)

# Code Demo
The purpose of this repo is to showcase Blake Cromar's skills as a software developer. 

In this demo, the code calculates the standard deviation of an array of data. The goal was to use `Python` to calculate the standard deviation of male height data and analyze it. While there are `Python` packages that can do this simply, this code base attempts to do this without the help of any external packages.

The equation for standard deviation (sample) is as follows:

s = √[ Σ(xᵢ − x̄)² / (n − 1) ]

Where:
- s = sample standard deviation
- xᵢ = each data point
- x̄ = sample mean
- n = number of data points

## Table of Contents
- [How to Use](#how-to-use)
- [Example Output](#example-output)
- [Analysis of the Data Output](#analysis-of-the-data-output)
- [File Structure](#file-structure)
- [Git Branching Model](#git-branching-model)
- [Contributing](#contributing)
- [License](#license)

## How to Use

1. Navigate to the folder where the repo will be stored
```
cd /path/to/your/desired/folder
```

2. Clone the repo into the local directory you chose in the pervious step

```
git clone https://github.com/blake-cromar/code_demo.git
```

3. Open the folder of the project

```
cd code_demo
```

4. Run the script
```
python3 src/standard_deviation.py 
```

## Example Output

![alt text](output_example.png)

## Analysis of the Data Output
This type of output would be great for a situation where you are trying to estimate a majority of height differences for a business product. For example, consider a situation where you are building race cars and one constraint of the system is the height of the driver. You could use these statistics to determine that `99.7%`of men will have a height between `157.6` and `194.0` centimeters (see output above). You could build the car based on that range and then place a disclaimer that the cockpit of these cars only account for men of this range of height. 

## File Structure
```
CODE_DEMO/                      | Main folder
├─ .gitignore                   | .gitignore file used to prevent types of files from being pushed to repo
├─ README.md                    | Used to provide an over view of this code
├─ output_example.png           | An example of the desired output
├─ gitflow_example.svg          | An example of the branching model used for this repo
└─ src/                         | Contains the main source code
   └─ standard_deviation.py     | Contains the Python programming example
```

## Git Branching Model
This codebase is utilizing a `gitflow` branching model. In my implementation I've chosen to delete feature branches after they have been merged to the `development` branch. More about this branching strategy can be found [here](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

![alt text](gitflow_example.svg)


## Contributing
Blake Cromar, Software Engineer, blake.cromar@icloud.com

## License

MIT License

Copyright (c) [2025-present] [Blake Cromar]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.