# coding=utf-8

import mechanize
import cookielib
"""
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.set_debug_http(False)

br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')]

response = br.open('http://eip.chinatowercom.cn')
br.select_form(nr=0)
br.form['username'] = 'sunzf'
br.form['password'] = 'seven7'
br.submit()
print 'login successful!'
"""
file = open('infoTest.txt', 'r')
data_input = []
for line in file.readlines():
    data_input = line.strip('\n').split(',')
    print data_input[2]


"""
     = info[1]
    configID = info[2]
    sourceID = info[3]
"""
file.close()