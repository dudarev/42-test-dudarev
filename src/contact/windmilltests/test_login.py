# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

def test_recordingSuite0():
    client = WindmillTestClient(__name__)

    client.click(id=u'first-column')
    client.click(link=u'Login')
    client.waits.forPageLoad(timeout=u'20000')
    client.type(text=u'admin', id=u'id_username')
    client.type(text=u'admin', id=u'id_password')
    client.click(xpath=u'/html/body/div/form/button')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'Edit', timeout=u'8000')
    client.click(link=u'Edit')
    client.waits.forPageLoad(timeout=u'20000')