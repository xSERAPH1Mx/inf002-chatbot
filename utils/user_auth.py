import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

class UserAuth:
    def __init__(self):
        with open('auth_config.yaml') as file:
            self.config = yaml.load(file, Loader=SafeLoader)

        # Pre-hashing all plain text passwords once
        # stauth.Hasher.hash_passwords(config['credentials'])

        self.authenticator = stauth.Authenticate(
            self.config['credentials'],
            self.config['cookie']['name'],
            self.config['cookie']['key'],
            self.config['cookie']['expiry_days']
        )

    def login_widget(self):
        try:
            self.authenticator.login()
        except stauth.LoginError as e:
            st.error(e)

    def registration_widget(self):
        try:
            email_of_registered_user, \
                username_of_registered_user, \
                name_of_registered_user = self.authenticator.register_user(roles=['user'])
            if email_of_registered_user:
                with open('auth_config.yaml', 'w') as file:
                    yaml.dump(self.config, file, default_flow_style=False)
                st.success('User registered successfully')
                st.switch_page("pages/Login.py")
        except Exception as e:
            st.error(e)

    def get_authenticator(self):
        return self.authenticator


# with open('../auth_config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)
#
# # Pre-hashing all plain text passwords once
# # stauth.Hasher.hash_passwords(config['credentials'])
#
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days']
# )
#
# #login
# try:
#     authenticator.login()
# except stauth.LoginError as e:
#     st.error(e)
#
# if st.session_state['authentication_status']:
#     authenticator.logout()
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state['authentication_status'] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state['authentication_status'] is None:
#     st.warning('Please enter your username and password')
#
# #reset pass
# if st.session_state['authentication_status']:
#     try:
#         if authenticator.reset_password(st.session_state['username']):
#             with open('auth_config.yaml', 'w') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)
#
#
