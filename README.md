
# A cautionary note on the use of  Gurobi for cryptanalysis
This is the accompanying code for the article "[A cautionary note on the use of  Gurobi for cryptanalysis](https://eprint.iacr.org/2020/1112)". It consists of the code of the four examples mentioned in the report.
## Dependancies
[Gurobi](https://www.gurobi.com/) `9.0.2 build v9.0.2rc0 (linux64)`

## Usage
Each example mainly consists of the MILP model in LP format `model.lp` and the python script `SolveModel.py` to test the model. 
To run the test, simply execute the following command:
- For Example I, II, III: ```$ gurobi.sh SolveModel.py model.lp```
- For Example IV: ```$ gurobi.sh SolveModel.py model.lp model_reoredered.lp```

It will generate three files: 
1. Gurobi log file for the n-threads run: `Log*_cores.log`
2. Gurobi log file for the single-thread run: `Log1_cores.log`
3. The feasible solution from the single-thread run: `solution_1_cores.sol`

And the output will be like:
```
Test Using 80 threads ...



Using license file /********************/gurobi902/linux64/gurobi.lic
Set parameter TokenServer to value ***************
Read LP format model from file model.lp
Reading time = 0.12 seconds
: 10882 rows, 38880 columns, 175220 nonzeros



the model is infeasible



Test Using 1 threads ...



Read LP format model from file model.lp
Reading time = 0.08 seconds
: 10882 rows, 38880 columns, 175220 nonzeros



Find Solution



```
## Verify that `model.lp` and `model_reoredered.lp` in Example IV are the same
Sort the constraints of each then compare digest hash of them.
```
$ md5sum <<< $(sort model.lp)
808a10ad7023917e2fa461be5c5704ef  -
$ md5sum <<< $(sort model_reordered.lp)
808a10ad7023917e2fa461be5c5704ef  -
```

## Validate the solution
To verify that the solution from the single-thead satisfies all the inequalities in the model:
```bash
$ ./testSol_using_model.sh "./Example_I/model.lp" "./Example_I/solution_1_cores.sol"
```
The output will be:
```
Does the solution satsify all the constraints? True
```
