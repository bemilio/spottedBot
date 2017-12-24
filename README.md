# spottedBot
Questo è l'inizio del nostro magico bot per trollare spotted.
L'idea è di fare un training sui post di spotted per generare dei post automaticamente e vedere le reazioni.
Prendetelo come un test di turing, però stupido. Chiunque voglia unirsi è benvenuto.

L' idea per ora è di usare textgenrnn ed un API facebook per scaricare i post. Per impostare tutto:

pip install keras
pip install tensorflow
pip install textgenrnn
___________________

from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.generate()
