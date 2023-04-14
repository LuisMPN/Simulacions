import numpy as np
import sisl
import sisl.viz
from pathlib import Path
import os


graphene =sisl.geom.graphene()
inputs_dir = Path("convergence/inputs")
graphene.write(inputs_dir / "geom.fdf")
root = Path("convergence/ks")
root.mkdir(exist_ok=True)
ks = ['1','2','3','4','5','6','7','8','9']
for k in ks:
    print(f"RUNNING SIMULATION FOR Ks: {k}")
    # Define the directory for this k, and create it if it doesn't exist
    k_dir = root / k
    k_dir.mkdir(exist_ok=True)


    # Copy inputs from the inputs directory into this one.
    os.system(f"cp {inputs_dir}/* {k_dir}")
    
    # Inside this directory, open a RUN.fdf file, which will be our main input file.
    with open(k_dir / 'RUN.fdf', 'w') as f:
        # We include the fdf file that contains the geometry, with the %include statement
        # Note the \n, which means "new line" in text files.
        f.write("%include geom.fdf \n")
        # We now include the basis size input.
        f.write(f"%block kgrid_Monkhorst_Pack \n  {k} 0 0  0 \n  0 {k} 0  0 \n  0 0 {k}  0  \n%endblock kgrid_Monkhorst_Pack \nPAO.BasisSize DZP" )




