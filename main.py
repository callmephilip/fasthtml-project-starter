from fasthtml.common import *

app,rt = fast_app(live=true)

def AppLayout(content: FT, current_path: str):
    nav_links = [
        {"name": "Home", "href": "/"},
        {"name": "About", "href": "/about"},
        {"name": "Contact Us", "href": "/contact"},
    ]
    return Div(
        Nav(
            Ul(
                *[Li(A(nl["name"] + ("✅" if current_path == nl["href"] else ""), href=nl["href"])) for nl in nav_links]
            )
        ),
        Hr(),
        content
    )


@rt('/')
def get(request): return AppLayout(content=Div("Home"), current_path=request.url.path)
@rt('/about')
def get(request): return AppLayout(content=Div("About"), current_path=request.url.path)
@rt('/contact')
def get(request): return AppLayout(content=Div("Contact us"), current_path=request.url.path)

serve()
