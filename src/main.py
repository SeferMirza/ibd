from pathlib import Path

import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from api.API import API

if __name__ == '__main__':
   api = API()
   api.app.run() #go to http://localhost:5000/ to view the page.