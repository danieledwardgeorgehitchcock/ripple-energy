# Ripple Energy

A Python package For interacting with the Ripple Energy GraphQL API.

The primary purpose of this package is to create an interface for Home Assistant to communicate with the Ripple Energy GraphQL API however, the facility is available to develop this module further by adding additional queries / functions.

-----

**Disclaimer** - I do not work for Ripple Energy however, I have memberships in some of their co-ops. While this module has been developed in consultation with Ripple Energy, I cannot guarantee it's long-term support or stability.

-----

[![PyPI - Version](https://img.shields.io/pypi/v/ripple-energy.svg)](https://pypi.org/project/ripple-energy)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ripple-energy.svg)](https://pypi.org/project/ripple-energy)

-----

**Table of Contents**

 - [To-Do](#to-do)  
 - [Installation](#installation)
 - [Example](#example)
 - [Contributing](#contributing)
 - [License](#license)

## To-Do

 - [x] Create exceptions
 - [x] Put functions into classes
 - [x] Add linting
    - [x] [PEP8](https://peps.python.org/pep-0008/) compliance
    - [x] [PEP257](https://peps.python.org/pep-0257/) compliance
    - [x] [PEP484](https://peps.python.org/pep-0484/) compliance
 - [ ] Create tests
 - [ ] Create build pipeline 
 - [x] Publish to PyPi 
 - [x] Make Async?

## Installation

### From Package Index

It is recommended to use `pip` to pull the package from PyPi

```console
pip install ripple-energy
```

### From Repository

Clone this repository  

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

  ```python
from ripple_energy import RippleEnergy, RippleEnergyCredentialAuth
import asyncio
from sys import platform

if(platform == "win32"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) #Avoid event loop selector policy error in Windows 

async def main():

    auth = RippleEnergyCredentialAuth(email="YOUR_RIPPLE_EMAIL", password="YOUR_RIPPLE_PASSWORD")

    async with RippleEnergy(auth=auth) as ripple:

        #Query filter
        faqs = await ripple.faqs("business")
        
        #Full object response
        print(faqs)
        
        member = await ripple.member()

        #Filtered object response
        print(member.address)

        version = await ripple.version()

        #Simple type response
        print(version)

if __name__ == "__main__":
    asyncio.run(main())
```

## Contributing

To add a new query to this module, add the GraphQL query into the `src/ripple_energy/graphql_queries` folder as a file with the extension `.graphql` such as: `my_example_query.graphql` - please see the existing queries as an example of how to write them.

In a terminal, make sure you are in the Hatch shell environment:

```console
hatch shell start
```

This project uses the Ariadne code generator. To run it:

```console
ariadne-codegen
```

If there no errors, a new client should be generated in the `src/ripple_energy/graphql_client` folder.

Add the new function to `src/ripple_energy/ripple_energy.py` - please see the existing functions as an example of how to write them.

Commit the changes and create a Pull Request in this repo.

## License

`ripple-energy` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.