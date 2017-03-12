from page_modules import pages

login = 'test@scalr.com'
password = '**********'
containerid = '8104b4ffeb57'
farmid = '9800012'


def test_go():
    pages.test_goto_container(containerid)
    pages.test_login_farm(login, password)
    pages.test_search_farm(containerid, farmid)
    pages.test_quick_start()
    pages.test_add_role()
    pages.test_launch(containerid, farmid)

