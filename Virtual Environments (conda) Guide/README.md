## Create Python virtual environments with conda

Please _do not use python "base" environment_ for installing your dependencies, your packages can be easily create conflicts with the packages installed by other researchers.

You can create a virtual environment with your specific packages and needs using: `conda create -n {environment name} python={python version}`. Example:

```
conda create -n pipeg_env python=3.11
```

Please use a meaningful name (e.g. `pipeg_env` for Pipe Galera test environment)

Your environment gets saved at your project folder: `F:Data\Workdata\{project id}\anaconda\envs\{your env}`

## Install what you need

Activate your environment `conda activate pipeg_env` and pip install what you need (e.g. `pip install pandas`)

You will notice that the package comes from a DST private channel called "srcnexus"

## Tidy up environment

Please do not keep a collection of environments (e.g. `pipeg_env`, `test`) for the same project goal. Check the current environments `conda env list` and delete your own environments that are not using (e.g. `conda remove -n test --all`).

Remember that all the researchers of your project are using the same conda manager, keep it tidy!
