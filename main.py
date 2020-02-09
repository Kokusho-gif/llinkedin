import linkedin_controller
from parameters import keyword1, keyword2, keyword3, maximum_invitation,\
    how_many_pages, linkedin_username, linkedin_password

if __name__ == '__main__':

    searching = linkedin_controller.controller()

    searching.login(linkedin_username, linkedin_password)

    # connect_sender(self, keyword1='', keyword2='', keyword3='',
    #                maximum_invitation=10, from_what_page=1,
    #                how_many_pages=100) <= default arguments

    searching.connect_sender('station', 'attendant', '', 10)
    searching.driver.close()
