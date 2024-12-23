from modeller import *
from modeller.automodel import *

log.verbose()
env = Environ()

# Specify directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Define a custom model class for refining missing residues
class MyModel(AutoModel):
    def select_atoms(self):
        # Select regions including gaps (residues 1-77, 292-294, and 503-534)
        return Selection(self.residue_range('1:A', '77:A'),
                         self.residue_range('292:A', '294:A'),
                         self.residue_range('503:A', '534:A'))

a = MyModel(env, alnfile='alignment.ali',
            knowns='8qd0', sequence='8qd0_fill')
a.starting_model = 1
a.ending_model = 10  # Generate 10 models for variability
a.make()
