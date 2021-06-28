import os
from posix import O_CREAT

fdworst = os.open('calledworst.txt', os.O_WRONLY|O_CREAT|os.O_TRUNC, 0o664)
os.close(fdworst)