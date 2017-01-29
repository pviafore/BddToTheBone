@given(u'a url {url}')
def step_impl(context, url):
    context.url = url

@given(u'we have shortened the url {url}')
def step_impl(context, url):
    context.shortened_url = ""
    raise NotImplementedError(u'STEP: Given we have shortened the url ' + url)

@given(u'we navigate to that shortened url {num_times} times')
def step_impl(context, num_times):
    # go to the url 
    raise NotImplementedError(u'STEP: Given we navigate to that shortened url {} times'.format(num_times))

@when(u'we shorten it through our service')
def step_impl(context):
    # make a request through our service
    raise NotImplementedError(u'STEP: When we shorten it through our service')

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
