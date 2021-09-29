
from selenium import webdriver

from fpdf import FPDF

driver = webdriver.Chrome(executable_path="c:\selenium browser drivers\chromedriver.exe")

driver.maximize_window()
driver.get("https://superbinc.ca/login")
driver.find_element_by_name("email").send_keys("ravinder1way@yopmail.com")
driver.find_element_by_name("password").send_keys("admin@123")
driver.find_element_by_xpath('//button[contains(text(),\'Login to Account\')]').click()

pdf = FPDF()

# save FPDF() class into a
# variable pdf

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)

# create a cell
pdf.cell(200, 10, txt="Login successfull",
         ln=1, align='C')

# add another cell
pdf.cell(200, 10, txt="Enjoy your Day!",ln=2, align='C')

# save the pdf with name .pdf
pdf.output("login.pdf")
