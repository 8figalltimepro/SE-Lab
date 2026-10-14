# Lab 5: Issues Found and Fixed

Student: Samarth Mohan | SRN: PES1UG24CS703
File: `vehicle_service.py`, the vehicle service desk for a garage.

I ran Pylint, Bandit and Flake8 on the file as it came from the repo and saved the
output in `reports/before/`. Then I fixed the findings and saved the new output in
`reports/after/`. The line numbers in the table are from the original file, before
my edits.

## Issue table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Weak MD5 hash (B324) | Security, High | 39 | `hashlib.md5()` makes the job card id, MD5 is not safe for security use | Added `usedforsecurity=False`, the id is only a short label and not a password hash |
| Shell call (B602) | Security, High | 61 | `subprocess.call("cp services.json " + folder, shell=True)` runs a shell string built from `folder` | Replaced with `shutil.copy("services.json", folder)`, no shell and no string join |
| Mutable default arg (W0102) | Bug | 12 | `history=[]` is built once and shared by every call to the function | Default is `None` now and a fresh list is made inside the function |
| Broad exception (W0718) | Bug | 23 | `except Exception` catches everything, so a real error would be hidden | Changed to `except KeyError`, that is the only error the code expects there |
| Hardcoded password (B105) | Security, Low | 8 | `ADMIN_PASSWORD = "garage-demo"` keeps a secret in the source file | Reads it from `GARAGE_ADMIN_PASSWORD` with `os.environ.get()` |
| Unused risky import (B404) | Security, Low | 3 | `import subprocess` was only used by the shell call above | Removed, `shutil` does the copy |
| Missing encoding (W1514) | Bug | 50, 55 | `open()` without encoding uses the machine locale, which breaks on other machines | Added `encoding="utf-8"` to both calls |
| camelCase names (C0103) | Style | 12 to 59 | 18 names like `addService`, `vehicleNo` and `totalCost` do not follow the naming style | Renamed to snake_case and updated every call in `main()` |
| Missing docstrings (C0114, C0116) | Style | 1, 12 to 64 | No module docstring and none of the nine functions had one | Added the module docstring and a docstring to the seven functions the demo uses |
| Two docstrings left as is (C0116) | Style | 60, 65 | `backupRecords()` and `main()` still have no docstring | Not fixed. Both are short and I documented the functions the program uses. Pylint still shows these two messages and the score is 9.68/10 |
| Long lines (E501) | Style | 49, 77 | The `print` call and the md5 return were over the 79 character limit | Split both over two lines |
| Missing whitespace (E231, E225) | Style | 7, 43 | `2500,"Brake Check"` and `best=None` | Added the missing spaces |
| Blank lines (E302) | Style | 49 | Only one blank line above `saveRecords` | Put two blank lines before it |

## After the fixes

Pylint went from 4.66/10 to 9.68/10. Bandit went from 4 issues to 0. Flake8 went
from 4 issues to 0. The program still prints the same five lines, and the job card
id for KA01AB1234 is still `353ee89f`.
