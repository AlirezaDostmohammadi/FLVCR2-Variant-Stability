# FLVCR2-Variant-Stability
Characterize the impact of the identified Arg492Trp variant on the WT `FLVCR2` protein.

In this analysis, we introduced the Arg492Trp variant into the FLVCR2 protein structure with <a href='https://www.rcsb.org/structure/8QD0'>PDB ID: 8QD0</a> (<a href='https://www.uniprot.org/uniprotkb/Q9UPI3/entry'>UniProtKB id: Q9UPI3</a>).

## Modeling Missing Residues
The determined protein structure of FLVCR2 has 112 missing residues. To address these gaps, we modeled the missing residues using <a href='https://salilab.org/modeller/'>Modeller</a> (version 10.6), generating 10 models. The model with the lowest molpdf score (459.43842) was selected as the best representation.

You can find the script used for modeling in the <a href='/ModelingMissingResidues'>ModelingMissingResidues</a> folder. Modeled structures are available in <a href='ModelingMissingResidues/refined_models'>refined_models</a>. Scores for each structure can be seen <a href='/ModelingMissingResidues/refine_missing_residues.py.log#L3807'>here</a>.

The model <a href='ModelingMissingResidues/refined_models/8qd0_fill.B99990007.pdb'>8qd0_fill.B99990007.pdb</a> has the lowest molpdf score: 459.43842.

## Minimizing Structures
We evaluated the impact of the Arg492Trp variant on protein stability using <a href='https://rosettacommons.org/software/'> Rosetta </a>(version 3.14) and <a href='https://biosig.lab.uq.edu.au/dynamut2/'>DynaMut2</a> to ensure robust and complementary analyses.

### Evaluated the impact of the Arg492Trp variant on protein stability using Rosetta
#### wild-type `FLVCR2` protein
1. clean structure:
```
clean_pdb.py 8qd0_fill.B99990007.pdb A
``` 
2. Minimize structure
The WT FLVCR2 structure was minimized independently 10 times using relaxation with constraints to preserve the starting coordinates.
The most stable (lowest-scoring) structure was selected.
`
relax.static.linuxgccrelease -s 8qd0_fill.B99990007_A.pdb -relax:constrain_relax_to_start_coords -relax:ramp_constraints false -ex1 -ex2 
-use_input_sc -flip_HNQ -no_optH false  -nstruct 10  -out:file:scorefile af_relaxed_8qd0.WT_A.sc
`
Results are available in the <a href='/MinimizingStructures/WT'>WT</a> folder. Scores for minimized structures are in <a href='MinimizingStructures/WT/af_relaxed_8qd0.WT_A.sc'>af_relaxed_8qd0.WT_A.sc</a>.

The structure <a href='/MinimizingStructures/WT/8qd0_fill.B99990007_A_0004.pdb'>8qd0_fill.B99990007_A_0004.pdb</a> has the lowest energy: -996.168 REU.

#### `FLVCR2` protein with the Arg492Trp variant
1. Introduce variant and minimize structure:
The Arg492Trp variant was introduced and minimized using the same pipeline as the WT FLVCR2 protein. Minimization was performed 10 times with constraints to preserve the starting coordinates.
`
relax.static.linuxgccrelease -s 8qd0_fill.B99990007_A.pdb -relax:constrain_relax_to_start_coords -relax:ramp_constraints false -relax:respect_resfile  -packing:resfile mutatnt.resfile  
 -ex1 -ex2 -use_input_sc -flip_HNQ -no_optH false  -nstruct 10  -out:file:af_relaxed_8qd0.Arg492Trp_A.sc
`
Results are available in the <a href='/MinimizingStructures/Arg492Trp'>Arg492Trp</a> folder. Scores for minimized structures are in <a href='MinimizingStructures/Arg492Trp/af_relaxed_8qd0.Arg492Trp_A.sc'>af_relaxed_8qd0.Arg492Trp_A.sc</a>.

The structure <a href='/MinimizingStructures/Arg492Trp/8qd0_fill.B99990007_A_0004.pdb'>8qd0_fill.B99990007_A_0004.pdb</a> has the lowest energy: -986.411 REU.

### Evaluating the impact of the Arg492Trp variant using DynaMut2
The results of this evaluation can be seen at the following link: <a href='https://biosig.lab.uq.edu.au/dynamut2/results_prediction/173491533976'>Predicted Stability Change</a>.
