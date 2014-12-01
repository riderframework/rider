from rider import conf
conf.SERVERS = (
    ('server.TestServer', [[('server.TestWsgiServer', [], {})]], {}),
)
