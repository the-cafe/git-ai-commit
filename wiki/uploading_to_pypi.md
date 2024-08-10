# Uploading to Pypi

## Login/Sign up for Pypi

Create an account on PYPI: Go to: <https://pypi.python.org> and select Register. Follow instructions.

Create an account on testpypi: Go to: <https://testpypi.python.org> and select Register. Follow instructions.

## Request Access to project

After making Pypi account, ask existing team members to add you as an collaborator to the project. After being added you should be able to access the following projects

Project links

- testpypi: <https://test.pypi.org/manage/project/prepare-commit-msg-hooks>

## Create a source distribution

PyPI has certain required meta-data that the setup.py should provide. If nothing is reported your package is acceptable. To quickly check if your project has this data use:

```bash
python setup.py check
```

This creates a dist/ directory containing a compressed archive of the package - `ai-commit-msg/dist/git-ai-commit-0.1.0.tar.gz`. This file is our source distribution.

```bash
python setup.py sdist # Generates dist/<PACKAGE_NAME>-<VERSION>.tar.gz
```

## Get Pypi API key

You are going to need two seperate API keys, a test and production PyPi one.

## To upload to Pypi

Install Twine

```bash
pip install twine
```

To upload to test Pypi

```bash
# Upload all your generated distributions
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Upload a specific version
twine upload --repository-url https://test.pypi.org/legacy/ ./dist/git-ai-commit-<version>.tar.gz
```

To upload to production Pypi

```bash
# Upload all your generated distributions
twine upload dist/*

# Upload a specific version
twine upload ./dist/git-ai-commit-<version>.tar.gz
```

## FAQ

This error is because the version number you have set has already been used. Check out the [pypi releases](https://test.pypi.org/manage/project/prepare-commit-msg-hooks/releases/) to see the latest versions. You need to make sure you properly increment the version before you upload.

The package version is defined in `setup.cfg` under the `version` attribute

```bash
WARNING  Error during upload. Retry with the --verbose option for more details.                                                                                                               
ERROR    HTTPError: 400 Bad Request from https://test.pypi.org legacy/                                                                                                                        
         File already exists. See https://test.pypi.org/help/#file-name-reuse for more information.          
```

----
