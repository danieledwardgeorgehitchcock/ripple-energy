# Ripple Energy

[![PyPI - Version](https://img.shields.io/pypi/v/ripple-energy.svg)](https://pypi.org/project/ripple-energy)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ripple-energy.svg)](https://pypi.org/project/ripple-energy)

-----

**Table of Contents**

 - [Known Bugs And Issues](#known-bugs-and-issues)
 - [To-Do](#to-do)  
 - [Installation](#installation)
 - [Example](#example)
 - [Contributing](#contributing)
 - [License](#license)

## Known Bugs And Issues

 - ~~Any (all?) GraphQL query functions fail~~ solved by dapalex/py-graphql-mapper#25
 - ~~list_Date type clash warning~~ solved by dapalex/py-graphql-mapper#25
 - ~~Unsure of header format for token auth~~ now confirmed working
 - ~~insightsChartData optional in response but mandatory in framework~~

## To-Do

 - Complete function wrappers for all GraphQL queries
 - Complete function wrappers for all GraphQL mutations
 - Create function exceptions
 - ~~Put functions into classes~~
 - Add linting
 - Create tests
 - Create build pipeline 
 - Publish to PyPi 
 - ~~Make Async?~~

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

Get Member:
  ```python
from ripple_energy import RippleEnergy
import asyncio
from sys import platform

if(platform == "win32"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) #Avoid event loop selector policy error in Windows 

async def main():
    async with RippleEnergy(email = "YOUR_RIPPLE_EMAIL", password = "YOUR_RIPPLE_PASSWORD") as ripple:
        
        member = await ripple.get_member()
        
        print(member)

        version = await ripple.version()

        print(version)

asyncio.run(main())
```

## Contributing

To add a new query to this module, add the GraphQL query into the `src/ripple_energy/graphql_queries` folder as a file with the extension `.graphql` such as: `my_example_query.graphql` - please see the existing queries as an example of how to write them.

In a terminal, make sure you are in the Hatch shell environment:

```console
hatch shell start
```

Run the Ariadne code generator:

```console
ariadne-codegen
```

If there no errors, a new client should be generated in the `src/ripple_energy/graphql_client` folder.

Add the new function to `src/ripple_energy/ripple_energy.py` - please see the existing functions as an example of how to write them.

Commit the changes and create a Pull Request in this repo.

## License

`ripple-energy` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.