import time
from selene.api import *

config.browser_name = 'chrome'
base_url = ".test-env.scalr.com/"
farmsquery = ".test-env.scalr.com/#/farms?query="



def test_goto_container(containerid):
    config.browser_name
    browser.visit('http://' + containerid + base_url)


def test_login_farm(login, password):
    config.browser_name
    s('#textfield-user-login-inputEl').set_value(login)
    s('#textfield-user-password-inputEl').set_value(password)
    time.sleep(1)
    s('#button-1030').click()
    time.sleep(2)


def test_search_farm(containerid, farmid):
    config.browser_name
    browser.visit('http://' + containerid + farmsquery + farmid)
    s('.x-grid-icon-configure').click()
    time.sleep(3)


def test_quick_start():
    config.browser_name
    s(by.xpath("//a[.='Add farm role']")).click()
    time.sleep(2)
    s(by.xpath("//*[.='Quick start']")).click()
    s(by.xpath("//*[.='MySQL']")).click()
    time.sleep(3)


def test_search_by_field(farmrole, scope):
    config.browser_name
    s(by.xpath("//a[.='Add farm role']")).click()
    time.sleep(3)
    s(by.xpath("//*[.='Base']")).click()
    s("div.x-form-text-wrap-focus> input").set_value(farmrole)
    time.sleep(2)
    s(scope).click()
    time.sleep(2)


def test_add_role():
    config.browser_name
    s(by.xpath("//a[.='Add to farm']")).click()
    time.sleep(1)
    s(by.xpath("//a[.='Save farm']")).click()
    time.sleep(1)


def test_launch(containerid, farmid):
    config.browser_name
    browser.visit('http://' + containerid + farmsquery + farmid)
    time.sleep(3)
    s(".x-grid-icon-launch").click()
    s("a.x-btn-default-small-focus").click()