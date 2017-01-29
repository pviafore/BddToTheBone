from requests import get

@given(u'a url {url}')
def step_impl(context, url):
    context.url = url

@given(u'we have shortened the url {url}')
def step_impl(context, url):
    context.browser.find_element_by_id("input").send_keys(url)
    context.browser.find_element_by_id("get-short-link").click()
    context.url = url
    context.shortened_url = browser.find_element_by_id("return-link").text

@given(u'we navigate to that shortened url {num_times} times')
def step_impl(context, num_times):
    # go to the url 
    for _ in range(num_times):
        context.browser.get(context.shortened_url)

@when(u'we shorten it through our service')
def step_impl(context):
    context.browser.find_element_by_id("input").send_keys(context.url)
    context.browser.find_element_by_id("get-short-link").click()
    context.shortened_url = browser.find_element_by_id("return-link").text

@when(u'we navigate to that shortened URL')
def step_impl(context):
    #navigate to the url
    raise NotImplementedError(u'STEP: When we navigate to that shortened URL')

@when(u'we look at the stats on the homepage')
def step_impl(context):
    # retrieve stats
    context.stats = {}
    raise NotImplementedError(u'STEP: When we look at the stats on the homepage')


@then(u'we arrive at the {url} as fast as possible')
def step_impl(context, url):
    #how do we test this?
    raise NotImplementedError(u'STEP: Then we arrive at the {} as fast as possible'.format(url))

@then(u'we should receive a shortened URL')
def step_impl(context):
    #receive the shortened url
    context.shortened_url=""

@then(u'we see the shortened URL for {url} has been visited {num_times} times')
def step_impl(context, url, num_times):
    assert context.stats[url] == num_times
