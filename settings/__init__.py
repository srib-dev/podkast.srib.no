import os
from dotenv import load_dotenv

# loads in the environment variables
load_dotenv()
env = os.environ.get('ENVIRON', "<unknown>" )

print("environ:", env)

match env:
    
    case "Production":
        print("importing production environment settings...")
        from .production import *

    case "Development":
        print("importing development environment settings...")
        from .development import *

    case "Staging":
        print("importing staging environment settings...")
        from .staging import *

    case _:
        raise ValueError(f"Unknown environment: {env}")