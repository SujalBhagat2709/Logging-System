# Logging System

## Overview

Simple logging system using Python logging module.

---

## Features

* Console logging
* File logging
* Request logging

---

## Files

* `logger.py` → console logger
* `file_logger.py` → logs to file
* `request_logger.py` → logs API requests

---

## Usage

```python
from logger import get_logger

log = get_logger()
log.info("Hello")
```

---

## Example Output

```
2026-04-21 10:00:00 - INFO - Logger initialized
```

---

## Use Case

* Backend services
* APIs
* ML pipelines
* Debugging systems