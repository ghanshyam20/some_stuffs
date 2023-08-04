

#like ,txt="I love python"
# the result must be => "I","love","Python"
# question bujhiyaxa ??????

import re

txt="I love python"

y=re.split("\s",txt)
print(y)