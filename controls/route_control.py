import views
from views import add_transacao_view, homeview
import views.add_transacao_view
import views.homeview

# Função de navegação entre rotas/janelas


def go_to(page, route, data=None):
    print(route)
    for view in page.views:
        if route == view.route:
            page.views.pop()
            page.go(view.route)
            return
            
    if route == "/add":
        views.add_transacao_view(page)
        
    elif route == "/homeview":
        views.homeview.HomeView(page)
        
# Função que volta até a home
def go_home(page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
