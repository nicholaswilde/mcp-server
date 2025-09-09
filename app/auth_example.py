import os

from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

# --- Configuration ---
# In a real application, use a .env file or other secure configuration method.
# You can get these values from your Authentik Provider settings.
AUTHENTIK_CLIENT_ID = os.getenv("AUTHENTIK_CLIENT_ID", "your-client-id")
AUTHENTIK_CLIENT_SECRET = os.getenv("AUTHENTIK_CLIENT_SECRET", "your-client-secret")
AUTHENTIK_DISCOVERY_URL = os.getenv(
    "AUTHENTIK_DISCOVERY_URL",
    "https://<your-authentik-domain>/application/o/<your-app-slug>/.well-known/openid-configuration",
)
# This key is used to sign the session cookie. Generate a secure random key for production.
SESSION_SECRET_KEY = os.getenv("SESSION_SECRET_KEY", "a-very-secret-key-that-you-should-change")

# Create the FastAPI app instance
app = FastAPI()

# Add session middleware from Starlette.
# This is required for storing the user's session data in a secure, signed cookie.
app.add_middleware(
    SessionMiddleware,
    secret_key=SESSION_SECRET_KEY,
    session_cookie="fastapi_session",
    max_age=14 * 24 * 60 * 60,  # Session expires in 14 days
)

# Create an OAuth client instance from Authlib
oauth = OAuth()

# Register the Authentik OIDC provider with Authlib.
# This uses the discovery URL to automatically configure the necessary endpoints.
oauth.register(
    name="authentik",
    client_id=AUTHENTIK_CLIENT_ID,
    client_secret=AUTHENTIK_CLIENT_SECRET,
    server_metadata_url=AUTHENTIK_DISCOVERY_URL,
    client_kwargs={
        "scope": "openid email profile"  # Standard OIDC scopes to request user details
    },
)


# --- Application Routes ---


@app.get("/")
async def homepage(request: Request) -> HTMLResponse:
    """Displays the homepage.

    Shows user info and a logout link if authenticated,
    otherwise shows a login link.
    """
    user = request.session.get("user")
    if user:
        return HTMLResponse(
            f"""
            <h1>Hello, {user.get("name", "user")}!</h1>
            <p>Email: {user.get("email")}</p>
            <p>Your user info from Authentik:</p>
            <pre>{user}</pre>
            <a href="/protected">Test Protected Route</a><br><br>
            <a href="/logout">Logout</a>
        """
        )
    return HTMLResponse('<h1>Welcome!</h1><p>You are not logged in.</p><a href="/login">Login with Authentik</a>')


@app.get("/login")
async def login(request: Request) -> RedirectResponse:
    """Initiates the OIDC login flow by redirecting the user to Authentik."""
    # The redirect_uri must match exactly one of the URIs you configured in your Authentik provider.
    redirect_uri = request.url_for("auth")
    return await oauth.authentik.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request) -> HTMLResponse | RedirectResponse:
    """This is the callback route.

    Authentik redirects the user here after a successful login.
    The function exchanges the authorization code for an access token and retrieves user info.
    """
    try:
        token = await oauth.authentik.authorize_access_token(request)
    except Exception as e:
        return HTMLResponse(
            f"<h1>Error</h1><p>Could not retrieve access token: {e}</p>",
            status_code=400,
        )

    # The token dictionary contains 'access_token', 'id_token', etc.
    # Authlib automatically parses the 'id_token' to get user info.
    user_info = token.get("userinfo")
    if user_info:
        # Store the user's information in the session cookie.
        request.session["user"] = dict(user_info)

    return RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: Request) -> RedirectResponse:
    """Clears the user session cookie and logs them out."""
    request.session.pop("user", None)
    return RedirectResponse(url="/")


@app.get("/protected")
async def protected_route(request: Request) -> HTMLResponse | RedirectResponse:
    """An example of a protected route.

    It checks for a valid session.
    If the user is not logged in, it redirects them to the login page.
    """
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/login")

    return HTMLResponse(
        f"""<h1>Protected Area</h1><p>Welcome, {user.get("name", "user")}!</p>
        <p>Only authenticated users can see this.</p>"""
    )
