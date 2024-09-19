#!/usr/bin/python3

import pandas as pd
from dowhy import CausalModel

def teste_scm_pipeline(df: pd.DataFrame):
    #Step 1: Model
    model=CausalModel(
            data = df,
            treatment='X',
            outcome='Y',
            common_causes=['U'],
            instruments=['Z']
            )


    # Step 2: Identify
    identified_estimand = model.identify_effect(proceed_when_unidentifiable=True)

    # Step 3: Estimate
    estimate = model.estimate_effect(identified_estimand,
            method_name="iv.instrumental_variable", test_significance=True)

    # Step 4: Refute
    ref = model.refute_estimate(identified_estimand, estimate, method_name="placebo_treatment_refuter", placebo_type="permute")
    print(ref)


if __name__ == "__main__":
    df = pd.read_csv('../data/balke_pearl.csv')
    teste_scm_pipeline(df)