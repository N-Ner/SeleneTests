from page_modules import pages

login = 'test@scalr.com'
password = '**********'
containerid = '8104b4ffeb57'
farmid = '9800012'
farmrole = 'base-ubuntu1404'
#Uncomment the line for Scope settings
#scope = "img[data-qtip='This Role is defined in the Scalr Scope']"
#scope = "img[data-qtip='TThis Role is defined in the Account Scope']"
scope = "img[data-qtip='This Role is defined in the Environment Scope']"


def test_go():
    pages.test_goto_container(containerid)
    pages.test_login_farm(login, password)
    pages.test_search_farm(containerid, farmid)
    pages.test_search_by_field(farmrole, scope)
    pages.test_add_role()
    pages.test_launch(containerid, farmid)