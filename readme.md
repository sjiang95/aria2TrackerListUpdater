# Aria2 Tracker List Updater

This script helps to update `bt-tracker` of aria2 config file from [ngosang/trackerslist](https://github.com/ngosang/trackerslist).

## Prerequisite

The script requires the `requests` module. If you use `entware`, run

```bash
opkg install python3-requests
```

Anyway, please install the `requests` module properly.

## Usage

Put the script `updater.py` under the same folder of your aria2 config file (Default: `aria2.conf`). Run

```bash
python updater.py
```

or if your config filename is customized, run

```bash
python updater.py -i <customized config filename>
```

For example, if your config filename is "aria2.cfg", run

```bash
python updater.py -i aria2.cfg
```
