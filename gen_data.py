# %%
import random as r
from datetime import datetime
from collections import OrderedDict
import polars as pl
from faker import Faker 

# %%
f = Faker(seed=12345)
provider_type = f.random_element(["obgyn", "surgery", "pcp", "oncology", "er", "anesthesiology", "cardiology", "neurology", "hematology", "dermatology", "pediatrics", "urology"])
provider_degree = f.random_element(["Doctor", "Physician Assistant", "Certified Nurse Practitioner"])

# %%
def gen_cpt_code() -> str:

    code = [
          f.random_choices(elements=OrderedDict([(f.random_uppercase_letter(), 0.45), (f.random_digit_not_null(), 0.55)]), length=1)[0]
        , f.random_digit_not_null()
        , f.random_digit_not_null()
        , f.random_digit_not_null()
        , f.random_choices(elements=OrderedDict([(f.random_uppercase_letter(), 0.45), (f.random_digit_not_null(), 0.55)]), length=1)[0]
    ]

    return "".join(map(str, code)) 

# %%
def gen_icd_code() -> dict:

    code = [
          f.random_uppercase_letter()
        , f.random_number(digits=5)
    ]

    return {
          "code": "".join(map(str, code)) 
        , "complication_cost": r.randint(a=1000, b=2000000)
    }
# %%
diags = [gen_icd_code() for y in range(1000)]
diags

# %%
def gen_procedure() -> dict:
    return {
          "cpt_code": gen_cpt_code()
        , "acceptable_codes": [r.choice(diags)["code"] for _ in range(r.randrange(1, 4))]
    }

# %%
procs = [gen_procedure() for y in range(100)]
procs

# %%
def gen_patient() -> dict:
    return {
          "fname": f.first_name()
        , "lname": f.last_name()
        , "dob": f.date_of_birth()
        , "ssn": f.ssn()
    }
    
# %%
pats = [gen_patient() for y in range(10000)]
pats

# %%

def gen_provider() -> dict:
    return {
          "npi": f.random_number(digits=9, fix_len=True)
        , "degree": provider_degree
        , "fname": f.first_name()
        , "lname": f.last_name()
        , "prov_tin": f.random_number(digits=10, fix_len=True)
        , "prov_type": provider_type
    }

# %%
provs = [gen_provider() for _ in range(100)]
provs

# %%
def gen_claim() -> dict:
    return {
          "proc_date": f.date_between_dates(date_start=datetime.fromisoformat("2025-03-18"), date_end=datetime.fromisoformat("2035-01-01"))
        , "proc_time": f.time()
        , "patient": r.choice(pats)
        , "admit_diag": r.choice(diags)
        , "provider": r.choice(provs)
        , "procedure": r.choice(procs)
        , "complication": f.random_element(OrderedDict([(0.0, 0.90), (0.50, 0.04), (0.75, 0.03), (1.0, 0.02), (1.1, 0.0075), (1.2, 0.0015)]))
    }

# %%
claims = [gen_claim() for y in range (10000)]

# %%
df = pl.DataFrame(data=claims).write_parquet("data/model_data.parquet")

# %%
