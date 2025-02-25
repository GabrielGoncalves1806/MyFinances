import views.homeview
import views.add_transaction_view
import views.reports_view

# Função de navegação entre rotas/janelas
def go_to(page, route, data=None):
    print(route)
    for view in page.views:
        if route == view.route:
            page.views.pop()
            page.go(view.route)
            return
            
    if route == "/add":
        views.add_transaction_view.AddTransacaoView(page)
        
    elif route == "/homeview":
        views.homeview.HomeView(page)
    
    elif route == "/reports":
        views.reports_view.ReportsView(page)
        
# Função que volta até a home
def go_home(page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
