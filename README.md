# List-up-references
Make a reference list from the main text of a manuscript. The list can be used for manual check of consistency between references in main text and reference list. 

The main script is listup_references_from_manuscript.py, and you can run 
python -i listup_references_from_manuscript.py

You will be asked to type in the input file name (manuscript text file) and output file name (output list file). 

For exapmle, the following list ("ref.txt" in this repository)

Adam 1910  
Baker and Clark 1920  
Davis et al. 1930  
Evans-Smith 2000  
Francis et al. 2010a  
Francis et al. 2010b  
Kucieńska et al. 2015  
Neumann 2050  

is extracted from the "sample_input_file.txt" in this repository. The extraction is correct except for the last one, which is actually "von Neumann 2050", but the current version simply ignores "von". 

