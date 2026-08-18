# BZAN 531 Course Pre-Setup

This setup is for a future BZAN 531 class. The goal is to create a working Python environment with `uv`. The file `cat1w.py` is only a test script: if it runs successfully, your environment is ready for BZAN 531.

[Dr. Souza](https://scholar.google.com/citations?hl=en&user=twBwrYwAAAAJ) provided [`bzan531example.zip`](bzan531example.zip), which contains:

- `cat1w.py`
- `cat1w.dat`

Both files are needed for the test.

## 1. Create a Course Folder

Create a folder for the course and move into it:

```bash
mkdir bzan_531
cd bzan_531
```

## 2. Create the Python Project

Initialize a new `uv` project:

```bash
uv init
```

## 3. Install Python Packages

Install the Python packages needed for the test script and future class work:

```bash
uv add pyomo pandas
```

## 4. Install GLPK

`cat1w.py` uses Pyomo, but Pyomo needs an optimization solver. For this test, the solver is GLPK.

If you are on macOS and use Homebrew:

```bash
brew install glpk
```

If you are on Windows:

There are many ways to install GLPK on Windows; using Chocolatey seems to be one of the more straightforward approaches that works.

1. Install Chocolatey from https://chocolatey.org/install. You do not need to enter an email address; the newsletter signup is optional.
2. Open PowerShell or Command Prompt as Administrator.
3. Install GLPK:

```powershell
choco install glpk
```

These Windows steps were tested by Matthew Malone. Direct all questions, complaints, and praise to Matthew at mmalon45@vols.utk.edu.

If you are Ian Allish and use Linux, this should be `yum` / `apt-get` / etc. installable.

More information about GLPK is available here:

https://www.gnu.org/software/glpk/

Check that GLPK installed correctly:

```bash
glpsol --version
```

## 5. Add the Example Files

Move `bzan531example.zip` into your `bzan_531` folder.

Unzip it:

```bash
unzip bzan531example.zip
```

You should now have a folder named `bzan531example`.

Check that both files are present:

```bash
ls bzan531example
```

You should see:

```text
cat1w.dat
cat1w.py
```

## 6. Run the Test Script

Move into the example folder:

```bash
cd bzan531example
```

Run the test script:

```bash
uv run python cat1w.py
```

## Example Output

On Adam's machine, the script ran successfully and ended with this output:

```text
# ==========================================================
# = Solver Results                                         =
# ==========================================================
# ----------------------------------------------------------
#   Problem Information
# ----------------------------------------------------------
Problem:
- Name: unknown
  Lower bound: 8694954.44882855
  Upper bound: 8694954.44882855
  Number of objectives: 1
  Number of constraints: 31
  Number of variables: 50
  Number of nonzeros: 74
  Sense: minimize
# ----------------------------------------------------------
#   Solver Information
# ----------------------------------------------------------
Solver:
- Status: ok
  Termination condition: optimal
  Statistics:
    Branch and bound:
      Number of bounded subproblems: 0
      Number of created subproblems: 0
  Error rc: 0
  Time: 0.013283014297485352
# ----------------------------------------------------------
#   Solution Information
# ----------------------------------------------------------
Solution:
- number of solutions: 0
  number of solutions displayed: 0
T : Size=10, Index=Tset
    Key : Lower : Value            : Upper : Fixed : Stale : Domain
      1 :     0 :              0.0 :  None : False : False : NonNegativeReals
      2 :     0 : 967.193705593538 :  None : False : False : NonNegativeReals
      3 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
      4 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
      5 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
      6 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
      7 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
      8 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
      9 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
     10 :     0 : 1913.11453680081 :  None : False : False : NonNegativeReals
```
