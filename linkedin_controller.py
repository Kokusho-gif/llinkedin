from selenium import webdriver
from time import sleep
import parameters


class controller():

    def __init__(self):
        # specifies the path to the chromedriver.exe
        self.driver = webdriver.Chrome()

    def login(self, linkedin_username, linkedin_password):

        # driver.get method() will navigate to a page given by the URL address
        self.driver.get('https://www.linkedin.com')
        sleep(1)

        # locate submit button by_class_name
        sign_in_button = self.driver.find_element_by_class_name('nav__button-secondary')

        # .click() to mimic button click
        sign_in_button.click()

        # locate email form by_class_name
        username = self.driver.find_element_by_id('username')

        # send_keys() to simulate key strokes
        username.send_keys(linkedin_username)

        # locate password form by_class_name
        password = self.driver.find_element_by_id('password')

        # send_keys() to simulate key strokes
        password.send_keys(linkedin_password)

        # locate submit button by_class_name
        log_in_button = self.driver.find_element_by_class_name(
            'login__form_action_container ')

        # .click() to mimic button click
        log_in_button.click()

        sleep(1)


    def connect_sender(self, keyword1='', keyword2='', keyword3='',
                       maximum_invitation=10, from_what_page=1, how_many_pages=100):

        print(f'Start connecting with {keyword1}, {keyword2}, {keyword3}')
        count = 0
        connect_buttons=[]

        concatenation_link_to_keyword = \
            f"https://www.linkedin.com/search/results/people/?keywords={keyword1}"

        if keyword2:
            concatenation_link_to_keyword += f'%20{keyword2}'
        if keyword3:
            concatenation_link_to_keyword += f'%20{keyword3}'

        for page in range(from_what_page, from_what_page+how_many_pages+1):

            if count >= maximum_invitation:
                break

            self.driver.get(concatenation_link_to_keyword+f"&page={page}")

            sleep(2)

            print("I\'m now on page:%s" % (page))

            # Scroll to the bottom of the page to get all button-elements
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")

            # Get all button-elements
            connect_buttons = self.driver.find_elements_by_class_name(
                'search-result__action-button')

            # Scroll to the summit of the page
            # to driver could recognize button accurately
            self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

            if connect_buttons:
                print(f'{len(connect_buttons)} people founded in page{page}')

                for i in range(len(connect_buttons)-1):

                    print('I\'m now on index:%s' % i)

                    connect_buttons[i].click()

                    # Pop up window comes up when click 'connect' button
                    # So below 3 codes for vanish it
                    if self.driver.find_elements_by_class_name('artdeco-modal__dismiss'):

                        back_button = self.driver.find_elements_by_class_name(
                            'artdeco-modal__dismiss')
                        back_button[0].click()
                        count += 1

                    sleep(1.2)

                    if count%10 == 0:
                        print(
                            f"Invited {count} people[Invited/Maximum >>"
                            f" {count}/{maximum_invitation}]")

                    # This program will be interrupted
                    # when invitations go the maximum number
                    # from argument specifying
                    if count >= maximum_invitation:

                        print(f'Invited {maximum_invitation} people. '
                              f'For not getting a restriction from LinkedIn, '
                              f'this program will stop')

                        print('Current page:%s' % page)
                        print('Invited people:%s' % maximum_invitation)
                        print('------------------------------------')
                        break




