from selenium import webdriver

url = "http://testing-ground.scraping.pro/ajax"

def find_xpath(element, target, path):
    if target in element.get_attribute('textcontent') and element.get_tag == 'ul':
        return path
    new_elements = element.find_elements_by_xpath('./*')
    for element in new_elements:
        final = find_xpath(element, target, path+'/'+element.tag_name)
        if final != '':
            return final
    return ''

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.get(url)

elements = driver.find_element_by_xpath("html")
print(elements.text)
driver.quit()