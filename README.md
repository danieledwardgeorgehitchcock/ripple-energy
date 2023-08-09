# Ripple Energy

[![PyPI - Version](https://img.shields.io/pypi/v/ripple-energy.svg)](https://pypi.org/project/ripple-energy)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ripple-energy.svg)](https://pypi.org/project/ripple-energy)

-----

**Table of Contents**

 - [Known Bugs And Issues](#known-bugs-and-issues)
 - [To-Do](#to-do)  
 - [Installation](#installation)
 - [Example](#example)
 - [License](#license)

## Known Bugs And Issues

 - Any (all?) GraphQL query functions fail
 - list_Date type clash warning
 - Unsure of header format for token auth

## To-Do

 - Complete function wrappers for all GraphQL queries
 - Complete function wrappers for all GraphQL mutations
 - Create function exceptions
 - Put functions into classes
 - Add linting
 - Create tests
 - Create build pipeline 
 - Publish to PyPi 
 - Make Async?

## Installation

At present, this package has not been published to PyPi - You will therefore need to clone this repository to use it.  

```console
git clone https://github.com/danieledwardgeorgehitchcock/ripple-energy.git
```
This project leverages the use of [Hatch](https://hatch.pypa.io/latest/) for project management - please follow the installation instructions there before continuing.

Once the above has completed, enter in to the project directory

```console
cd ripple-energy
```
As this package is managed by Hatch, you can start an environment which automatically pulls the project dependencies
  
  ```console
hatch shell start
```

You should then be able to use the package from within this environment.

## Example
Token Auth:
  ```python
from  ripple_energy  import token_auth

data  = token_auth(email  =  "YOUR_RIPPLE_EMAIL", password  =  "YOUR_RIPPLE_PASSWORD")

print(data.token)
```

## License

`ripple-energy` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.