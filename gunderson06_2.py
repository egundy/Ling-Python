'''Let's revise your Pig Latin program so that it correctly handles uppercase letters and punctuation 
marks such as commas, periods, questions marks, and exclamation marks. If an English word 
begins with an uppercase letter, then its Pig Latin representation should also begin with an 
uppercase, and the uppercase letter moved to the end of the word should be changed to 
lowercase. For example, Computer should become Omputercay. If a word ends in a punctuation 
mark, then the punctuation mark should remain at the end of the word after the transformation 
has been performed. For example, Linguistics! should become Inguisticslay! '''

import re
