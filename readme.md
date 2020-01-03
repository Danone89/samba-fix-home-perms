# Samba Home Permission Fixer

Samba fix perms is python script for mass changing home's directories permissions.
If yours home are stored as /home/%u (where %u is user login) you can use this script to correct file permissions on disk. It's handy when:

  - you moved/migrate homes from source without correct perms.
  - your ldb or idmap got corrupted
  - created new domain with old files
  
# Prerequisites

Python 3.x

# Usage

Just copy to directory where you store user direcctories. 

> //for /home/SAMDOM/<login>
> cp fixperms.py /home/SAMDOM
> python fixperms.py

# licence
MIT
