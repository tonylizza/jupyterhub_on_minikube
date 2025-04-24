# hub/jupyterhub_config.py

c = get_config()

# Bind JupyterHub to all interfaces on port 8000 inside the container
c.JupyterHub.bind_url = 'http://:8000'

# Use DummyAuthenticator for simple login during testing
from jupyterhub.auth import DummyAuthenticator
c.JupyterHub.authenticator_class = DummyAuthenticator

# All users must use this fixed password
c.DummyAuthenticator.password = "password"

# Optional: allow any username to log in (default is True)
c.DummyAuthenticator.allowed_users = []  # allow all usernames

# Optional: set admin access for a known test user (uncomment below if needed)
# c.Authenticator.admin_users = {"admin"}
