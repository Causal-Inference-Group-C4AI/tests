from autobounds.causalProblem import causalProblem
from autobounds.DAG import DAG
from autobounds.Query import Query

import pandas as pd
import numpy as np

def calculate_ate_exemplo_7():
    raw_data = pd.read_csv("slide_exemplo_7.csv")

    dag_just = DAG()
    dag_just.from_structure(edges="U1 -> X1, U1 -> X2, U2 -> X1, U3 -> X1, X1 -> X2")

    dat = pd.DataFrame(raw_data.groupby(['X1', 'X2','U1','U2','U3']).value_counts().reset_index()) 
    dat['prob'] = dat['count'] / dat['count'].sum()
    dat = dat.drop(columns='count', axis=0)

    problem_just = causalProblem(dag_just)
    problem_just.load_data(dat)

    problem_just.add_prob_constraints()

    problem_just.set_ate(ind="X1", dep="X2")

    just_prog_ate = problem_just.write_program()

    just_prog_ate_optim = just_prog_ate.run_scip('replication_files/results/ate_exemplo_7.csv')

    print("==============================================")
    print(f"Causal effect lies in the interval [{np.round(just_prog_ate_optim[0]['dual'], 3)}, "
        f"{np.round(just_prog_ate_optim[1]['dual'], 3)}]" 
    )

def main():
    calculate_ate_exemplo_7()

if __name__ == '__main__':
    main()
