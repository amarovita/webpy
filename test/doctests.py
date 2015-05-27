"""Run all doctests in w3.py.
"""
import webtest

def suite():
    modules = [
        "w3.application",
        "w3.db",
        "w3.form",
        "w3.http", 
        "w3.net", 
        "w3.session",
        "w3.template",
        "w3.utils", 
#        "w3.webapi", 
#        "w3.wsgi", 
    ]
    return webtest.doctest_suite(modules)
    
if __name__ == "__main__":
    webtest.main()
