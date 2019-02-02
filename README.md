# lang_git
A python library to retrieve a GitHub's profile programming languages

```python
from lang_lib import *

# Usage:
# Takes one argument: username (which is the GitHub username)
# This function returns the language for each repository (Max 100)
get_language_list()
# Returns (for example) ['JavaScript','Java', 'JavaScript', 'HTML']

# Takes one argument: username (which is the GitHub username)
# This function returns the unique languages
get_unique_language_list()
# Returns (for example) ['JavaScript','Java' , 'HTML']
```


