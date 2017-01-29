
@given(u'a url {url}')
def step_impl(context, url):
    context.url = url

@given(u'we have shortened the url {url}')
def step_impl(context, url):
    context.browser.find_element_by_id("input").send_keys(url)
    context.browser.find_element_by_id("get-short-link").click()
    context.url = url
    context.shortened_url = context.browser.find_element_by_id("return-link").text
    context.mapping[context.url] = context.shortened_url

@given(u'we navigate to that shortened url {num_times} times')
def step_impl(context, num_times):
    # go to the url 
    for _ in range(int(num_times)):
        context.browser.get(context.shortened_url)
    #reset back to the original page
    context.browser.get("http://pat.ly:8080")

@when(u'we shorten it through our service')
def step_impl(context):
    context.browser.find_element_by_id("input").send_keys(context.url)
    context.browser.find_element_by_id("get-short-link").click()
    context.shortened_url = context.browser.find_element_by_id("return-link").text

@when(u'we navigate to that shortened URL')
def step_impl(context):
    context.browser.get(context.shortened_url)

@when(u'we look at the stats on the homepage')
def step_impl(context):
    context.stats = {}
    table = context.browser.find_element_by_id("stats")
    for row in table.find_elements_by_tag_name("tr")[1:]:
        cells = row.find_elements_by_tag_name("td")
        context.stats[cells[0]] = cells[1]


@then(u'we arrive at {url} as fast as possible')
def step_impl(context, url):
    assert url == context.browser.current_url
    #how do we test speed?

@then(u'we should receive a shortened URL')
def step_impl(context):
    assert context.browser.find_element_by_id("return-link").text.startswith("http://pat.ly:8080")

@then(u'we see the shortened URL for {url} has been visited {num_times} times')
def step_impl(context, url, num_times):
    #this is the step that should fail, given our implementation
    assert context.stats[context.mapping[url]] == num_times
