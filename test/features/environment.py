from selenium import webdriver

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.get("http://pat.ly:8080")
    context.mapping = {}

def after_scenario(context ,scenario):
    context.browser.quit()